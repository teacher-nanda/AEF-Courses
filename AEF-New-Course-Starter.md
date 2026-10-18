# Starter for a NEW course conversation (paste the block below as your first message)

---

I'm Nanda, an English teacher. Lessons are strictly one-on-one ("Conversational English with teacher Nanda"). I build interactive HTML lessons for a course from its book, one lesson at a time. My folder `AEF-Courses` is connected. Before building anything:

1. Read `AEF Lesson Standards.md` in that folder (never edit it without asking me) and use `AEF2-1B/index.html` as the style/quality reference.
2. Ask me which course/book, level, unit and lesson, and what theme I want (each lesson gets its own creative visual theme).
3. Follow every rule below.

## Standing rules (learned while building AEF2-1A and 1B)

**Setting and language**
- One-on-one only: never write pair, partner, classmate, "Student A/B" or class-vote wording. Use "you / me / teacher". (Romantic "partner" content from the book is fine.)
- American spelling. No on-screen book references (I don't use the books in class): every book item must be on screen. Audio and images are placeholders until I supply files; never invent filenames.
- CELTA-style flow: meaning/CCQs, form, pronunciation, controlled practice, freer practice. Homework is workbook-exact and limited to language taught.
- Text size: 1.25x (`.content{zoom:1.25}`).

**Exercises**
- Numbered exercises go in two columns whenever possible, numbered top to bottom then left to right (left column = ceil(n/2)). Homework slides too.
- The worked example is item 1 inside the left column, same layout as the other items, answer filled and highlighted green. No "Example" label, no "(example)". Badge `1` if the book numbers the example 1; a green ✓ if the student's items start at 1. For word order / rewrite items, show the answer on its own line below the prompt.
- Never write the answers or hints into instructions. If a task is "find the correct ones", say how many exist in total so it doesn't read as "find three".
- Matching exercises: reduce font/box sizes so everything (and the Check button) is visible without scrolling. Prefer typing the letter/number into a blank over drag-and-match when it is just matching numbers to situations.
- Check Answers: one button per exercise covers all parts. Leave generous space between the Check button, banners and the audio player.
- Audio: players go after Check Answers, at the end of the slide, for the student to check their answers (pre-listening warm-up audio goes at the top). Wire audio files from the lesson folder (`AEF3e_Level_2_SB_1.x.mp3`, `..._WB_1.x.mp3`) into the `AUDIO` map.

**Slide design**
- Keep emojis as sound/picture icons; don't add "replace with book image" notes for them.
- Don't ask students questions in cards that let them just read the answer; leave room for them to try ("The app asks about my free time: pets, activities, movies...").
- Lead-ins should be interactive and creative (e.g. "Build the dad" drawing game); remove boring quote/discussion slides.
- Student-led activities: the student does the thinking; don't give help or answers on screen.
- Instructions are short and clear.

**Delivery**
- Edit existing files in place (no `_copy` files); backups are fine only as an extra.
- After every change: rebuild, run the answer-check sweep, then save to my folder.
- Update the course homepage `index.html` card order (1A before 1B) and remove the `draft` tag when I say a lesson is ready.
- "Save Notes" PDF: purple banner with lesson name, then "How to use this PDF": 1) Read your notes below... 2) Click the green button to open the lesson... (single green button).

---

## Tools (saved in your folder as `AEF-build-tools.tar.gz`)
Python build scripts (one `build.py` per lesson, shared `balance.py`) and Playwright checks. Ask Claude to unpack it and start the new course from `a1b`.
