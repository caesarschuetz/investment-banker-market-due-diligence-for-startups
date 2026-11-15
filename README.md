# Investment Banker Market Due Diligence for Startups

An agent skill that puts a startup idea through the market due diligence an investment banker would run, and returns a sourced paper with a verdict.

You give it an idea. It returns a paper, in Markdown and PDF, that covers market size, business models, 12 to 20 player profiles, comps, precedent transactions, the graveyard, demand evidence, a gap check, exit math and a scorecard, with every number traceable to a source.

**See what it produces:** [example report (PDF, 12 pages)](examples/ai-native-wealth-advice-us/report.pdf) · [Markdown](examples/ai-native-wealth-advice-us/report.md) · [evidence log](examples/ai-native-wealth-advice-us/evidence.csv)

## Why this exists

Ask a model for market research and you usually get a list of competitors, a market-size figure with no source, and an encouraging conclusion. That is no use for deciding whether to spend two years on something.

This skill makes the model work like a banker's analyst preparing a deal. It runs what consultants call a commercial due diligence on the market (size, money flow, players, demand, gaps) and adds the three blocks from a banker's valuation work: comps, precedent transactions and exit math. One thing is deliberately different: a banker writes to sell the deal, and this report is written for the person who would lose the money. Four rules do most of the work:

1. **Every number carries a source, a date and a read status.** The evidence log records whether the page was opened, partly read, only seen as a search snippet, or whether the figure is the model's own calculation.
2. **A gap is a claim to disprove.** "Nobody does this" counts only after searches designed to find an occupant have failed, and after the neighbours, the incumbents and the graveyard have been checked.
3. **Conflicts and corrections stay visible.** When sources disagree, both are shown. When the run corrects itself, the report says so.
4. **The verdict comes first.** Page one says go, go with conditions, or no-go, and why.

The method comes from a real run in November 2026: a founder's idea for AI-native wealth advice, researched over several days. The mistakes made along the way are in the skill as "failure modes", so the next run does not repeat them.

## What the report contains

| Section | What it answers |
|---|---|
| 1. Verdict | Go or no-go, the facts that decide it, the scorecard |
| 2. Idea and scope | Who pays whom, how much, for what |
| 3. Market size and money flow | How much is already paid for this job, and where the price goes |
| 4. Business models | The four to eight ways the market is served today |
| 5. Players | 12 to 20 profiles: price, traction, funding |
| 6. What the winners do | Channel, pricing moves, economics |
| 7. Comps | What comparable companies are worth, as a multiple |
| 8. Precedent transactions | Funding rounds and exits, including the bad ones |
| 9. Graveyard and absentees | Who failed, and who could do this but does not |
| 10. Demand evidence | Behaviour first, surveys last |
| 11. Gap check | Each candidate gap with the searches run against it |
| 12. Exit math | What a $1B outcome needs in revenue, customers and share |
| 13. Theses | How this market works, with evidence for and against |
| 14. Scorecard | Seven criteria, green, yellow or red |
| 15 to 17 | Risks and next test, corrections and open questions, sources |

## Install

**Claude (web, desktop, mobile).** Download [`investment-banker-market-due-diligence-for-startups.zip`](https://github.com/caesarschuetz/investment-banker-market-due-diligence-for-startups/raw/main/dist/investment-banker-market-due-diligence-for-startups.zip) and add it under Customize → Skills. Code execution has to be enabled. Anthropic's guide: [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

**Claude Code.**

```bash
git clone https://github.com/caesarschuetz/investment-banker-market-due-diligence-for-startups.git
mkdir -p ~/.claude/skills
cp -r investment-banker-market-due-diligence-for-startups/skills/investment-banker-market-due-diligence-for-startups ~/.claude/skills/
```

**Other agents.** With the [skills CLI](https://skills.sh) (Node.js 22.20 or later):

```bash
npx skills add caesarschuetz/investment-banker-market-due-diligence-for-startups
```

**Any model with web search.** Paste the contents of [`SKILL.md`](skills/investment-banker-market-due-diligence-for-startups/SKILL.md) as instructions, then describe the idea. The file is self-contained for the analysis. For the typeset PDF it tells the model to fetch the script from this repository, and to say so.

## Use

Describe the idea and the market. For example:

```text
Run an investment banker market due diligence on this idea: an AI-native
surety bond provider for small contractors in the US, sold through bond agents.
```

```text
/investment-banker-market-due-diligence-for-startups Subscription meal kits for dialysis patients in Germany
```

```text
Is there a market for this? A marketplace that lets independent pharmacies
in the UK buy generics together. Quick scan first.
```

The skill asks at most three questions (country, customer, how the company earns money), then works through thirteen steps and delivers a folder:

```text
dd-<idea>/
  report.md       the paper
  evidence.csv    every fact with source, date and read status
  report.pdf      the paper, typeset
```

A full run opens forty or more sources and takes a while. Ask for a "quick scan" to halve the depth.

## Requirements

- A model with live web search and the ability to open pages. Without them the skill stops and says so, because numbers from memory cannot be checked.
- For the PDF: Python 3 with the `markdown` package, and one of Playwright with Chromium, Chrome or Chromium, wkhtmltopdf, or pandoc with a LaTeX engine. Without any of these you still get the Markdown report.

To build a PDF by hand:

```bash
python skills/investment-banker-market-due-diligence-for-startups/scripts/build_pdf.py dd-my-idea/report.md
```

## Limits

- The report is only as good as the public sources. Private companies disclose little, and the report says "n/d" where they do.
- A model can still misread a page. The evidence log exists so that you can check the facts that matter to you.
- A "no-go" is a statement about the idea as framed, in that market, on that date. Markets move.
- "Investment banker" describes the method: comps, precedent transactions and exit math on top of a market due diligence. No bank wrote or reviewed this skill.
- This is research support. It is not investment, legal or tax advice.

## Repository layout

```text
skills/investment-banker-market-due-diligence-for-startups/
  SKILL.md                    the workflow and the rules
  references/
    evidence-rules.md         sourcing, dating, read status, corrections
    search-playbook.md        query patterns for each step
    scorecard.md              scoring anchors, exit math, verdict rules
  templates/
    report.md                 the report skeleton
    evidence.csv              the log header
  scripts/
    build_pdf.py              Markdown to PDF
    print.css                 the print stylesheet
    fonts/                    Source Serif 4 and IBM Plex Sans (SIL OFL 1.1)
examples/
  ai-native-wealth-advice-us/ a complete public example
dist/
  investment-banker-market-due-diligence-for-startups.zip  the skill folder, ready to upload
```

After changing the skill, rebuild the upload file:

```bash
cd skills && zip -r ../dist/investment-banker-market-due-diligence-for-startups.zip investment-banker-market-due-diligence-for-startups -x "*/__pycache__/*" "*.DS_Store"
```

## License

MIT for the skill, see [LICENSE](LICENSE). The bundled fonts are under the SIL Open Font License 1.1; their license texts are in `skills/investment-banker-market-due-diligence-for-startups/scripts/fonts/`.

Made by [Caesar Schütz](https://github.com/caesarschuetz).
