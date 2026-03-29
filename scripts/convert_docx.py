#!/usr/bin/env python3
"""Convert DOCX files to Markdown with image extraction."""

import os
import sys
import zipfile
import re
from pathlib import Path

# Mammoth is now installed in the environment
import mammoth

def extract_images(docx_path, output_dir):
    """Extract images from DOCX file."""
    images = []
    base_name = Path(docx_path).stem.replace(' ', '_').lower()

    with zipfile.ZipFile(docx_path, 'r') as zip_ref:
        for file_info in zip_ref.filelist:
            if file_info.filename.startswith('word/media/'):
                ext = os.path.splitext(file_info.filename)[1]
                img_name = f"{base_name}_{len(images)+1}{ext}"
                img_path = os.path.join(output_dir, img_name)

                with zip_ref.open(file_info.filename) as src:
                    with open(img_path, 'wb') as dst:
                        dst.write(src.read())

                images.append({
                    'original': file_info.filename,
                    'saved_as': img_name,
                    'path': img_path
                })

    return images

def convert_docx_to_md(docx_path, output_md_path, images_dir):
    """Convert DOCX to Markdown."""
    # Extract images first
    images = extract_images(docx_path, images_dir)

    # Counter for image replacement
    img_counter = [0]
    base_name = Path(docx_path).stem.replace(' ', '_').lower()

    def convert_image(image):
        img_counter[0] += 1
        ext = image.content_type.split('/')[-1]
        if ext == 'jpeg':
            ext = 'jpg'
        img_name = f"{base_name}_{img_counter[0]}.{ext}"
        return {"src": f"images/{img_name}"}

    # Convert to HTML first, then clean up to markdown
    with open(docx_path, 'rb') as docx_file:
        result = mammoth.convert_to_html(docx_file, convert_image=mammoth.images.img_element(convert_image))
        html = result.value
        messages = result.messages

    # Convert HTML to Markdown-like format
    md_content = html_to_markdown(html)

    # Add header
    doc_name = Path(docx_path).stem
    header = f"# {doc_name}\n\n"

    # Write markdown file
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(header + md_content)

    return images, messages

def html_to_markdown(html):
    """Convert HTML to Markdown."""
    md = html

    # Headers
    md = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n', md, flags=re.DOTALL)
    md = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n', md, flags=re.DOTALL)
    md = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', md, flags=re.DOTALL)

    # Bold and italic
    md = re.sub(r'<strong>(.*?)</strong>', r'**\1**', md, flags=re.DOTALL)
    md = re.sub(r'<b>(.*?)</b>', r'**\1**', md, flags=re.DOTALL)
    md = re.sub(r'<em>(.*?)</em>', r'*\1*', md, flags=re.DOTALL)
    md = re.sub(r'<i>(.*?)</i>', r'*\1*', md, flags=re.DOTALL)

    # Images
    md = re.sub(r'<img[^>]*src="([^"]*)"[^>]*/?>', r'![](\1)\n', md)

    # Lists
    md = re.sub(r'<ul[^>]*>', '', md)
    md = re.sub(r'</ul>', '\n', md)
    md = re.sub(r'<ol[^>]*>', '', md)
    md = re.sub(r'</ol>', '\n', md)
    md = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', md, flags=re.DOTALL)

    # Paragraphs and line breaks
    md = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', md, flags=re.DOTALL)
    md = re.sub(r'<br\s*/?>', '\n', md)

    # Tables (basic conversion)
    md = re.sub(r'<table[^>]*>', '\n', md)
    md = re.sub(r'</table>', '\n', md)
    md = re.sub(r'<tr[^>]*>', '| ', md)
    md = re.sub(r'</tr>', ' |\n', md)
    md = re.sub(r'<t[dh][^>]*>(.*?)</t[dh]>', r'\1 | ', md, flags=re.DOTALL)

    # Remove remaining HTML tags
    md = re.sub(r'<[^>]+>', '', md)

    # Clean up whitespace
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = md.strip()

    return md

def main():
    if len(sys.argv) < 3:
        print("Usage: python convert_docx.py <docx_path> <output_md_path>")
        sys.exit(1)

    docx_path = sys.argv[1]
    output_md_path = sys.argv[2]
    images_dir = sys.argv[3] if len(sys.argv) > 3 else str(Path(__file__).parent.parent / "year9/past-papers/maths/images")

    os.makedirs(images_dir, exist_ok=True)

    images, messages = convert_docx_to_md(docx_path, output_md_path, images_dir)

    print(f"Converted: {docx_path}")
    print(f"Output: {output_md_path}")
    print(f"Images extracted: {len(images)}")
    for img in images:
        print(f"  - {img['saved_as']}")

    if messages:
        print("Messages:")
        for msg in messages:
            print(f"  - {msg}")

if __name__ == "__main__":
    main()
