# Year 9 Study Notes Repository

## Purpose
This repository is designed to organize and process study materials for Year 9 subjects. It handles various input formats including images, text files, and PDFs, processing them into structured notes. Each subject has notes grouped into topics. Notes are always created in MD format. 

Always keep notes concise and to the point. Do not expand sections unless asked by user.

Notes are always based on GCSE Year 9 curriculum in the UK

## Generating new Papers
When creating new papers:
- Always follow the format and structure from the `past-papers' provided
- Ask whether all syllabus is to be considered or just the test topics
- Ask difficult level (easy, medium, hard)
- Create a mark scheme for the generated paper
- In terms of syllabus and difficulty use IGCSE standard for Year 9 at a UK independent school, specifically Haberdashers Boys school
- Papers are generated in the `dump` folder
- Use internet resources to create a paper that is relevant to the syllabus and difficulty level

- If a paper requires information like the periodic table and the table would have been provided in an IGCSE exam then include that in the paper. Do similar for diagrams or other reference material necessary to complete the paper.

- See subject level split below for creating paper with the correct ratio of question type mcqs or subjective.

## Usage

Here are some sample prompts you can use to manage this repository:

1. **Process specific notes**:
   "Please read `notes.jpg` from the `/dump` folder, extract the text, and add the summarized content to `history.md`."

2. **Process all pending materials**:
   "Check the `/dump` folder for any new files. For each file, process the content into the relevant subject's markdown file in the root directory, and then move the source file to `/archive` with a timestamp. From the file identify whether it is a past paper, if it is, then create a folder with the name of the subject under `past-papers` directory and move the file to that folder. If the file is a mark scheme, then name the markscheme file matching the past paper with the same name as past paper with a suffix '_markscheme'."

3. **Organize and review**:
   "Review the recent additions in `history.md` for clarity and formatting. Also, check if there are any stray files in `/dump` that haven't been processed yet."

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
- `history.md`: History subject notes
- `chemistry.md`: Chemistry subject notes
   - exams typically have a 50:50 split between mcqs:subjective questions
- `physics.md`: Physics subject notes
- `geography.md`: Geography subject notes
- `maths.md`: Maths subject notes
- `biology.md`: Biology subject notes
   - exams typically have a 80:20 split between mcqs:subjective questions.
- `english.md`: English subject notes
- `CLAUDE.md`: This documentation file

## Workflow

1. **Input**: Place study materials (images, PDFs, text files) in `/dump`
2. **Process**: Materials are processed and converted into structured notes. Donot expand sections unless asked by user.
3. **Output**: Notes are added to subject-specific `.md` files in the root directory
4. **Archive**: Processed source files are moved to `/archive` with timestamps

## Notes
- Keep the `/dump` folder clean by regularly processing files
- Archive maintains all historical processed files for reference
- Use clear, descriptive filenames when adding materials to `/dump`
