import os
import glob
import subprocess
import shutil
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
dump_dir = PROJECT_ROOT / "year9" / "dump" / "drive-download-20260302T201420Z-3-001"
archive_dir = PROJECT_ROOT / "year9" / "archive"
past_papers_dir = PROJECT_ROOT / "year9" / "past-papers" / "maths"

past_papers_dir.mkdir(parents=True, exist_ok=True)
archive_dir.mkdir(exist_ok=True)

docx_files = list(dump_dir.glob("*.docx"))

for docx in docx_files:
    # use textutil to convert to txt
    subprocess.run(["textutil", "-convert", "txt", str(docx)], check=True)
    
    txt_file = docx.with_suffix(".txt")
    
    stem = docx.stem
    # determine if it's markscheme/answers
    is_ms = "ANSWERS" in stem.upper()
    
    # clean up the name
    clean_name = stem.replace("ANSWERS", "").strip().replace(" ", "_")
    if is_ms:
        clean_name += "_markscheme"
        
    md_file = past_papers_dir / f"{clean_name}.md"
    
    # move the txt to the md location and wrap in markdown format
    with open(txt_file, "r") as f:
        content = f.read()
    
    with open(md_file, "w") as f:
        f.write(f"# {stem}\n\n")
        f.write(content)
        
    os.remove(txt_file)
    
    # Move docx to archive
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_path = archive_dir / f"{stem}_{timestamp}.docx"
    shutil.move(str(docx), str(archive_path))

print(f"Processed {len(docx_files)} files.")
