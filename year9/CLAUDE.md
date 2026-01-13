# Year 9 Study Notes Repository

## Purpose
This repository is designed to organize and process study materials for Year 9 subjects. It handles various input formats including images, text files, and PDFs, processing them into structured notes.

## Usage

Here are some sample prompts you can use to manage this repository:

1. **Process specific notes**:
   "Please read `notes.jpg` from the `/dump` folder, extract the text, and add the summarized content to `history.md`."

2. **Process all pending materials**:
   "Check the `/dump` folder for any new files. For each file, process the content into the relevant subject's markdown file in the root directory, and then move the source file to `/archive` with a timestamp."

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
