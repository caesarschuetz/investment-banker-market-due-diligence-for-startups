# Fonts

The PDF uses two typefaces, both distributed under the SIL Open Font License, Version 1.1:

- **Source Serif 4** for text. License: `OFL-SourceSerif4.txt`.
- **IBM Plex Sans** for headings and tables. License: `OFL-IBMPlexSans.txt`.

The files are the Latin and Latin Extended subsets from the `@fontsource/source-serif-4` and `@fontsource/ibm-plex-sans` packages, unmodified. `build_pdf.py` inlines them into the HTML it prints. If this folder is missing, the stylesheet falls back to system fonts.
