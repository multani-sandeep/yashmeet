# Year 9 Study Repository

Study materials for Year 9 iGCSE subjects at Haberdashers Boys School (UK).

## Agents

Two sub-agents handle all work in this repo. Invoke them with `@`:

| Agent | When to use |
|-------|------------|
| `@note-taker` | Processing dump files, extracting notes, classifying past papers, archiving materials |
| `@paper-generator` | Creating practice papers and mark schemes |
| `@quiz-gen` | Creating interactive HTML flashcard quizzes for specific topics; asks difficulty (default Hard) |

## Folder Structure

| Folder | Purpose |
|--------|---------|
| `year9/dump/` | Drop zone — place new files here for processing; generated papers also land here |
| `year9/archive/` | Processed source files (timestamped) |
| `year9/past-papers/<subject>/` | Past papers and mark schemes per subject |
| `year9/images/<subject>/` | Images extracted from DOCX files |
| Root `year9/*.md` | Subject notes files |

## Subject Notes Files

- `year9/biology.md` — Biology (80:20 MCQ:subjective)
- `year9/chemistry.md` — Chemistry (50:50 MCQ:subjective)
- `year9/computer-science.md` — Computer Science
- `year9/design-technology.md` — Design & Technology
- `year9/english.md` — English
- `year9/french.md` — French
- `year9/geography.md` — Geography
- `year9/history.md` — History
- `year9/maths.md` — Maths
- `year9/music.md` — Music
- `year9/physics.md` — Physics
- `year9/spanish.md` — Spanish
- `year9/theology-and-philosophy.md` — Theology & Philosophy

## Quick-start Prompts

```
# Process everything in dump
@note-taker Process all pending files in year9/dump/

# Add specific notes
@note-taker Read notes.jpg from dump and add content to history.md

# Generate a paper
@paper-generator Generate a Chemistry practice paper

# Classify a new file
@note-taker Classify and process year9/dump/<filename>

# Generate a quiz
@quiz-gen Create a Hard Biology quiz on cell division and mitosis
@quiz-gen Quiz me on Geography plate tectonics — Medium difficulty
```
