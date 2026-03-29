import os
import shutil
from datetime import datetime
from pathlib import Path
import subprocess

# Set project paths relative to this script
PROJECT_ROOT = Path(__file__).parent.parent
YEAR9_ROOT = PROJECT_ROOT / "year9"
DUMP_DIR = YEAR9_ROOT / "dump"
ARCHIVE_DIR = YEAR9_ROOT / "archive"
PAST_PAPERS_DIR = YEAR9_ROOT / "past-papers"
IMAGES_DIR = YEAR9_ROOT / "images"

# Ensure directories exist
ARCHIVE_DIR.mkdir(exist_ok=True)
PAST_PAPERS_DIR.mkdir(exist_ok=True)
IMAGES_DIR.mkdir(exist_ok=True)

try:
    import mammoth
    MAMMOTH_AVAILABLE = True
except ImportError:
    MAMMOTH_AVAILABLE = False
    print("WARNING: mammoth not found. Falling back to textutil (no images).")

def process_docx(docx_path: Path):
    stem = docx_path.stem
    print(f"Processing {docx_path.name} ...")
    
    # Identify subject (simple guess, can be improved)
    subject = "unknown"
    subjects = ["history", "chemistry", "physics", "geography", "maths", "biology", "english", "spanish"]
    for s in subjects:
        if s in stem.lower():
            subject = s
            break
            
    # Define output folder for images
    file_images_dir = IMAGES_DIR / subject
    file_images_dir.mkdir(exist_ok=True)

    def convert_image(image):
        nonlocal image_counter
        image_counter += 1
        with image.open() as image_bytes:
            ext = image.content_type.split("/")[-1]
            if ext == "jpeg": ext = "jpg"
            img_name = f"{stem.lower().replace(' ', '_')}_{image_counter}.{ext}"
            img_path = file_images_dir / img_name
            with open(img_path, "wb") as f:
                f.write(image_bytes.read())
            return {"src": f"images/{subject}/{img_name}"}

    image_counter = 0
    
    if MAMMOTH_AVAILABLE:
        with open(docx_path, "rb") as docx_file:
            result = mammoth.convert_to_markdown(docx_file, convert_image=mammoth.images.img_element(convert_image))
            md_content = result.value
            messages = result.messages
            for msg in messages:
                print(f"  Mammoth: {msg}")
    else:
        # Fallback to textutil if mammoth is missing
        txt_path = docx_path.with_suffix(".txt")
        subprocess.run(["textutil", "-convert", "txt", str(docx_path)], check=True)
        with open(txt_path, "r") as f:
            md_content = f.read()
        os.remove(txt_path)

    # Clean up name for output file
    is_ms = "ANSWERS" in stem.upper() or "MARK" in stem.upper()
    clean_name = stem.replace("ANSWERS", "").replace("MARK", "").strip().replace(" ", "_")
    if is_ms:
        clean_name += "_markscheme"

    # Decide where to put MD
    is_paper = "EOY" in stem.upper() or "PAPER" in stem.upper() or "REVISION" in stem.upper()
    
    if is_paper and subject != "unknown":
        target_dir = PAST_PAPERS_DIR / subject
        target_dir.mkdir(exist_ok=True)
        md_file = target_dir / f"{clean_name}.md"
        with open(md_file, "w") as f:
            f.write(f"# {stem}\n\n{md_content}")
        print(f"  Saved as paper: {md_file.relative_to(YEAR9_ROOT)}")
    else:
        # Save as a general subject note if subject known, or just a new file in dump
        if subject != "unknown":
            subject_file = YEAR9_ROOT / f"{subject}.md"
            with open(subject_file, "a") as f:
                f.write(f"\n\n---\n# Notes from {stem} ({datetime.now().strftime('%Y-%m-%d')})\n\n{md_content}\n")
            print(f"  Appended to notes: {subject_file.relative_to(YEAR9_ROOT)}")
        else:
            md_file = docx_path.with_suffix(".md")
            with open(md_file, "w") as f:
                f.write(f"# {stem}\n\n{md_content}")
            print(f"  Processed as raw MD: {md_file.relative_to(YEAR9_ROOT)}")

    # Move docx to archive
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_path = ARCHIVE_DIR / f"{stem}_{timestamp}.docx"
    shutil.move(str(docx_path), str(archive_path))
    print(f"  Archived to: {archive_path.name}")

def main():
    # Find all docx in the dump folder
    docx_files = list(DUMP_DIR.glob("**/*.docx"))
    
    if not docx_files:
        print(f"No .docx files found in {DUMP_DIR}")
        return

    for docx in docx_files:
        try:
            process_docx(docx)
        except Exception as e:
            print(f"ERROR processing {docx}: {e}")

    print(f"\nDone. Processed {len(docx_files)} files.")

if __name__ == "__main__":
    main()
