#!/usr/bin/env python3
"""
Bulk PDF to Markdown converter.

Converts all PDFs in the dump/ folder to .md files (saved alongside the PDF).
Optionally archives the source PDF after conversion.

Usage:
    python3 pdf_to_md.py            # convert only
    python3 pdf_to_md.py --archive  # convert + move PDF to archive/
"""

import sys
import shutil
from pathlib import Path
from datetime import datetime

DUMP_DIR = Path(__file__).parent / "dump"
ARCHIVE_DIR = Path(__file__).parent / "archive"


def convert_with_pymupdf(pdf_path: Path) -> str:
    import fitz  # PyMuPDF
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc, 1):
        try:
            # PyMuPDF 1.24+ supports native markdown extraction
            text = page.get_text("markdown")
        except Exception:
            text = page.get_text()
        if text.strip():
            pages.append(f"<!-- Page {i} -->\n\n{text.strip()}")
    return "\n\n---\n\n".join(pages)


def convert_with_pypdf(pdf_path: Path) -> str:
    from pypdf import PdfReader
    reader = PdfReader(pdf_path)
    pages = []
    for i, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        if text.strip():
            pages.append(f"<!-- Page {i} -->\n\n{text.strip()}")
    return "\n\n---\n\n".join(pages)


def convert_pdf(pdf_path: Path) -> str:
    try:
        import fitz  # noqa: F401
        return convert_with_pymupdf(pdf_path)
    except ImportError:
        return convert_with_pypdf(pdf_path)


def main():
    archive = "--archive" in sys.argv

    pdfs = sorted(DUMP_DIR.glob("*.pdf"))
    if not pdfs:
        print("No PDFs found in dump/")
        return

    print(f"Found {len(pdfs)} PDF(s) in dump/\n")

    for pdf_path in pdfs:
        print(f"  {pdf_path.name}", end=" ... ", flush=True)
        try:
            body = convert_pdf(pdf_path)
            header = (
                f"# {pdf_path.stem}\n\n"
                f"_Converted from `{pdf_path.name}` on "
                f"{datetime.now().strftime('%Y-%m-%d')}_\n\n---\n\n"
            )
            md_path = DUMP_DIR / pdf_path.with_suffix(".md").name
            md_path.write_text(header + body, encoding="utf-8")
            print(f"saved {md_path.name}", end="")

            if archive:
                ARCHIVE_DIR.mkdir(exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                dest = ARCHIVE_DIR / f"{pdf_path.stem}_{timestamp}.pdf"
                shutil.move(str(pdf_path), dest)
                print(f"  (archived -> archive/{dest.name})", end="")

            print()

        except Exception as e:
            print(f"FAILED: {e}")

    print("\nDone.")


if __name__ == "__main__":
    main()
