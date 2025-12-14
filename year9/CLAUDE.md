# Year 9 Study Notes Repository

## Purpose
This repository is designed to organize and process study materials for Year 9 subjects. It handles various input formats including images, text files, and PDFs, processing them into structured notes.

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
- `CLAUDE.md`: This documentation file

## Workflow

1. **Input**: Place study materials (images, PDFs, text files) in `/dump`
2. **Process**: Materials are processed and converted into structured notes
3. **Output**: Notes are added to subject-specific `.md` files in the root directory
4. **Archive**: Processed source files are moved to `/archive` with timestamps

## Notes
- Keep the `/dump` folder clean by regularly processing files
- Archive maintains all historical processed files for reference
- Use clear, descriptive filenames when adding materials to `/dump`
