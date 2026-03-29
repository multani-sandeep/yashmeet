#!/usr/bin/env python3
"""
Bulk image to Markdown converter using a local Ollama vision model.

Extracts text from images in dump/ and saves .md files alongside them.
Optionally archives the source image after conversion.

Usage:
    python3 img_to_md.py            # convert only
    python3 img_to_md.py --archive  # convert + move image to archive/

Requires (one-time setup):
    brew install ollama
    ollama pull llava
    pip install ollama
"""

import sys
import shutil
from pathlib import Path
from datetime import datetime

import ollama

DUMP_DIR = Path(__file__).parent.parent / "year9" / "dump"
ARCHIVE_DIR = Path(__file__).parent.parent / "year9" / "archive"

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
MODEL = "llava"

EXTRACT_PROMPT = (
    "Extract all text from this image exactly as written. "
    "Preserve headings, lists, and structure using Markdown formatting. "
    "For diagrams or figures that cannot be transcribed as text, write a brief description "
    "in square brackets like [Diagram: description]. "
    "Output only the extracted content with no preamble."
)


def image_to_md(image_path: Path) -> str:
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": EXTRACT_PROMPT,
                "images": [str(image_path)],
            }
        ],
    )
    return response.message.content


def main():
    archive = "--archive" in sys.argv

    images = sorted(
        p for p in DUMP_DIR.iterdir() if p.suffix.lower() in IMAGE_EXTENSIONS
    )
    if not images:
        print("No images found in dump/")
        return

    print(f"Found {len(images)} image(s) in dump/\n")

    for img_path in images:
        print(f"  {img_path.name}", end=" ... ", flush=True)
        try:
            body = image_to_md(img_path)
            header = (
                f"# {img_path.stem}\n\n"
                f"_Extracted from `{img_path.name}` on "
                f"{datetime.now().strftime('%Y-%m-%d')}_\n\n---\n\n"
            )
            md_path = DUMP_DIR / img_path.with_suffix(".md").name
            md_path.write_text(header + body, encoding="utf-8")
            print(f"saved {md_path.name}", end="")

            if archive:
                ARCHIVE_DIR.mkdir(exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                dest = ARCHIVE_DIR / f"{img_path.stem}_{timestamp}{img_path.suffix}"
                shutil.move(str(img_path), dest)
                print(f"  (archived -> archive/{dest.name})", end="")

            print()

        except Exception as e:
            print(f"FAILED: {e}")

    print("\nDone.")


if __name__ == "__main__":
    main()
