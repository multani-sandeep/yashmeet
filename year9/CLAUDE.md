# Year 9 Study Notes Repository

## Purpose
This repository is designed to organize and process study materials for Year 9 subjects. It handles various input formats including images, text files, and PDFs, processing them into structured notes. Each subject has notes grouped into topics. Notes are always created in MD format. 

Always keep notes concise and to the point. Do not expand sections unless asked by user.

Notes are always based on iGCSE Year 9 curriculum in the UK

## Generating new Papers
When creating new papers:
- Always follow the format and structure from the `past-papers' provided
- Ask whether all syllabus is to be considered or just the test topics
- Ask difficult level (easy, medium, hard)
- Create a mark scheme for the generated paper
- In terms of syllabus and difficulty use IGCSE standard for Year 9 at a UK independent school, specifically Haberdashers Boys school
- Papers are generated in the `dump` folder
- Subject specific past paper questions can be reused in papers, but should not exceed 20% of the paper
- Use internet resources to create a paper that is relevant to the syllabus and difficulty level

- If a paper requires information like the periodic table and the table would have been provided in an IGCSE exam then include that in the paper. Do similar for diagrams or other reference material necessary to complete the paper.

- See subject level split below in `Root Files` for creating paper with the correct ratio of question type mcqs or subjective.

- Estimate an A4 size content based on lines per question and options. Assume a wide margin at the bottom of each page.

## Usage

Here are some sample prompts you can use to manage this repository:

1. **Classify material**
   Based on the content and filename identify the subject and topic of the material. If the material is a past paper, then create a folder with the name of the subject under `past-papers` directory and move the file to that folder. If the file is a mark scheme, then name the markscheme file matching the past paper with the same name as past paper with a suffix '_markscheme'. If its an assignment, then extract the IGCSE objectives of the assignment and add it to subject notes. Some assignments are also assessments, in which case it has a question paper and a mark scheme. In that case extract the IGCSE subject areas from the assignment and update the notes for the subject highlighting the IGCSE topics covered in the assignment/assessment.

2. **Process specific notes**:
   "Please read `notes.jpg` from the `/dump` folder, extract the text, and add the summarized content to `history.md`."

3. **Process all pending materials**:
   "Check the `/dump` folder for any new files. For each file, process the content into the relevant subject's markdown file in the root directory, and then move the source file to `/archive` with a timestamp. From the file identify whether it is a past paper, if it is, then create a folder with the name of the subject under `past-papers` directory and move the file to that folder. If the file is a mark scheme, then name the markscheme file matching the past paper with the same name as past paper with a suffix '_markscheme'."

4. **Organize and review**:
   "Review the recent additions in `history.md` for clarity and formatting. Also, check if there are any stray files in `/dump` that haven't been processed yet."

## Curriculum Processing Plan

To process the curriculum from a dump (e.g., `Y9 Curriculum Booklet 25-26.pdf`):

1. **Extraction**: Use `python3 scripts/pdf_to_md.py` to convert the curriculum PDF into a temporary Markdown file.
2. **Analysis**: Read the converted Markdown to identify pages and sections corresponding to each subject.
3. **Distribution**:
   - For each subject (Biology, Chemistry, Physics, History, Geography, Maths, English), identify:
     - Term-by-term objectives
     - Key topics and assessment types
     - iGCSE curriculum links
   - Append or update the curriculum information at the top of the relevant subject's `.md` file (e.g., `biology.md`). Use a "Curriculum Overview" header.
4. **Formatting**: Ensure all curriculum notes follow these rules:
   - Use bullet points for clear readability.
   - Categorize by 'Term 1', 'Term 2', and 'Term 3' where applicable.
   - Group related topics logically for easier revision planning.
5. **Completion**:
   - Archive the source PDF to `year9/archive/` using the script's `--archive` flag.
   - Delete the temporary Markdown file created during extraction.

## Folder Structure

### `/dump`
**Purpose**: Input processing directory
- Place raw study materials here for processing
- Supported formats:
  - Images (screenshots, photos of notes, diagrams)
  - Text files (.txt, .md)
  - PDFs (textbooks, worksheets, documents)
- Files in this folder are awaiting processing

### `/archive`
**Purpose**: Processed files storage
- Processed files are moved here after completion
- Maintains a historical record of all processed materials
- Files are typically renamed with timestamps for organization

### Root Directory
**Purpose**: Subject notes storage
- Subject-specific notes are stored as `.md` files in the root directory
- Example: `history.md` contains History subject notes
- Each subject gets its own markdown file for organized note-taking

### Root Files
- `biology.md`: Biology subject notes (exams: 80:20 mcqs:subjective)
- `chemistry.md`: Chemistry subject notes (exams: 50:50 mcqs:subjective)
- `computer-science.md`: Computer Science subject notes
- `design-technology.md`: Design & Technology subject notes
- `english.md`: English subject notes
- `french.md`: French subject notes
- `geography.md`: Geography subject notes
- `history.md`: History subject notes
- `maths.md`: Maths subject notes
- `music.md`: Music subject notes
- `physics.md`: Physics subject notes
- `spanish.md`: Spanish subject notes
- `theology-and-philosophy.md`: Theology and Philosophy subject notes
- `CLAUDE.md`: This documentation file

## Workflow

1. **Input**: Place study materials (images, PDFs, text files) in `/dump`
2. **Process**: Materials are processed and converted into structured notes. Do not expand sections unless asked by user.
   - For **DOCX files with images**, use `scripts/convert_docx.py` to preserve images and formatting.
   - Extract images to `year9/images/<subject>/` and update markdown links.
3. **Output**: Notes are added to subject-specific `.md` files in the root directory
4. **Archive**: Processed source files are moved to `/archive` with timestamps

### DOCX Processing Protocol
To process a complex DOCX file (like multiple subject notes or papers):
1. **Convert**: Run `python3 scripts/convert_docx.py "year9/dump/filename.docx" /tmp/output.md /tmp/images`.
2. **Inspect**: Read `/tmp/output.md` to identify subject(s) and content type.
3. **Distribute**: 
   - Move images to `year9/images/<subject>/`.
   - Update image links in the markdown to point to the new location.
   - Append or create subject notes in the root directory (e.g., `spanish.md`).
4. **Finalize**: Move the original DOCX to `year9/archive/` with a timestamp.

Note: Requires `mammoth` library (`pip install mammoth`).

## Notes
- Keep the `/dump` folder clean by regularly processing files
- Archive maintains all historical processed files for reference
- Use clear, descriptive filenames when adding materials to `/dump`
