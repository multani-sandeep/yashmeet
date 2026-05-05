#!/usr/bin/env python3
"""Convert Markdown files to styled HTML exam papers. Output always goes to year9/dump/."""

import sys
import re
from pathlib import Path
import markdown

REPO_ROOT = Path(__file__).parent.parent
DUMP_DIR = REPO_ROOT / "year9" / "dump"

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <script>
    MathJax = {{
      tex: {{ inlineMath: [['$','$']], displayMath: [['$$','$$']] }},
      options: {{ skipHtmlTags: ['script','noscript','style','textarea','pre'] }}
    }};
  </script>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      font-family: "Times New Roman", Times, serif;
      font-size: 12pt;
      color: #000;
      background: #fff;
      max-width: 210mm;
      margin: 0 auto;
      padding: 20mm 18mm 28mm;
    }}

    h1 {{
      font-size: 15pt;
      font-weight: bold;
      text-align: center;
      border-bottom: 3px solid #000;
      padding-bottom: 10px;
      margin-bottom: 16px;
    }}

    h2 {{
      font-size: 12pt;
      font-weight: bold;
      border: 1.5px solid #000;
      border-left: 5px solid #000;
      padding: 5px 10px;
      margin: 24px 0 12px;
    }}

    h3 {{
      font-size: 11pt;
      font-weight: bold;
      margin: 16px 0 6px;
    }}

    p {{
      line-height: 1.6;
      margin-bottom: 10px;
    }}

    ul, ol {{
      padding-left: 22px;
      margin-bottom: 10px;
      line-height: 1.6;
    }}

    li {{ margin-bottom: 4px; }}

    /* Answer lines for MCQ options */
    li p {{ margin-bottom: 2px; }}

    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0;
      font-size: 11pt;
    }}

    th, td {{
      border: 1px solid #000;
      padding: 5px 10px;
      text-align: left;
    }}

    th {{ font-weight: bold; background: #f0f0f0; }}

    blockquote {{
      border-left: 4px solid #888;
      padding: 6px 14px;
      margin: 10px 0;
      color: #333;
      font-style: italic;
    }}

    code {{
      font-family: "Courier New", monospace;
      font-size: 10.5pt;
      background: #f5f5f5;
      padding: 1px 4px;
      border-radius: 2px;
    }}

    pre {{
      font-family: "Courier New", monospace;
      font-size: 10pt;
      background: #f5f5f5;
      border: 1px solid #ccc;
      padding: 10px 14px;
      margin: 10px 0;
      white-space: pre-wrap;
    }}

    hr {{
      border: none;
      border-top: 1px solid #ccc;
      margin: 20px 0;
    }}

    strong {{ font-weight: bold; }}
    em {{ font-style: italic; }}

    @media print {{
      body {{ padding: 0; }}
      @page {{ margin: 20mm 18mm 28mm; size: A4; }}
    }}
  </style>
</head>
<body>
{body}
</body>
</html>
"""


def extract_title(md_text: str) -> str:
    """Pull the first H1 heading as the page title, falling back to a generic title."""
    match = re.search(r'^#\s+(.+)', md_text, re.MULTILINE)
    return match.group(1).strip() if match else "Practice Paper"


def convert(md_path: Path) -> Path:
    md_text = md_path.read_text(encoding="utf-8")

    title = extract_title(md_text)

    md = markdown.Markdown(extensions=["tables", "fenced_code", "nl2br"])
    body_html = md.convert(md_text)

    html = HTML_TEMPLATE.format(title=title, body=body_html)

    out_path = DUMP_DIR / md_path.with_suffix(".html").name
    out_path.write_text(html, encoding="utf-8")
    return out_path


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 md_to_html.py <file.md> [file2.md ...]")
        sys.exit(1)

    DUMP_DIR.mkdir(parents=True, exist_ok=True)

    for arg in sys.argv[1:]:
        md_path = Path(arg).resolve()
        if not md_path.exists():
            print(f"Not found: {md_path}", file=sys.stderr)
            continue
        if md_path.suffix.lower() != ".md":
            print(f"Skipping (not .md): {md_path}", file=sys.stderr)
            continue
        out = convert(md_path)
        print(f"{md_path.name}  →  {out}")


if __name__ == "__main__":
    main()
