#!/usr/bin/env python3
"""Build a PDF from a Markdown due diligence report.

Usage:
    python build_pdf.py report.md [-o report.pdf] [--paper a4|letter] [--keep-html]

The script converts Markdown to HTML, applies print.css and the bundled fonts,
and prints the page with the first engine it finds:

    1. Playwright with Chromium (Python package "playwright")
    2. A Chrome or Chromium binary on the PATH (headless)
    3. wkhtmltopdf
    4. pandoc with any PDF engine it can find

If none is available it leaves the HTML file next to the Markdown file and
exits with code 1, so the caller can say that no PDF was built.
"""

from __future__ import annotations

import argparse
import base64
import html as html_lib
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FONT_DIR = HERE / "fonts"

LATIN = (
    "U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, "
    "U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, "
    "U+FEFF, U+FFFD"
)
LATIN_EXT = (
    "U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, "
    "U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, "
    "U+2113, U+2C60-2C7F, U+A720-A7FF"
)

# (family, file stem, weight, style)
FONTS = [
    ("Source Serif 4", "source-serif-4-{subset}-400-normal", 400, "normal"),
    ("Source Serif 4", "source-serif-4-{subset}-400-italic", 400, "italic"),
    ("Source Serif 4", "source-serif-4-{subset}-600-normal", 600, "normal"),
    ("Source Serif 4", "source-serif-4-{subset}-700-normal", 700, "normal"),
    ("IBM Plex Sans", "ibm-plex-sans-{subset}-400-normal", 400, "normal"),
    ("IBM Plex Sans", "ibm-plex-sans-{subset}-600-normal", 600, "normal"),
    ("IBM Plex Sans", "ibm-plex-sans-{subset}-700-normal", 700, "normal"),
]

# Words that mark a traffic-light score when they are the only content of a table cell.
SCORE_WORDS = {
    "go": {"green", "grün", "gruen", "vert", "verde", "groen"},
    "wait": {"yellow", "amber", "gelb", "jaune", "amarillo", "giallo", "amarelo", "geel"},
    "stop": {"red", "rot", "rouge", "rojo", "rosso", "vermelho", "rood"},
}

PAPER = {
    "a4": {"playwright": "A4", "wk": "A4", "css": "A4"},
    "letter": {"playwright": "Letter", "wk": "Letter", "css": "Letter"},
}


def font_css() -> str:
    """Inline the bundled fonts as data URIs so the HTML renders the same everywhere."""
    if not FONT_DIR.is_dir():
        return ""
    rules = []
    for family, stem, weight, style in FONTS:
        for subset, unicode_range in (("latin", LATIN), ("latin-ext", LATIN_EXT)):
            path = FONT_DIR / (stem.format(subset=subset) + ".woff2")
            if not path.is_file():
                continue
            data = base64.b64encode(path.read_bytes()).decode("ascii")
            rules.append(
                "@font-face {"
                f"font-family: '{family}'; font-weight: {weight}; font-style: {style}; "
                f"src: url(data:font/woff2;base64,{data}) format('woff2'); "
                f"unicode-range: {unicode_range};"
                "}"
            )
    return "\n".join(rules)


def markdown_to_html(text: str) -> str:
    try:
        import markdown  # type: ignore
    except ImportError:
        pandoc = shutil.which("pandoc")
        if not pandoc:
            sys.exit(
                "Neither the Python package 'markdown' nor pandoc is available. "
                "Install one of them: pip install markdown"
            )
        result = subprocess.run(
            [pandoc, "-f", "gfm", "-t", "html"],
            input=text.encode("utf-8"),
            capture_output=True,
            check=True,
        )
        return result.stdout.decode("utf-8")
    return markdown.markdown(
        text,
        extensions=["tables", "footnotes", "sane_lists", "attr_list", "fenced_code"],
        output_format="html5",
    )


def mark_scores(body: str) -> str:
    """Wrap table cells that hold only a score word in a styled span."""

    def repl(match: re.Match) -> str:
        open_tag, inner, close_tag = match.group(1), match.group(2), match.group(3)
        word = re.sub(r"<[^>]+>", "", inner).strip().lower()
        for kind, words in SCORE_WORDS.items():
            if word in words:
                label = re.sub(r"<[^>]+>", "", inner).strip()
                return f'{open_tag}<span class="score score-{kind}">{label}</span>{close_tag}'
        return match.group(0)

    return re.sub(r"(<td[^>]*>)(.*?)(</td>)", repl, body, flags=re.S)


def build_html(md_path: Path, paper: str) -> str:
    text = md_path.read_text(encoding="utf-8")
    body = mark_scores(markdown_to_html(text))
    title_match = re.search(r"^#\s+(.+)$", text, flags=re.M)
    title = title_match.group(1).strip() if title_match else md_path.stem
    css_path = HERE / "print.css"
    css = css_path.read_text(encoding="utf-8") if css_path.is_file() else ""
    if paper != "a4":
        css = css.replace("size: A4;", f"size: {PAPER[paper]['css']};")
    return (
        "<!doctype html>\n<html><head><meta charset='utf-8'>"
        f"<title>{html_lib.escape(title)}</title>"
        f"<style>{font_css()}\n{css}</style></head>"
        f"<body>{body}</body></html>"
    )


FOOTER = (
    "<div style=\"font-family: Arial, sans-serif; font-size: 7.5px; color: #646a76; "
    "width: 100%; padding: 0 18mm; display: flex; justify-content: space-between;\">"
    "<span class=\"title\"></span>"
    "<span><span class=\"pageNumber\"></span> / <span class=\"totalPages\"></span></span></div>"
)


def with_playwright(html_path: Path, pdf_path: Path, paper: str) -> bool:
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except ImportError:
        return False
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(html_path.as_uri())
            page.evaluate("document.fonts.ready")
            page.pdf(
                path=str(pdf_path),
                format=PAPER[paper]["playwright"],
                print_background=True,
                prefer_css_page_size=True,
                display_header_footer=True,
                header_template="<span></span>",
                footer_template=FOOTER,
            )
            browser.close()
        return pdf_path.is_file()
    except Exception as exc:  # browser missing, sandbox refused, and so on
        print(f"Playwright could not print: {exc}", file=sys.stderr)
        return False


def with_chrome(html_path: Path, pdf_path: Path) -> bool:
    for name in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable", "chrome", "msedge"):
        binary = shutil.which(name)
        if not binary:
            continue
        for no_header in ("--no-pdf-header-footer", "--print-to-pdf-no-header"):
            cmd = [
                binary, "--headless", "--disable-gpu", "--no-sandbox", no_header,
                f"--print-to-pdf={pdf_path}", html_path.as_uri(),
            ]
            try:
                subprocess.run(cmd, capture_output=True, check=True, timeout=120)
            except Exception:
                continue
            if pdf_path.is_file() and pdf_path.stat().st_size > 0:
                return True
    return False


def with_wkhtmltopdf(html_path: Path, pdf_path: Path, paper: str) -> bool:
    binary = shutil.which("wkhtmltopdf")
    if not binary:
        return False
    cmd = [
        binary, "--quiet", "--enable-local-file-access", "-s", PAPER[paper]["wk"],
        "-T", "19mm", "-B", "20mm", "-L", "18mm", "-R", "18mm",
        "--footer-right", "[page] / [toPage]", "--footer-font-size", "7",
        str(html_path), str(pdf_path),
    ]
    try:
        subprocess.run(cmd, capture_output=True, check=True, timeout=180)
    except Exception as exc:
        print(f"wkhtmltopdf could not print: {exc}", file=sys.stderr)
        return False
    return pdf_path.is_file()


def with_pandoc(md_path: Path, pdf_path: Path) -> bool:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        return False
    for engine in ("xelatex", "lualatex", "pdflatex", "tectonic", "weasyprint"):
        if not shutil.which(engine):
            continue
        # pandoc's own Markdown reader wraps wide tables to the page; the gfm reader does not.
        # Dollar signs are amounts here, not TeX math, and a leading rule is not a YAML block.
        cmd = [pandoc, "-f", "markdown-tex_math_dollars-raw_tex-yaml_metadata_block",
               str(md_path), "-o", str(pdf_path), f"--pdf-engine={engine}",
               "-V", "geometry:margin=2cm", "-V", "fontsize=10pt", "-V", "colorlinks=true"]
        try:
            subprocess.run(cmd, capture_output=True, check=True, timeout=300)
        except Exception:
            continue
        if pdf_path.is_file():
            return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a PDF from a Markdown due diligence report.")
    parser.add_argument("markdown", type=Path, help="path to report.md")
    parser.add_argument("-o", "--output", type=Path, help="path of the PDF (default: next to the Markdown file)")
    parser.add_argument("--paper", choices=sorted(PAPER), default="a4")
    parser.add_argument("--keep-html", action="store_true", help="keep the intermediate HTML file")
    args = parser.parse_args()

    md_path = args.markdown.resolve()
    if not md_path.is_file():
        sys.exit(f"File not found: {md_path}")
    pdf_path = (args.output or md_path.with_suffix(".pdf")).resolve()
    html_path = md_path.with_suffix(".print.html")
    html_path.write_text(build_html(md_path, args.paper), encoding="utf-8")

    engine = None
    if with_playwright(html_path, pdf_path, args.paper):
        engine = "Playwright with Chromium"
    elif with_chrome(html_path, pdf_path):
        engine = "headless Chrome"
    elif with_wkhtmltopdf(html_path, pdf_path, args.paper):
        engine = "wkhtmltopdf"
    elif with_pandoc(md_path, pdf_path):
        engine = "pandoc"

    if engine is None:
        print(
            "No PDF engine found. Install one of: playwright (pip install playwright && "
            "playwright install chromium), Chrome or Chromium, wkhtmltopdf, or pandoc with a "
            f"LaTeX engine. The HTML render is at {html_path}.",
            file=sys.stderr,
        )
        return 1

    if not args.keep_html:
        html_path.unlink(missing_ok=True)

    pages = ""
    try:
        from pypdf import PdfReader  # type: ignore

        pages = f", {len(PdfReader(str(pdf_path)).pages)} pages"
    except Exception:
        pass
    print(f"Wrote {pdf_path} with {engine}{pages}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
