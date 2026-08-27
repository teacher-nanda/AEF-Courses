# 🎓 AEF Interactive Lesson Standards

This document summarises all standards established across AEF3 1B, AEF3 2A, AEF4 1A, AEF4 2A, AEF4 3A, AEF4 3B, and AEF4 7A.
Share it at the start of any new conversation so Claude can match the existing lessons exactly.

> **This is the single, consolidated master file** (last folded together 2026-07-20). It supersedes and fully incorporates every previously separate patch-notes file — "Minimum Font Size Rule," "Notes System Correction," "Wordbank Presentation Rule," and "Uniform Answer Blank Width Rule" (all previously living in `AEF4-3B/`) — which are now merged in below and have been retired/deleted. **Only this one file, saved at the root of the `AEF-Courses` folder, is ever used or edited going forward.** No other standards file should be created, referenced, or trusted — if a new correction needs to become a standing rule, it gets added directly to this file, and only after the teacher has reviewed and approved the exact wording first.

---

## ✅ Pre-Edit Checklist — Run This Before Touching ANY Book-Content Slide

> Added 2026-08-25 after repeated book-accuracy and standards-compliance mistakes on AEF4-1B. This checklist is not optional and is not a one-time read — run it fresh every time, for every slide, even ones already built. Never build or fix a slide from memory of the book or memory of this file.

1. **Open the actual book page render for this exercise first** — every time, even if it was already viewed earlier in the same session. Never reconstruct exercise content from memory, from a similar exercise in another unit, or from what "sounds right."
2. **Follow the book's exercises step by step, in the exact order they appear on the page** (a, b, c, d… / 1, 2, 3…). Don't skip a step, merge two steps into one slide, reorder them, or add a step the book doesn't have — unless the teacher explicitly asks for a deviation.
3. **Copy the book's wording, sentences, and sequence exactly.** The only allowed changes are the ones already documented elsewhere in this file — e.g. adapting "compare with a partner" / "discuss with a partner" to one-on-one phrasing ("tell me," "share your thoughts with me"), or changing the interaction mechanic to fit an on-screen click/type format. Never paraphrase or invent book content.
4. **Never mention the source on screen** — no "book," "Student Book," "Workbook," "SB," "WB," "TB," page numbers, or exercise letters/numbers anywhere the student can see. These are internal references for building the slide only.
5. **Never show a raw number on screen that comes from the book's own internal referencing** — this covers audio track numbers (e.g. "1.17") as well as exercise/page numbers. This extends the existing Audio Standards rule ("no 'Track 2.8'") to all book-internal numbering, not audio alone.
6. **Never invent anything that's missing** — a filename, an answer-key value, a piece of content the available book scans don't show. Ask the teacher instead of guessing or filling the gap with something plausible.
7. **After building, re-open the same book page again and check the finished slide against it line by line** — don't rely on the read from step 1 still being accurate in memory by the time the slide is done.
8. **Then, separately, check the relevant sections of the rest of this standards file** (exercise type, banner, audio, example numbering, blank widths, etc.) against what was just built — book-accuracy and standards-compliance are two separate checks, not one.
9. **Two specific, repeated mistakes to actively check for on every single numbered exercise, every time, with no exceptions — including every Homework slide:**
   - **The green "example" badge is only for an item the book itself shows as already worked/answered.** If the book's exercise starts straight at item 1 with no example, item 1 is a real question — `circ-num`, not `example-badge`. Never default to marking item 1 as the example just because it's first; check the actual book page for that specific exercise every time, per item 1-3 above.
   - **Column order must be top-to-bottom then left-to-right, never row-major/interleaved.** With `n` items in 2 columns, items 1…⌈n/2⌉ go in the left column (stacked top to bottom) and the rest in the right column — e.g. 4 items → 1,2 left / 3,4 right; not 1,3 left / 2,4 right. `.fixed-two-col` / `.fixed-three-col` / `.fixed-four-col` are plain CSS grids with no auto-flow override, so placing numbered items directly as grid children produces the wrong (row-major) order — always wrap each column's items in its own child `<div>` inside the grid container so the grouping is explicit in the HTML, not left to the grid to guess.
   - Both of these must be re-checked on every slide touched, not just newly built ones — a slide edited for an unrelated reason can still be carrying one of these two mistakes from earlier.
10. **Any self-authored explanatory content — CCQs, gram-notes, gram-boxes, glossary-box definitions, "meaning" statements — must be independently fact-checked for grammatical/logical accuracy before it ships, separately from checking it against the book.** This content isn't copied from the book, so the book-accuracy checks above (steps 1-7) don't catch errors in it — a wrong CCQ answer is a real error teaching false information to a real student in a real class, not a formatting issue. Concretely:
    - Before writing a CCQ, gram-note, or meaning explanation, work out the actual correct answer yourself from first principles — don't write a plausible-sounding question and a plausible-sounding answer without independently verifying the answer is true.
    - **Check every self-authored explanation against every example already sitting in the same box**, not just the example it was written for. A rule that's true for one example in a `.gram-box` can be false for another example three lines below it (this happened: a CCQ claimed "the two halves always change in the same direction," which was true for one example in the box and false for the very next one).
    - If a box contains multiple examples of the same structure, prefer a CCQ/explanation general enough to be true for all of them, or scope it explicitly to the one example it's actually testing.
    - This applies with the same seriousness as book-accuracy — wrong grammar taught confidently is worse than a formatting inconsistency.
11. **Every `data-ans` value (every answer key) must come from an actual Teacher's Book or Workbook answer-key page you have open — never derived yourself from grammar logic, even when you're confident the derivation is correct.** This happened: an exercise's answers were worked out from the transformation pattern instead of read off the TB page, and a *different* exercise on the very same TB page turned out to have a wrong answer already shipped in the lesson ("self-centered" instead of the book's actual "self-sufficient") — a mistake that opening the TB page for an unrelated reason caught by accident. Concretely:
    - Before building any Check-Answers exercise, locate and open the actual TB/WB answer-key page for that specific exercise. If it isn't in the available renders, say so explicitly to the teacher rather than filling the gap with a self-derived answer presented as fact.
    - If only a self-derived answer is possible (the official key genuinely isn't available), the unverified flag goes in an **HTML comment** right above/inside that slide for the teacher's own eyes only (e.g. `<!-- TEACHER NOTE: these answers are derived, not read from an official key — verify if possible. -->`) — it must **never** appear as visible text on the slide itself. A visible disclaimer like "double-check against your official answer key" is a **book-reference violation** (see "No book references — ever" above) on top of being confusing/unprofessional in front of a student — the student should never see any hint that an answer might be wrong or unsourced. This happened once (HW5) and was corrected 2026-08-26 — don't repeat it.
    - Never silently ship a guessed answer with the same confidence as a verified one either — the HTML-comment flag exists so *you* (or the teacher, reading the source) know to re-check it, not so the student sees a hedge.
    - When you do open a TB/WB page for one exercise, check it for every exercise it contains, not just the one you were looking for — answer keys for unrelated exercises often share the same page and are easy to verify "for free" once the page is already open.

---

## ⏩ Forward-Only Rule — never re-touch already-approved slides

> Added 2026-08-26 at the teacher's explicit request, after a "check every slide" audit pass ended up re-opening and re-editing slides the teacher had already reviewed and considered finished.

Once a slide has been built, reviewed, and not flagged by the teacher, it is **settled** — treat it as correct and move forward. Do not re-open, re-check, or re-edit a slide that isn't the one currently being discussed, even during a broad "check everything" audit, unless:
- The teacher explicitly names that slide or exercise, or
- A change made elsewhere in the file mechanically requires it (e.g. renumbering `slideIds`/`slideLabels` after inserting a slide, or a shared function/CSS class used by that slide was just changed).

**"Check every homework slide" / "check every slide" means audit and report, not silently rewrite.** If a broad audit turns up something on an already-approved slide, surface it to the teacher and ask before touching it — don't fix it automatically just because the audit found it. This is a deliberate change from earlier in this project, where broad audits directly edited any slide with an issue; going forward, only the slide(s) the teacher is actively pointing at get edited without asking first.

The direction of work is always **forward**: new slides, the current slide being discussed, or a slide the teacher just named. Never backward into settled work on your own initiative.

---

## 🗂 General Structure

- Single-file HTML slide deck — `.slide` divs with opacity transitions, all inside `<div id="deck">`
- Main `<script>` tag comes **after all slides**, before `</div></body>`
- `slides = Array.from(document.querySelectorAll('.slide'))` runs after all slides are in the DOM
- Navigation bar order: ◀ Prev | dots | counter | Next ▶ | 💾 Save Notes | 🖨️ Print Lesson
- 📝 Notes button is fixed on screen (top right, outside the deck)
- `goTo(n)` handles navigation, dot updates, prev/next button states, notes save/load

### ⚙️ `slideIds` / `slideLabels` arrays — must stay in sync with the DOM

Every lesson also declares two parallel arrays near the top of the `<script>` block:

```js
var slideIds = ["s1","s2","s-vocab1", ... ,"hw-cover","hw-voc1", ... ];
var slideLabels = ["Cover","Lead-in","Vocabulary – ...", ... ,"Homework Cover","HW1 – ...", ... ];
```

- **Position `i` in `slideIds` must be the exact same slide as position `i` in the DOM** (`.slide` divs, in document order), and `slideLabels[i]` must describe that same slide. All three (DOM order, `slideIds`, `slideLabels`) must have identical length and stay positionally aligned.
- A startup check should always be present and left in place:
  ```js
  if (slides.length !== slideIds.length || slides.length !== slideLabels.length) {
    console.warn('Slide count mismatch:', slides.length, 'slides,', slideIds.length, 'IDs,', slideLabels.length, 'labels');
  }
  ```
- **Whenever a slide is added, removed, or split into two slides, immediately update both arrays in the same edit** — insert/remove the entry at the matching position, don't just append at the end.
- **Splitting one slide into two** (e.g. a slide had two unrelated exercises and got separated): insert the new slide's id/label into both arrays right after the original slide's entry, then renumber every subsequent HW/section title (`h2` text) and its matching `slideLabels` entry that shifted (e.g. "HW10" → "HW11", "HW11" → "HW12"...).
- **Verify after every structural change** — don't just assume it worked. Parse the file (e.g. with a quick BeautifulSoup/Python script) and confirm: DOM `.slide` id order == `slideIds` order == `slideLabels` count, no duplicate ids, and (if relevant) `<div>` open/close tag counts haven't shifted unexpectedly.

### ⚠️ JS function-naming collisions — give check/reset functions unique names

Two different slides accidentally defining functions with the **same name** (e.g. two unrelated exercises both calling their check function `checkPV()` / `resetPV()`) is a real bug that has happened and is easy to miss: JavaScript does not error on a duplicate `function foo(){}` declaration — the **last one defined in the file silently wins** and overrides the earlier one everywhere it's called, even on a completely different slide. The result: one exercise's Check/Reset buttons quietly stop working (or throw a console error) with no visible sign in the HTML.

- Always give check/reset (and any other interaction) functions a name that's unique to that specific exercise/slide — prefer a name derived from the slide id or exercise topic (e.g. `checkHwPron()`, `resetGr3()`) over a generic reusable name like `checkPV()` unless you are certain no other slide in the file already uses it.
- Before naming a new function, grep the file for that exact name first.
- If a shared interaction pattern (like click-tile-then-click-blank) is reused across multiple slides, make the **shared helper functions generic** (scope their DOM queries via `element.closest('.slide')` rather than a hardcoded slide id) so they can be safely reused, but still give each slide its **own check/reset function** with a unique name.

### Banner colour palette
Banner colours are chosen per lesson — the values below are AEF4 7A examples only, not fixed standards. Pick colours that fit the lesson's overall palette.

| Section | Example colour (AEF4 7A) |
|---|---|
| Warm-Up | #D35400 |
| Reading | #2A6B42 |
| Listening | #0E7A8A |
| Speaking | #1E4D8C |
| Grammar | #4A1A6A |
| Homework | #1C2B3A |
| Review | #2E2A6B |

---

## 📋 Column Order Rule

When exercises are displayed in two (or more) columns, the numbering always flows **top to bottom, then left to right** — never across rows.

- 10 exercises in 2 columns → 1–5 on the left, 6–10 on the right
- 9 exercises in 2 columns → 1–5 on the left, 6–9 on the right — always completing the left column first
- 3 columns → fill column 1 top-to-bottom, then column 2, then column 3

Never lay out exercises left-to-right across a row (1 on left, 2 on right, 3 on left, 4 on right…). Always finish one column before starting the next.

Layout classes: `.fixed-two-col` (2 columns), `.fixed-three-col` (3 columns), `.fixed-four-col` (4 columns) — all fixed CSS grids, used when items must split by an exact count rather than auto-balance by height.

### `.two-col` vs `.fixed-two-col` — pick based on content, not habit

> Added 2026-08-26 after AEF4-1B's HW2/HW4 dialogue exercises (multi-line `A:`/`B:` turns with `<br>`) were left in `.two-col` (native CSS multi-column auto-balancing), causing the first item of the left column and the first item of the right column to start at visibly different heights once turns spanned multiple lines.

`.two-col` (`columns:2`, browser auto-balance) only produces clean-looking results when every item is roughly the same height (e.g. short single-line vocabulary rows). **The moment an exercise has multi-line items of uneven length — especially multi-turn dialogues using `<br>` between speakers — switch to `.fixed-two-col` with two explicit child `<div>`s (items split per the Column Order Rule, e.g. 8 items → 4 in the first `<div>`, 4 in the second).** This guarantees the top of column 1 and the top of column 2 actually align, since both columns start at the same grid row instead of being auto-flowed by total height. Check this any time a conversation/dialogue exercise is built or edited — it's an easy one to miss because `.two-col` still "looks fine" until an item's turn count grows past one line.

---

## 📏 Text Line-Height Standard

> Added 2026-08-25 after AEF4-1B's instruction/discussion-question text looked visually cramped compared to quoted example text.

**Every block of instruction, discussion-question, or quoted text uses `line-height:1.7`.** This applies to (at minimum) `.instruction`, `.inst-light`, `.discuss-label`, `.ex-row`, `.glossary-box p`, `.gram-note`, `.gram-mistake`, `.ex-example-centered`, `.ccq-list li`, and any similar reading-text class — never leave a text block at the browser default line-height (~1.2) or at a tighter value like `1.5`/`1.6`, it reads as cramped next to the rest of the deck. When adding a new CSS class for body/instruction-style text, always set `line-height:1.7` explicitly (some exercise/dialogue text intentionally uses a looser `1.8–1.9` — see the Typography reference table — but never anything tighter than 1.7).

> Audited 2026-08-25 across all lesson files: `.inst-light` was missing `line-height` entirely (browser default ~1.2) in every lesson that had it, and `.glossary-box p` / `.gram-note` / `.gram-mistake` / `.ex-example-centered` / `.ccq-list li` were all sitting at `1.6` or missing it. All were corrected to `1.7`. When building or reviewing a lesson, check every reading-text class against this list — don't assume a class is compliant just because `.instruction` is.

**When a slide has 2 or more standalone discussion questions (not a single flowing instruction sentence), give each question its own boxed container** (e.g. a `.ccq-box` wrapping a `.discuss-label`) stacked with a visible gap between boxes (`display:flex;flex-direction:column;gap:16px` or similar) — never stack multiple questions inside one shared block separated only by `<br>`.

**Any image placed beside text in a `.fixed-two-col` / `.fixed-three-col` / `.fixed-four-col` layout must be height-constrained (e.g. `max-height`) so that section of the slide fits on screen without forcing a scroll.** Use `object-fit:contain` (not `cover`) whenever the full image needs to stay visible without cropping — `cover` is only for images being used as a decorative background fill where cropping the edges is acceptable.

---

## 🎨 Text Highlighting Standard

> Added 2026-08-25 after AEF4-1B's "How weird!" glossary box (a wall of plain-text reacting phrases) felt flat and hard to scan.

**Whenever an explanation box, glossary box, or grammar note has more than a sentence or two of plain text, break it up visually — don't leave dense paragraphs of uniform black text.** Use a mix of:

- **Bold + color** on the key phrase or pattern being taught (e.g. the fixed part of a structure like `How / That's`), often paired with a light matching background chip: `color:#1B6E96;background:#E4F1F7;padding:1px 8px;border-radius:5px;` (swap the color pair per item so multiple patterns in the same box are visually distinct).
- *Italics* for the variable/example word list that follows a pattern (e.g. the adjectives that can slot into it).
- Color coding kept **consistent with the rest of the slide/lesson** where a concept already has an established color (e.g. reuse the same color for "did" everywhere it's highlighted across a lesson — see Text Line-Height Standard's sibling rule on auxiliary-verb color coding).

This applies especially to `.glossary-box`, `.gram-box`, `.gram-note`, and similar theory/reference boxes — these are exactly the places dense text tends to accumulate. The goal is that a student can scan the box and immediately spot the pattern being taught, not read it top to bottom like a paragraph.

### Instructions that list the target language get the same colour-chip treatment

> Added 2026-08-26, reference implementation: AEF4-1B's `s-gbank-a`/`s-gbank-b` ("Quick-fire practice" / "A night at the club") instruction lines — `Complete with an auxiliary (do, did, have, is, etc.) or modal verb (can, would, etc.).` — where each listed word is individually bold + coloured.

**Whenever an instruction line names specific words or phrases the student is meant to use or respond with (a list of auxiliaries, modals, response patterns, etc.), style each one as bold + its own colour** — never leave them as plain text inside the instruction sentence:
```html
<strong style="color:#1B6E96;">do</strong>, <strong style="color:#C4614A;">did</strong>, <strong style="color:#0E7A8A;">have</strong>, etc.
```
- Give each distinct word/phrase its own colour (reuse colours already established for that word elsewhere in the lesson if one exists — e.g. if "did" is already blue-green in a grammar box on an earlier slide, keep it that colour here too).
- This applies to any instruction listing target language — not just auxiliary/modal lists: response-pattern lists ("So do I, Neither do I, I do, I don't, etc."), connector lists, modifier lists, or any other "use one of these" instruction.
- Check this on every slide during an audit, homework and non-homework alike — an instruction line that lists specific words in plain black text is the same category of "boring explanation" the Text Highlighting Standard already targets, just inside an instruction instead of a gram-box.

### Worked example sentences inside explanation boxes also get highlighted — never left as plain text

> Added 2026-08-25 after AEF4-1B's "The more, the merrier" meaning box was caught with its example sentences (in the `<ul>` list and the `.ex-example-centered` box) sitting in plain black/italic text while the rest of the box used colour chips.

**Any worked example sentence shown inside a `.gram-box`, `.glossary-box`, CCQ, or `.ex-example-centered` block must highlight the actual target structure inline** — not just the prose explaining it. If the box teaches a two-part pattern (e.g. `the + comparative …, the + comparative …`), each half of the pattern gets its own colour chip (reuse the same colour pair — e.g. blue for the first half, purple for the second — across every example in that box, so the repeated structure is instantly recognisable slide to slide). Don't highlight the surrounding explanation text and then leave the example sentence itself in plain italics — the example is the part a student actually reads to "get" the pattern, so it needs the highlight more than the prose does, not less.

**General principle — boring explanations should always be made more visually interesting, not just technically correct.** Every theory/meaning box (`.gram-box`, `.glossary-box`, CCQs, worked examples) should be treated as a design problem, not just a content problem: before finishing a slide, ask "would a student's eye actually land on the pattern being taught, or does this read like a wall of text?" If the answer is the latter, add colour chips, icons, spacing, or card layout — whatever makes the target structure jump out — rather than shipping the plain-text version because it's technically complete.

---

## 🪟 Two-Part Slide Standard

> Added 2026-08-25, reference implementation: AEF4-1B's Warm-Up slide (`s-warmup`) — title + discussion questions + image as part 1, four superstition cards as part 2.

Some slides genuinely hold two distinct activities stacked on one slide (e.g. a discussion prompt with an image, followed by a separate card exercise below). When this happens:

- **Part 1 should visually read as its own complete screen** — sized generously enough to feel intentional, not like leftover space above a second exercise. Don't leave a tall image floating with big empty margins, and don't let it feel like it's fighting part 2 for room.
- **Do not use a fixed pixel height or a raw `calc(100vh - Npx)` on the container** — actual usable height varies too much between windows and causes overflow/overlap bugs. Instead, size the dominant visual (usually the image) with `max-height: clamp(<min>px, <vh>vh, <max>px)` and `object-fit:contain`, letting it scale naturally with the viewport while staying within safe bounds.
- **Give part 1 a generous bottom margin before part 2 begins** — e.g. `margin-bottom:40px` on the part-1 container plus `margin-top:50-60px` on part 2's instruction paragraph. This visually separates the two parts so part 2 clearly starts "after a scroll," not immediately below part 1.
- **When part 1 has a left column of stacked question boxes next to a right-column image, align the columns to `align-items:flex-start`** (not `center`) so the top of the first question box lines up with the top of the image.

---

## 🟢 Example Presentation Standards

> Covers how a book exercise's worked example is numbered, styled, and positioned relative to word banks and the exercise's own columns. Added 2026-07-20 after a series of corrections on AEF3-2A's grammar bank exercises.

### Numbering — verify from the book page every time (non-homework slides)

**The example is never assumed to be "exercise 1." Check the actual book page image for how that specific lesson numbers things, and copy it exactly — never reuse a numbering convention from a different lesson file.**

- Outside the Homework section, many book pages show the example completely unnumbered — set apart visually (e.g. italic, underline, or a muted color) instead of a number badge — with the real numbered items starting fresh at 1 right after it.
- A different course/edition may legitimately number its example "1" and start real items at 2 — but that must be verified from that specific book page, never assumed or copy-pasted as a "standard" across lessons.
- Some examples span more than one sentence/line (e.g. a right-answer example AND a wrong-answer-with-correction example shown together) — include everything the book shows as part of the example, not just the first line.
- This is a "look before you build" rule, not a fixed formatting rule — nothing here is exempt from re-checking the source page image.

### Homework examples — numbered "1" (its own mandatory rule)

Inside the Homework section specifically (after `hw-cover`), examples follow a **different, mandatory** convention: every worked example is numbered **1** with the specific green rounded badge style, and real questions start at **2**. This is intentional and does not conflict with the rule above — see **📝 Homework Exercise Standards → Examples — numbered "1"** below for the full spec. The "verify from the book page" rule above applies only outside the Homework section.

### Answer highlighting — green bold chip, not blue italic underline

**When an example shows the model/correct answer inline (words that fill blanks or complete a sentence), those target words are styled as a green bold highlight chip:**

```css
color:#1A7A4A; font-weight:800; background:#E3F5EA; padding:1px 7px; border-radius:5px;
```

- This is the same green already used for `.circ-opt.correct` / `.ans-input.correct` elsewhere in the file, so "this is the correct answer" reads consistently across the whole lesson.
- Applies whether the example sits inline mid-conversation (e.g. a reading-conversation slide showing the model answer for blank 1 in context) or as a standalone "example" block before a numbered exercise list (e.g. a "Complete the conversation" grammar-bank exercise).
- The word "example" itself (or an `<em>example</em>` label) stays small, muted, and unnumbered, set apart from the real numbered items — only the *target answer words within the example* get the green highlight, not the label text.
- Do not write the literal word "EXAMPLE" as a stand-in for showing the actual filled answer inside a running conversation/text — show the real answer, highlighted green, so the student can see exactly what a correct answer looks like in context.
- If a conversation example has multiple speaker turns (A/B), always break each speaker onto its own line, exactly matching the format used for the real numbered items in the same exercise (e.g. `<b>A:</b> ...<br><b>B:</b> ...` — colon included, matching the real items' own A:/B: format).

### Example placement relative to word banks and columns

> Revised 2026-08-26 — the previous version of this rule (folding the example into the top of the right column for odd item counts) shipped on HW5 and produced a confusing, unacceptable layout: items read "2, 3, 4" in the left column and "1, 5, 6" in the right column, i.e. the example broke the visual reading order between the two columns. That version of the rule is retired — never fold the example into either column again.

**The example always gets its own centered block, placed above the two-column (or word-bank) exercise list — never folded into either column, regardless of whether the real item count is odd or even.** Items then split by the standard Column Order Rule as if the example weren't part of the grid at all:
- Even real item count (e.g. 8): 4 left / 4 right.
- Odd real item count (e.g. 5 or 7): left column gets the extra item (e.g. 5 → 3 left / 2 right).

This keeps the numbered items reading in strict ascending order across the two columns every time, with the example sitting visually separate above — never interleaved with the numbering.

---

## 📝 Exercises

- Every exercise with **fixed answers** → **Check Answers** + **Reset** buttons
  - Uses teacher's book answer key (always verify against the key, not guessing)
  - `checkSlide(sid)` / `resetSlide(sid)` for standard input exercises
  - `data-ans` attribute on each input; `data-alt` for alternate accepted answers
  - `norm(s)` normalises answers: trim, lowercase, strip trailing punctuation, collapse spaces

### Text alignment in inputs and textboxes
- Text inside all inputs and textboxes must be **left-aligned** — never centered
- This applies to all exercise types: gap fills, open answers, dialogue completions, any text field
- Only center text if explicitly requested

### No placeholder text in student answer boxes

**Text boxes and text lines where a student is meant to write something must always be left completely empty — no placeholder text, ever.**
- No `placeholder="Type the correct sentence..."`, `placeholder="Complete the sentence..."`, `placeholder="Write your answer here..."`, or any other instructional/example filler inside an `<input>` or `<textarea>` a student types into.
- The instruction line above the exercise (`.instruction` / `.inst-light`) is where any guidance belongs — never inside the answer field itself.
- Applies to every typed-answer exercise type: sentence-rewrite boxes, listening-completion lines, writing-task textareas (short story, reading continuation, "make it personal" sentences), word-scramble inputs, and any future typed-answer exercise.
- **Exempt**: `#notesTA` (the slide Notes panel) — app UI chrome for the tutor/student's own private notes, not lesson exercise content, and keeps its `data-placeholder="Your notes for this slide…"`.

### Uniform width for typed answer blanks

**Every typed-answer blank (`.ans-input`) within the same exercise must be the same fixed width — never sized to match, or hint at, the length of its own expected answer.**
- Variable widths leak the answer. If one blank is narrow and another is wide, a student can guess the grammatical form (e.g. short simple form vs. long continuous form) just by looking at the size of the space, without knowing the language.
- Fix: pick one width that comfortably fits the *longest* expected answer in the exercise, and apply that same width to every blank in the set — including the short ones, which will now have visible empty space at the end. That empty space is intentional and correct; it's what keeps the exercise fair.
- Applies to any inline `style="width:...px;"` (or a shared class) placed on `.ans-input` elements — not just present perfect simple/continuous exercises, but any gap-fill where answers could vary in length (verb forms, contractions, one-word vs. multi-word answers, etc.).
- The base `.ans-input` class only defines `min-width:80px` with no default fixed width, so any exercise using variable per-blank widths needs to be checked and corrected under this rule.
- **Exempt**: blanks in genuinely different exercises/slides where there's no shared answer-length pattern to give away (a single standalone blank with no sibling blanks in the same task), or widths driven by layout/space constraints rather than answer length — but default to uniform width whenever in doubt.

### Check Answers — feedback states (apply to every exercise)
| State | Border | Text colour | Answer shown? |
|---|---|---|---|
| Empty (not filled) | orange | orange | No |
| Correct | green | green | No — student typed it correctly |
| Wrong | red | red | No — student must try again |

**No answer is ever revealed** — not for empty inputs, not for wrong answers. The student always has to figure it out and try again. Never show the correct answer automatically.

- Every exercise with **open/creative answers** → **Suggested Answer** + **Reset** buttons
- Instructions always adapted for **one-on-one lessons**
  - No "discuss with a partner" → use "share your thoughts", "tell me", etc.
  - Never reference "your tutor" — there is no separate tutor role; the teacher runs the lesson live, so instructions should assume just the student working through the exercise
- Always use the **actual book exercises** — never invent content
- **Images**: styled placeholder `<div>` where the book image goes (never leave blank)
- **Audio files**: use the **native `<audio controls>` element** wrapped in a styled container

### Audio standards (follow every time)

1. **Always ask for the filename** — never assume or invent an audio filename. Before building any slide with audio, ask: *"What is the audio filename for this slide?"*
2. **Never display the raw filename on screen** — nothing on the slide should show the .mp3 filename itself.
3. **Player style**: native `<audio controls src="filename.mp3">` set to full container width, wrapped in a light-coloured rounded pill container (e.g. `background: #f0f4f8; border-radius: 999px; padding: 10px 18px`)
   - Native controls provide play/pause, seekable progress bar, time display, and volume — no custom JS needed
   - Reference style: AEF3 1B audio player
4. **No names, titles, or labels glued to the player — zero exceptions.** `.audio-box` (or wherever the `<audio>` element lives) must contain **nothing but the `<audio>` element itself** — no `<p>`, `<span>`, or icon inside or immediately above/below it describing what the track is (no "🎧 Listen and check", no "Track 2.8", no speaker names attached to the box). If the student needs an instruction before listening, that instruction belongs in the slide's normal `.instruction`/`.inst-light` paragraph placed *before* the audio box, exactly like any other exercise instruction — never as a caption specifically glued to the player.

---

## 🗃 Exercise Type Reference

Use this table to decide how to build each exercise. Every type has a fixed interaction pattern — don't improvise a new one if the type already exists here.

| Exercise type | Interaction | Check / Reveal | Notes |
|---|---|---|---|
| **Gap fill — typed** | Student types into inline input | Check Answers (orange/green/red) + Reset | `data-ans`, `data-alt`; never reveal answer |
| **Word bank → fill blank** | Click chip in bank → click blank to place it; click filled blank to remove | Check Answers + Reset | Chip greys out when used; blank shows the word — see Wordbank Click Behavior below for when to use this vs. the typed variant |
| **Sentence colour-pair matching** | Click sentence on left → assigns colour; click response on right → pairs them | Check Answers (only correct pairs turn green) + Reset | 4 colours: purple, orange, green, teal; `gm2PickSent` / `gm2PickResp` / `checkGM2` |
| **Image → sentence matching** | Click image → highlights; click sentence → pairs them with colour | Check Answers + Reset | Same colour-pair logic; each pair gets its own colour |
| **Multiple choice — circle** | Click one option per question to select it (highlighted); click again to deselect | Check Answers (correct → green, wrong → red) + Reset | `circPick` / `checkCircSlide`; only one selection per question |
| **Checkboxes (tick all correct)** | Click items to toggle selected state | Check Answers (selected+correct → green, selected+wrong → red) + Reset | Student can retry after red; `toggleCheck` / `checkCheckEx` |
| **True / False rows** | Click row to toggle ✓ or ✗ | Check Answers + Reset | Row turns green/red on check; `toggleTick` |
| **Myth / Statement true-false** | Click statement to mark True or False | Check Answers + Reset | `toggleMyth` / `checkMyths` |
| **Word order chips** | Chips are visual reference only — clicking marks as "used"; student types answer in text box | Check Answers + Reset | `wpToggle`; `data-alt` for alternatives |
| **Classify / Sort into groups** | Click item → select it; click target group/column → assigns it | Check Answers + Reset | Each group is a coloured drop zone |
| **Pronunciation — sort into columns** | Click word → select; click column → places it | Check Answers + Reset | `selectPronWord` / `clickPronCol` / `checkPron` |
| **Syllable / stress marking** | Click on the stressed syllable in a word | Check Answers + Reset | `sylClick`; correct syllable turns green on check |
| **Ranking / ordering** | Click cards to assign a rank number (cycles 1→2→3→…→blank) | Check Answers + Reset | `cycleRank`; show correct ranking on check |
| **Vocabulary flashcards** | Prev / Next buttons to flip through word pairs; click to reveal meaning | No check — self-guided | `showVocabPair` / `revealVocabMeaning` |
| **Open text box** (discussion, writing) | Student types freely | 💡 Suggested Answer toggle (show/hide) + Reset | Never Check Answers for open-ended; text always left-aligned |
| **Answer key toggle** (listening, reading) | Button reveals/hides the answer key below the exercise | Toggle: 🔑 Show Answer Key / 🔒 Hide Answer Key | Use when answers are open-ended or context-dependent |
| **Spin the Wheel** | Click Spin button; wheel animates and lands on a random prompt | No check | `drawWheel` / `doSpin`; redraw on slide entry via `goTo` hook |
| **Dice Roller** | Click Roll button; die animates and lands on a random face 1–6, revealing that number's prompt | No check | `rollDie`; prompts stored per-slide in a `dicePrompts['dice-{topic}']` object — see Speaking Activities section |
| **Concept Checking Questions (CCQ)** | Read-and-discuss list, no click interaction | No check — spoken exchange | Used at the Meaning stage of a grammar sequence; see CELTA section |
| **Timeline diagram** | Static visual, no interaction | No check | CSS-only horizontal timeline for tense meaning; see CELTA section |
| **MadLibs-style reveal** | Student types into blanks without seeing the story, then reveals | ✨ Reveal button (substitutes inputs into a template) | `revealMadLib`; freer-practice/personalization activity |
| **Bingo grid** | Click a cell to mark it | No check — teacher-led call-out | Reuses the checkbox-toggle pattern; vocab review |
| **Word Scramble** | Student types the unscrambled word into a normal input | Check Answers + Reset | Same as gap-fill typed; only the scrambled-letters display is different |
| **Virtual Breakout (unlock puzzle)** | Type the answer/code into each "lock" to unlock it | Auto-unlocks on correct code (no separate Check button) | `checkLock`; optional gamified review/wrap-up closer |
| **Audio player** | Native `<audio controls>` with seekable progress bar | No check | Always ask for filename; never show filename; never a glued-on label — see Audio standards above |

### Wordbank Click Behavior — decide by whether the word changes form

Before building any exercise that gives the student a list of words to complete sentences/blanks, check the answer key: **does every word get used exactly as written in the bank, with no change at all?**

**Case A — words are used unchanged → click-tile-then-click-blank (word gets placed)**
- If every word in the bank is dropped into its blank exactly as written (no conjugation, no pluralizing, no added words), use the "Word bank → fill blank" pattern: click a tile in the bank → click the blank it belongs in → the tile's text fills the blank and the tile grays out ("used"). Click a **filled** blank again to remove it and return the tile to the bank.
- `wbPick` / `wbPlace` / `checkWbSlide` / `resetWbSlide` — already fully generic and reusable.
- If the exercise's worked example consumes one tile, that tile starts already marked "used" (grayed out, not clickable).

**Case B — one or more words need to change form → click-to-mark-used, typed blank**
- If **any** word in the bank needs to change (verb conjugation/tense, add -s, add "is"/"are", pluralize, etc.) to fit its sentence, a placed-tile mechanic would silently produce wrong sentences. Instead: the blank stays a normal **typed** `.ans-input`, graded with `checkSlide`/`data-ans` as usual.
- The wordbank itself is still fully **clickable** — clicking a word toggles a crossed-out/grayed "used" visual state, purely as a self-tracking aid so the student can see at a glance which base words they've already drawn on. This state is **not graded** and does not feed into `checkSlide` — it's bookkeeping, not part of the answer.
- Generic helper: `mvWordToggle(el){ el.classList.toggle('used'); }` — one class toggle, reusable across any lesson's wordbank of this type.
- If the worked example already uses one of the words, that word starts pre-marked "used" and is **not clickable** (`cursor:default`, no `onclick`).
- Per the Uniform Answer Blank Width rule above: since Case B blanks hold answers of varying length by definition, all blanks in the exercise must still share one uniform width.

**Exception — reusable word lists ("you can use these more than once")**
- If the exercise's own instruction says a word may be reused, don't apply either click-tracking pattern — leave the list as plain static reference text (not clickable), styled distinctly (e.g. inside a `.card`).

**Non-exception — pure reference/discussion word lists**
- A word list shown only to support a discussion or observation question (not feeding any blank at all) isn't a "wordbank" under this rule at all. Leave it as plain static text.

---

## 🎨 Special Exercise Types

### Checkboxes (multiple correct answers)
- `var correctAnswers = {n: true, ...}` defines which items are correct
- `toggleCheck(n)` — click to select/deselect
- On Check: selected+correct → green, selected+wrong → red, unselected → neutral
- Student can retry after seeing red (no full lock-out)

### Colour-pairing matching (Grammar Analyzing)
- `.gm2-c0` purple · `.gm2-c1` orange · `.gm2-c2` green · `.gm2-c3` teal
- Click sentence on left → picks colour; click response on right → pairs them
- `gm2DoPair()`, `checkGM2()`, `resetGM2()`
- On Check: only correct pairs turn green

### Word chips (Word Order exercises)
- Chips are **visual only** — clicking marks a chip as "used" (`wpToggle`)
- Student types the actual answer in a text box
- `data-alt` for alternative accepted answers
- Example box shows chips already in `.wp-used` state + green answer chip

### Spin the Wheel
- `window.drawWheelFn` exposed so wheel redraws on slide entry
- Hook in `goTo`: `if (slides[current].id === 's-spin' && typeof window.drawWheelFn === 'function') { setTimeout(window.drawWheelFn, 50); }`

---

## 📒 Notes System (perfected — apply to every lesson)

> There are **two** distinct nav-bar buttons (💾 Save Notes and 🖨️ Print Lesson — neither replaces the other), and the toolbar has **4 highlight colors**, not one.

### In-lesson editor
- Toolbar: **B** (bold) · **U** (underline) · 4 highlight-color swatches · ✕ remove-highlight — see "Notes toolbar" below
- `contenteditable` div (not a textarea), id `notesTA`, with `data-placeholder="Your notes for this slide…"` (uses `:empty::before` for the placeholder text) and `spellcheck="false"`
- Saves via `oninput="saveNotes()"` directly on the element (not a separate `addEventListener`)
- Box: **360px wide**, min 220px / max 260px height, scrolls when full
- `saveNotes()` / `loadNotes(idx)` use `innerHTML` (preserves formatting)
- Arrow keys inside notes box do **not** trigger slide navigation:
  ```js
  if (tag === 'INPUT' || tag === 'TEXTAREA' || document.activeElement.contentEditable === 'true') return;
  ```
- Requires a top-level `var notesOpen = false;` alongside `notesData`/`current`

### Notes toolbar — 4 highlight colors + remove, with toggle-off

```html
<div id="notesToolbar">
  <button onclick="notesFormat('bold')" title="Bold"><b>B</b></button>
  <button onclick="notesFormat('underline')" title="Underline"><u>U</u></button>
  <span style="display:flex;gap:3px;align-items:center;margin-left:6px;padding-left:6px;border-left:1px solid rgba(255,255,255,.2)">
    <button onclick="notesHilite('#FFE600')" title="Yellow" style="background:#FFE600;width:20px;height:20px;padding:0;border-radius:4px;border:none;cursor:pointer;"></button>
    <button onclick="notesHilite('#90EE90')" title="Green"  style="background:#90EE90;width:20px;height:20px;padding:0;border-radius:4px;border:none;cursor:pointer;"></button>
    <button onclick="notesHilite('#FFB3C6')" title="Pink"   style="background:#FFB3C6;width:20px;height:20px;padding:0;border-radius:4px;border:none;cursor:pointer;"></button>
    <button onclick="notesHilite('#ADD8E6')" title="Blue"   style="background:#ADD8E6;width:20px;height:20px;padding:0;border-radius:4px;border:none;cursor:pointer;"></button>
    <button onclick="notesHilite('remove')" title="Remove highlight" style="font-size:.78rem;padding:2px 7px;color:#ff9999;margin-left:2px;background:rgba(255,255,255,.1);border:none;border-radius:4px;cursor:pointer;">✕</button>
  </span>
</div>
<div id="notesTA" contenteditable="true" data-placeholder="Your notes for this slide…" spellcheck="false" oninput="saveNotes()"></div>
```

- 4 fixed highlight colors: yellow `#FFE600`, green `#90EE90`, pink `#FFB3C6`, blue `#ADD8E6` — swatch buttons, no color picker.
- `notesHilite(color)` requires a text selection (no-op if nothing selected). Clicking the **same color that's already applied to the selection toggles it off** (checks `queryCommandValue('backColor')` against the target color first).
- A dedicated ✕ "Remove highlight" button always clears highlighting regardless of color, by setting `hiliteColor` to `transparent` and unwrapping any resulting empty-background spans so they don't linger in the DOM.
- Function names: `notesFormat(cmd)` for bold/underline, `notesHilite(color)` for all highlight actions — **not** `fmt()` / `fmtHilite()`.
- Highlight text stays forced dark `#1a1a1a` so it's readable against any of the 4 colors on both dark and light backgrounds.

### Notes button label toggles

```js
function toggleNotes(){
  notesOpen = !notesOpen;
  var panel = document.getElementById('notesPanel');
  panel.classList.toggle('open', notesOpen);
  if (current === 0) panel.classList.toggle('cover', notesOpen);
  document.getElementById('notesBtn').textContent = notesOpen ? '✕ Close' : '📝 Notes';
  /* reset position on close */
  if (!notesOpen) { panel.style.left=''; panel.style.top=''; panel.style.right=''; panel.style.bottom=''; panel.style.transform=''; }
}
```

The button text itself changes between "📝 Notes" and "✕ Close" — it isn't a fixed label.

### Draggable panel always resets to its default position on close

The notes panel can be dragged around the screen mid-lesson (see the drag-handle script further down), but that dragged position is **session-only, never persisted across a close/reopen**. Every time `toggleNotes()` closes the panel (transitions from open → closed), it must clear the inline `left`/`top`/`right`/`bottom`/`transform` styles the drag handler set, so the panel falls back to its default CSS position (top-right, or centered for the `.cover` state) the next time it's opened — regardless of where it was last dragged to.

- This reset happens **only on close**, not on every render — dragging while the panel is open must still work smoothly and keep its position until the teacher closes it.
- Applies to every lesson using the draggable notes panel (all of them, going forward).
- If a lesson's `toggleNotes()` uses a differently-named open/closed flag (e.g. a local `isOpen` captured before the toggle instead of the shared `notesOpen`), adapt the condition accordingly — the point is: whichever branch represents "the panel just closed," reset the inline position styles there.

### Panel animation
`#notesPanel` uses `max-height: 0 → 320px` + `opacity` transition (not `display:none/flex`) for a smooth slide-open, and has a dark frosted-glass style (`background: rgba(10,40,54,.92)` on the textarea, `backdrop-filter: blur`) rather than a plain white box.

### Cover slide behaviour
- Notes do **not** auto-open on the cover
- When opened on the cover, panel expands to **full-page size** (centred, `min/max-height: calc(100vh - 210px)`)
- Button works to close/reopen on all slides including the cover
- `toggleNotes()` toggles the `.cover` class when on slide 0
- `goTo()` adds `.cover` if open on slide 0; removes `.cover` on all other slides

### 💾 Save Notes button

Background `#2E2A6B`. Opens a new tab with a clean, printable summary of every slide that has notes (slide number + label as a card header, note content below), then triggers `window.print()` after a short delay. If no notes exist yet, alerts "No notes to save yet!" instead of opening a blank tab. This is `savePDF()`.

### 🖨️ Print Lesson button

Background `#0E5A8A`. **A separate, complementary tool from Save Notes — neither replaces the other.** Save Notes exports just the notes as a standalone reference page; Print Lesson exports the whole lesson deck with notes embedded in context. When clicked, Print Lesson prints the entire lesson as a PDF — one slide per page, in their original visual layout — with the lesson link banner on the first page and teacher's notes at the bottom of any page that has them.

> Reference implementation: `/Users/nanda/Desktop/AEF4 3A/index.html` — use this as the exact model.

#### What the PDF contains:
1. **Every slide**: shown in its original visual layout (colours, fonts, layout), one per page. Each slide also gets a small grey page header at the top: `AEF[X] [Y] — [Lesson Title]` (10px, generated via CSS `::before`).
2. **Cover slide (page 1)**: the CSS `::before` header is suppressed. Instead, a `.lesson-link-print` banner div is injected at the very top — a styled dark gradient card with the lesson title large and bold, and below it "Click here to access the lesson online: [link]".
3. **Notes block**: on any slide with teacher's notes, a light-blue `.slide-notes-print` block (`📝 Teacher Notes` label) is injected at the bottom of that slide before printing, then removed after.
4. **UI chrome hidden**: `#notesBtn`, `#notesPanel`, `#nav`, `#homeBtn` are all hidden in print.

#### CSS — add to `<style>` block (exact from AEF4 3A):
```css
/* Hidden in normal view, shown only at print */
.slide-notes-print { display: none; }
.lesson-link-print { display: none; }

@media print {
  @page { margin: 1.2cm; }
  * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  html, body { height: auto !important; overflow: visible !important; background: #fff !important; display: block !important; }
  #deck { overflow: visible !important; height: auto !important; display: block !important; position: static !important; }
  #notesBtn, #notesPanel, #nav, #homeBtn { display: none !important; }

  /* All slides when printing full lesson */
  body.print-all .slide {
    display: flex !important; flex-direction: column !important;
    position: relative !important; inset: auto !important; opacity: 1 !important;
    padding: 16px 24px !important; page-break-after: always; break-after: page;
    min-height: 0 !important; height: auto !important;
  }
  /* Prevent blank gaps from flex:1 children */
  .slide * { flex: none !important; height: auto !important; min-height: 0 !important; max-height: none !important; }
  .slide-main, .content { overflow: visible !important; }
  img { max-height: 240px !important; width: auto !important; max-width: 100% !important; object-fit: contain !important; }

  /* Small page header on every slide: "AEF4 3A — Lesson Title" */
  body.print-all .slide::before {
    content: "AEF[X] [Y] \2014  [Lesson Title]"; /* update per lesson */
    display: block !important; font-size: 10px; color: #999;
    font-family: 'Segoe UI', Arial, sans-serif;
    padding-bottom: 5px; border-bottom: 1px solid #ddd; margin-bottom: 8px;
  }
  /* Cover slide: suppress generic header (lesson-link-print replaces it) */
  body.print-all #s1::before { display: none !important; }

  /* Lesson link banner — cover slide only */
  .lesson-link-print {
    display: block !important; padding: 28px 32px; margin-bottom: 20px;
    background: linear-gradient(135deg, #0A1628 0%, #1A3A6B 55%, #0E5A8A 100%);
    /* ↑ use the lesson's own dark gradient colours here */
    border-radius: 12px; text-align: center;
    font-family: 'Segoe UI', Arial, sans-serif;
  }
  .lesson-link-print .lp-title {
    display: block; font-size: 30px; font-weight: 900; color: #fff;
    margin-bottom: 10px; letter-spacing: .01em; line-height: 1.2;
  }
  .lesson-link-print .lp-sub {
    display: block; font-size: 16px; color: rgba(255,255,255,.88); font-weight: 500;
  }
  .lesson-link-print a { color: #4FC3F7; font-weight: 800; text-decoration: underline; font-size: 17px; }

  /* Teacher notes block */
  .slide-notes-print {
    display: block !important; margin-top: 12px; padding: 10px 14px;
    border-top: 2px solid #0E5A8A; background: #E3F2FD; border-radius: 6px;
    font-size: 12px; line-height: 1.6; color: #1A1A2E;
  }
  .slide-notes-print-label {
    font-size: 10px; font-weight: 800; color: #0E5A8A;
    text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; display: block;
  }
}
```

#### JavaScript — `printAll()` function (exact from AEF4 3A):
```js
function printAll() {
  saveNotes();
  var injected = [];

  slides.forEach(function(slide, i) {
    // Inject lesson link banner into cover slide only
    if (i === 0) {
      var linkEl = document.createElement('div');
      linkEl.className = 'lesson-link-print';
      linkEl.innerHTML =
        '<span class="lp-title">[Lesson Title]</span>' +
        '<span class="lp-sub">Click here to access the lesson online: ' +
        '<a href="[LESSON_URL]" target="_blank">[LESSON_URL]</a></span>';
      slide.insertBefore(linkEl, slide.firstChild);
      injected.push(linkEl);
    }
    // Inject teacher notes block at the bottom of each slide with notes
    var n = notesData[i] || '';
    if (n.replace(/<[^>]*>/g, '').trim()) {
      var notesEl = document.createElement('div');
      notesEl.className = 'slide-notes-print';
      notesEl.innerHTML = '<div class="slide-notes-print-label">📝 Teacher Notes</div>' + n;
      slide.appendChild(notesEl);
      injected.push(notesEl);
    }
  });

  document.body.classList.add('print-all');
  window.print();

  // Clean up after print dialog closes
  setTimeout(function() {
    document.body.classList.remove('print-all');
    injected.forEach(function(el) { el.parentNode && el.parentNode.removeChild(el); });
  }, 1500);
}
```

#### Nav bar button HTML:
```html
<button onclick="savePDF()" style="margin-left:10px;padding:5px 12px;background:#2E2A6B;color:#fff;border:none;border-radius:7px;font-size:.82rem;cursor:pointer;font-family:inherit;">💾 Save Notes</button>
<button onclick="printAll()" style="margin-left:10px;padding:5px 12px;background:#0E5A8A;color:#fff;border:none;border-radius:7px;font-size:.82rem;cursor:pointer;font-family:inherit;">🖨️ Print Lesson</button>
```
Both buttons are styled separately from the regular Prev/Next nav buttons — smaller font, placed after the Next button, Save Notes first then Print Lesson. Colors: Save Notes `#2E2A6B`, Print Lesson `#0E5A8A`.

#### Per-lesson values to update (in the CSS `::before` content and in `printAll()`):
- `[Lesson Title]` → the lesson's human-readable title (e.g. `Fasten your seat belts`)
- `[LESSON_URL]` → the deployed lesson URL, now always in the form `https://teacher-nanda.github.io/AEF-Courses/[FOLDER]/index.html` (e.g. `https://teacher-nanda.github.io/AEF-Courses/AEF4-3A/index.html`) — see **🌐 AEF-Courses Deployment** above. Older lessons not yet migrated into AEF-Courses may still use their old Netlify URL until moved.
- The gradient in `.lesson-link-print` → match the lesson's own cover gradient colours
- The `::before` content string → `"AEF4 3A \2014  Fasten your seat belts"` (update per lesson)

#### Important details:
- The `.lesson-link-print` banner is injected into `slides[0]` first child — it appears **above** all cover slide content on the printed page
- The small grey page header (`::before`) appears on every slide **except** the cover (suppressed via `body.print-all #s1::before { display:none }`)
- Notes blocks use **light blue** background (`#E3F2FD`) with a teal top border — not yellow
- Everything injected is removed via `setTimeout` after `window.print()` — DOM is always restored cleanly
- Bold, underline, and yellow highlights in notes are preserved (stored as `innerHTML`)

---

## 🌐 AEF-Courses Deployment

All AEF lessons now live inside **one unified folder and one unified GitHub repo**, called `AEF-Courses`, on the Desktop. This replaced the old setup where each lesson (AEF3-1B, AEF4-1A, AEF4-2A…) had its own separate folder and its own separate Netlify site/repo.

### Structure
```
AEF-Courses/
├── AEF Lesson Standards.md   ← this file — the single source of truth for every lesson
├── index.html          ← homepage — lists/links to every course as a card
├── .gitignore           ← excludes PDFs, MP3s, node_modules, .DS_Store, backups
├── AEF3-1B/
│   └── index.html
├── AEF4-1A/
│   └── index.html
├── AEF4-2A/
│   └── index.html
└── ...one folder per lesson
```

- **Live site**: https://teacher-nanda.github.io/AEF-Courses/
- **Each lesson's URL**: `https://teacher-nanda.github.io/AEF-Courses/[FOLDER]/index.html`
  - e.g. `https://teacher-nanda.github.io/AEF-Courses/AEF3-1B/index.html`
- The homepage (`AEF-Courses/index.html`) has a small `courses` array near the bottom of the file — one entry per lesson (`level`, `folder`, `file`, `code`, `title`). Add a line there whenever a new lesson folder is pasted in.
- PDFs, MP3s, and other copyrighted textbook/audio files stay in each lesson folder locally (needed for the slides/audio to work) but are **excluded from git** via `.gitignore` — they are never pushed to GitHub.

### Checklist when adding a new lesson folder to AEF-Courses
1. Paste the lesson folder into `AEF-Courses/` (folder name uses hyphens, e.g. `AEF4-3A`, not spaces)
2. Remove any leftover nested `.git` folder inside it, if the lesson used to be its own separate repo
3. Add a card entry to the `courses` array in `AEF-Courses/index.html`
4. Add the 🏠 All-Courses link to the lesson's cover slide (see standard above) — `href="../index.html"`
5. Update the lesson's **saved-PDF link** (the one injected by `printAll()` into the cover banner and the lesson-notes panel) to `https://teacher-nanda.github.io/AEF-Courses/[FOLDER]/index.html` — see `[LESSON_URL]` note in the Print Lesson section above
6. `git add` + commit inside `AEF-Courses`

---

## 🔗 Live Lesson URLs

> Format for every lesson inside AEF-Courses: `https://teacher-nanda.github.io/AEF-Courses/[FOLDER]/index.html`

| Lesson | URL |
|---|---|
| AEF3 1B | https://teacher-nanda.github.io/AEF-Courses/AEF3-1B/index.html |
| AEF4 1A | https://teacher-nanda.github.io/AEF-Courses/AEF4-1A/index.html |
| AEF4 1B | https://teacher-nanda.github.io/AEF-Courses/AEF4-1B/index.html |
| AEF4 2A | https://teacher-nanda.github.io/AEF-Courses/AEF4-2A/index.html |
| AEF4 Review 1&2 | https://teacher-nanda.github.io/AEF-Courses/AEF4-Review1-2/index.html |
| AEF4 3A | https://teacher-nanda.github.io/AEF-Courses/AEF4-3A/index.html |
| AEF4 7A | https://aef4-7a.netlify.app/ *(not yet migrated into AEF-Courses)* |
| Business English for Everyone (Level 1) — Business-EFE1 | https://teacher-nanda.github.io/Business-EFE1/ *(separate repo, not part of AEF-Courses)* |

*(Add new lesson URLs here as they are migrated into AEF-Courses)*

---

## 🖼 COVER SLIDE — MANDATORY STANDARD

> ⚠️ READ THIS EVERY TIME BEFORE BUILDING A COVER. NO EXCEPTIONS.
> Reference lessons: AEF4 7A and AEF3 1B. When in doubt, open one of those files.

---

### WHAT GOES ON THE COVER — COMPLETE LIST

The cover has **exactly these elements and nothing else**:

1. Full-screen dark gradient background
2. Three lines of centred text (see below)
3. Notes button — top right
4. Homework button — bottom right
5. 🏠 All-Courses link — bottom left
6. Nav bar — bottom of screen

That is all. No images, no banners, no extra labels, no decorations, no other buttons.

---

### THE THREE TEXT LINES

All three lines are centred horizontally and vertically on the screen.

**Line 1 — `.title-label`**
```
Conversational English
```
- Uppercase, letter-spacing, muted white (`rgba(255,255,255,.65)`)
- `font-size:1.1rem; font-weight:500; letter-spacing:.18em; text-transform:uppercase`
- ⚠️ This is ONE line by itself — never combined with Line 2

**Line 2 — `.title-sub`**
```
with teacher Nanda
```
- Smaller, slightly muted white (`rgba(255,255,255,.75)`)
- `font-size:1.15rem; font-weight:400`
- ⚠️ This is ONE line by itself — never combined with Line 1

**Line 3 — `.title-main`**
```
[The Lesson Title]
```
- Large, heavy, white — `font-size:3.4rem; font-weight:900; color:#fff; line-height:1.1`
- One or two meaningful words get the accent colour using `.title-accent` — choose whichever words look best visually
- The rest of the title stays white

**Full HTML structure of the cover — copy this every time:**
```html
<div class="slide active" id="s1">
  <div class="title-inner">
    <div class="title-label">Conversational English</div>
    <div class="title-sub">with teacher Nanda</div>
    <div class="title-main">[White words] <span class="title-accent">[Accent words]</span></div>
    <a href="../index.html" title="All AEF Courses"
       style="position:absolute;bottom:70px;left:32px;font-size:1.7rem;line-height:1;
              text-decoration:none;filter:drop-shadow(0 1px 3px rgba(0,0,0,.3));">🏠</a>
    <div style="position:absolute;bottom:70px;right:32px;">
      <button onclick="goToId('[hw-slide-id]')"
        style="background:#1C2B3A;color:#fff;border:none;border-radius:10px;
               padding:11px 24px;font-size:.95rem;font-weight:700;cursor:pointer;
               letter-spacing:.03em;">📝 Homework</button>
    </div>
  </div>
</div>
```

---

### NOTES BUTTON — TOP RIGHT, ALWAYS

```html
<button id="notesBtn" onclick="toggleNotes()">📝 Notes</button>
```
```css
#notesBtn {
  position: fixed; top: 14px; right: 22px; z-index: 1000;
  background: rgba(10,40,54,.88); color: #fff; border: none;
  padding: 9px 20px; border-radius: 22px; cursor: pointer;
  font-size: .92rem; font-weight: 600;
}
```
- ✅ Fixed, top right corner, every slide including the cover
- ❌ Never bottom left, never bottom centre, never anywhere else

### HOMEWORK BUTTON — BOTTOM RIGHT, INSIDE COVER ONLY (AEF4 7A standard)

The Homework button sits inside `.title-inner` on the cover slide, positioned absolutely at **bottom right**. It is **not a fixed button** — it is part of the cover slide's content and disappears automatically when you navigate away.

**Exact HTML — copy this every time (taken directly from AEF4 7A):**
```html
<div style="position:absolute;bottom:70px;right:32px;">
  <button onclick="goToId('[hw-slide-id]')"
    style="background:#1C2B3A;color:#fff;border:none;border-radius:10px;
           padding:11px 24px;font-size:.95rem;font-weight:700;
           cursor:pointer;letter-spacing:.03em;">📝 Homework</button>
</div>
```

This `<div>` is the **last child inside `.title-inner`**, before its closing `</div>`.

Every value — do not change:
- Position: `absolute; bottom:70px; right:32px` → **bottom right of the cover**
- Background: `#1C2B3A` (dark solid navy — not transparent, not frosted)
- Border: `none`
- Border-radius: `10px` (rounded rectangle — **not a pill**)
- Padding: `11px 24px`
- Font-size: `.95rem`, font-weight: `700`
- Letter-spacing: `.03em`
- Label: `📝 Homework`

- ✅ `position:absolute` inside `.title-inner` — disappears with the cover slide naturally
- ✅ Bottom right corner
- ✅ Dark solid rectangle, not frosted glass
- ❌ Never `position:fixed`
- ❌ Never bottom centre
- ❌ Never a pill (`border-radius:30px`)
- ❌ Never outside `.title-inner`

### 🏠 ALL-COURSES LINK — BOTTOM LEFT, INSIDE COVER ONLY (AEF-Courses standard)

Every lesson now lives inside the unified **AEF-Courses** repo (one folder per lesson, one shared `index.html` homepage at the root — see the **🌐 AEF-Courses Deployment** section below). To let students/teachers get back to the full course catalogue, the cover slide has a small 🏠 emoji link at the **bottom left** — the mirror position of the Homework button at bottom right.

This is a **different button from the top-centre 🏠 Home button** described below — that one returns to *this lesson's own cover* (`goTo(0)`) and is hidden on the cover. This one takes you *out* of the lesson entirely, to the AEF-Courses catalogue, and only appears **on the cover**.

**Exact HTML — copy this every time:**
```html
<a href="../index.html" title="All AEF Courses"
   style="position:absolute;bottom:70px;left:32px;font-size:1.7rem;line-height:1;
          text-decoration:none;filter:drop-shadow(0 1px 3px rgba(0,0,0,.3));">🏠</a>
```

This `<a>` is a child of `.title-inner`, a sibling of the Homework button `<div>` (mirrored on the opposite side).

Every value — do not change:
- Position: `absolute; bottom:70px; left:32px` → **bottom left of the cover** (same vertical position as the Homework button, opposite horizontal side)
- Just the emoji `🏠` — no background, no border, no button chrome, no label text
- Font-size: `1.7rem`
- `href="../index.html"` — relative path up one level, to the AEF-Courses homepage (works because every lesson folder sits directly inside `AEF-Courses/`)
- `filter: drop-shadow(...)` keeps the emoji visible against any cover gradient colour

- ✅ `position:absolute` inside `.title-inner` — disappears with the cover slide naturally, cover only
- ✅ Bottom left corner, plain emoji, no button styling
- ✅ Always `href="../index.html"` (never a hardcoded full URL — relative path only)
- ❌ Never `position:fixed`
- ❌ Never add a background/border — this is not a button like Homework, just a clickable emoji
- ❌ Never place it on any slide other than the cover

### HOME BUTTON — TOP CENTRE, ALL SLIDES EXCEPT COVER (AEF4 7A standard)

A Home button is fixed at the top centre of the screen. It is **hidden on the cover** (slide 0) and **visible on all other slides**, letting the student return to the cover at any time.

**CSS — add to `<style>` block:**
```css
#homeBtn {
  position: fixed; top: 14px; left: 50%; transform: translateX(-50%); z-index: 1000;
  display: none;
  background: rgba(10,40,54,.88); color: #fff; border: none;
  width: 38px; height: 38px; border-radius: 50%; cursor: pointer;
  font-size: 1.1rem; align-items: center; justify-content: center;
  transition: background .2s; backdrop-filter: blur(4px);
}
#homeBtn:hover { background: rgba(20,96,122,.95); }
```

**HTML — place just after `<body>`, outside `#deck`:**
```html
<button id="homeBtn" onclick="goTo(0)">🏠</button>
```

**Visibility — toggle inside `goTo()` function:**
```js
document.getElementById('homeBtn').style.display = n === 0 ? 'none' : 'flex';
```

### NAV BAR — bottom of every slide including cover

```
◀ Prev  |  dots  |  1/22  |  Next ▶  |  💾 Save Notes  |  🖨️ Print Lesson
```
```css
#nav { position:fixed; bottom:0; left:0; right:0; height:52px;
       background:rgba(10,40,54,.96); z-index:500; }
```

---

### NOTES BEHAVIOUR ON THE COVER (from Notes System section)

- Notes do **not** auto-open on the cover
- When opened on the cover, the panel expands to full-page size (centred, `min/max-height: calc(100vh - 210px)`)
- `toggleNotes()` toggles the `.cover` class when on slide 0
- `goTo()` adds `.cover` if notes are open on slide 0; removes `.cover` on all other slides

---

### ❌ COMMON MISTAKES — DO NOT DO THESE

| Wrong | Correct |
|---|---|
| Merging "Conversational English · with teacher Nanda" into one line | Two separate HTML elements: `.title-label` then `.title-sub` |
| Notes button at bottom left | Notes button fixed at **top right** |
| Homework button fixed/centred/frosted glass | Homework button `position:absolute; bottom:70px; right:32px` **inside `.title-inner`**, dark solid `#1C2B3A`, `border-radius:10px` |
| 🏠 All-Courses link missing, or styled as a button/badge | Plain `🏠` emoji, `position:absolute; bottom:70px; left:32px`, no background/border, `href="../index.html"` |
| 🏠 All-Courses link placed on every slide (like a fixed button) | Only inside `.title-inner` on the **cover slide** — nowhere else |
| Any extra text, unit labels, or decorative elements | Only the 3 text lines — nothing else |
| Accent colour on random words | Accent on the most visually meaningful word(s) of the title |

---

## 📝 HOMEWORK COVER — MANDATORY STANDARD

The Homework Cover is the **first slide of the Homework section**. It is a full-screen dark slide — not a regular white exercise slide.

### WHAT GOES ON THE HOMEWORK COVER — COMPLETE LIST

1. Full-screen dark gradient background (can match lesson cover or use its own dark tone)
2. A small **"📝 Homework" badge** centred above the title — semi-transparent, pill-shaped
3. The **lesson title** centred below the badge — large, bold, with accent colour on key word(s)
4. Notes button — top right (same as always)
5. Nav bar — bottom of screen (same as always)

**That is all.** No "Conversational English / with teacher Nanda", no banner, no extra text, no Homework button.

### Exact HTML — copy this every time (from AEF4 2A):
```html
<div class="slide" id="hw-cover">
  <div class="title-inner">
    <div style="background:rgba(255,255,255,.1);border-radius:8px;padding:7px 22px;
                font-size:1rem;letter-spacing:.15em;color:rgba(255,255,255,.85);
                text-transform:uppercase;font-weight:600;margin-bottom:32px;">
      📝 Homework
    </div>
    <div class="title-main">[White words] <span class="title-accent">[Accent words]</span></div>
  </div>
</div>
```

### What it looks like:
```
[ dark gradient background — full screen ]

          📝 HOMEWORK           ← small semi-transparent pill badge

     [White part] Accent part   ← lesson title, large and bold, centred

[ nav bar at bottom ]
```

---

## 📝 Homework Exercise Standards — MANDATORY

> These rules apply to every slide inside the Homework section (after `hw-cover`). Established during AEF4-3A after repeated corrections — treat all of these as settled, not open questions.

### No book references — ever

Never show a book-specific exercise-letter label anywhere the student/teacher can see it: no "a", "b", "c", no "(a)", "Part a", "Exercise 3b", no audio track numbers (e.g. "3.2"), nothing that only makes sense if you're holding the physical book open. This applies to instructions, button labels, HTML comments intended as visible text, and audio labels alike.
- ✅ `<p class="instruction">Complete the phrasal verbs with a particle from the list.</p>`
- ❌ `<p class="instruction">a) Complete the phrasal verbs...</p>`
- ✅ `<p class="instruction">Listen and check.</p>`
- ❌ `<p class="instruction">🔊 3.2 Listen and check.</p>`

If you need to keep the book reference for your own tracking, put it in an HTML comment above the slide (`<!-- SB p.28, ex 6a -->`), never in visible text.

### Conversation / dialogue exercises — every speaker turn on its own line

> Added 2026-08-26 after AEF4-1B's HW2 (tag-question/auxiliary conversations) shipped with every speaker's turn run together in one paragraph (`A ... B ... A ...` all inline), making the exchange hard to read as a conversation.

Any exercise presented as a back-and-forth exchange between two (or more) speakers — homework or otherwise — must put **each speaker's turn on its own line**, never run multiple turns together in one flowing paragraph. This applies to every item in the exercise (not just the worked example, which already had this rule — see Example Presentation Standards above): `<b>A:</b> ...<br><b>B:</b> ...<br><b>A:</b> ...` etc., with a line break before each new speaker turn, matching the book's own layout.
- ✅ `<b>A:</b> I texted you last night, but you didn't reply.<br><b>B:</b> I <input> reply. I texted you right away.`
- ❌ `A I texted you last night, but you didn't reply. B I <input> reply. I texted you right away.` (all one line)

### Examples — numbered "1", never just labeled "(example)"

Every exercise's worked example is item **1**, not a separate "Eg"/"(example)" row outside the numbering. Real questions start at **2**. (This supersedes any older lesson using an "Eg" row before item 1 — new lessons and any slide you touch should use this numbered convention.) This rule is specific to the Homework section — for non-homework exercises, see **🟢 Example Presentation Standards** above, which requires verifying the book's own page instead.

- The example's number badge uses this exact style — a filled rounded-square badge, not the plain default `.circ-num` text style used for real questions (contrast matters: white bold text on a solid dark-green fill, not a light/blue text on white):
  ```html
  <span class="circ-num" style="background:#2E7D32;color:#fff;display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:6px;font-weight:800">1</span>
  ```
- The example still shows the fully worked/correct answer (not blank), tagged `(example)`, and is **not interactive** (no click/type target, `cursor:default`).
- For a **multiple-choice example**, show **all** the options, not just the correct one — mark the correct option and visually cross out/mute the incorrect one(s), so the student can see what was ruled out and why:
  ```html
  <span style="background:#fff;border:1.5px solid #2E7D32;border-radius:14px;padding:4px 14px;color:#1A5030;font-weight:800">word ✓</span>
  <span style="color:#aaa;text-decoration:line-through">other option</span>
  ```

### Multiple choice — options live inside the sentence, not listed after it

For "select the correct option" exercises, the options sit **inline in the blank position within the sentence** as clickable buttons/pills — never listed afterward with letter labels.
- ✅ `I had a terrible <button class="circ-opt">journey</button> <span class="circ-sep">/</span> <button class="circ-opt">trip</button> here — the flight was delayed.`
- ❌ `I had a terrible ___ here. (a) journey (b) trip (c) travel`

### Inline multiple-choice options never wrap mid-phrase

Multi-word `.circ-opt` options (e.g. "does the bus leave", "I've ever been seeing") sit inside a running sentence, so if the browser is free to line-wrap them, a long option can break across two lines — ugly and hard to read as a single option. `.circ-opt` must always render as one unbroken unit: `display:inline-block; white-space:nowrap;`. Check this any time `.circ-opt` (or an equivalent inline-choice class) is defined or copied into a new lesson file.

### One instruction paragraph per slide

Every homework slide has exactly **one** instruction paragraph. Never stack two `<p class="instruction">`/`<p class="inst-light">` tags on the same slide (e.g. a base instruction plus a separate "Tip:" paragraph) — merge any extra guidance into the single instruction paragraph instead. If a slide has two genuinely distinct exercises, split it into two slides (see the `slideIds`/`slideLabels` update rule above) rather than writing two instructions on one slide.

### Multi-select "select both if both are correct" grading

Some narrative-tense items in the book have two valid answers for the same sentence, and the exercise requires the student to select **both** (not either/or). Use independent per-button toggles (no sibling deselection, unlike the standard single-select "circle the correct option" pattern) plus a key object with a `'both'` sentinel meaning both options must be selected for that item to count correct:
- Grading is strict: an item only turns correct if **both** required buttons are selected — never mark it correct just because neither is selected, and never mark it correct with only one selected when the key calls for both.
- Instruction wording: "Select the correct verb form(s)." / "Select both if both are correct." — never "Circle..." (there's nothing to circle on a screen) and never "Check (✓) if both are correct" (mixes metaphors — the student clicks/selects, doesn't tick a box for this pattern).

### Accepting contractions and equivalent alternates

`checkSlide(sid)` supports **multiple** accepted alternates per input via a pipe-delimited `data-alt`, not just one:
```html
<input class="ans-input" data-ans="was raining" data-alt="had been raining|'d been raining" ...>
```
Use this whenever a full form and its contraction (`had` / `'d`, `was` / `'s`, etc.) are equally correct, or whenever the book's answer key lists more than one acceptable form for the same blank. The grading logic normalizes and checks the typed value against `data-ans` **and every value in `data-alt`**.

### "Why is this correct" explanation toggle

For dense grammar-completion exercises (e.g. a narrative-tenses cloze paragraph), add a toggle-able explanation panel below the exercise, off by default, using the same `.suggest-box` pattern as the Answer Key toggle:
- Button: `💡 Show Explanations` (toggles to hide)
- Panel: a short `<li>` per item, one sentence explaining *why* that tense/form is correct (not just restating the answer)
- Keep this separate from the "Answer Key" toggle — the explanation panel is about grammar reasoning, the answer key is about what to type

### Word-bank tiles that get "used up" — click tile, then click blank

When a word bank has a **fixed number of tiles that each get consumed exactly once** across the exercise (rather than a reusable option list), use the click-tile-then-click-blank interaction: click a tile to select it, click a blank to place the tile's value there (tile visually grays out / dashes its border as "used"), click a **filled** blank again to remove it and return that tile to available. This is the same "Word bank → fill blank" pattern (Case A) in the Wordbank Click Behavior section above — the key details worth restating here because they're easy to get wrong:
- Preserve whatever order the book/word list already has — never alphabetize or reorder tiles unless asked.
- If the exercise's worked example consumes one tile, that tile starts the slide already marked "used" (grayed out, not clickable) — don't make the student re-place it.
- Give each slide's check/reset functions unique names (see the JS function-naming warning above) — this exact pattern is where the naming collision bug actually happened.
- If two items can validly accept either of two tiles (e.g. two blanks share the same target vowel sound or are otherwise genuinely interchangeable per the answer key), grade both tiles as correct for both blanks via `data-alt` on the blank, rather than forcing one fixed pairing that isn't uniquely determined by the exercise's own logic.

### Blanks stay visually empty — no hint placeholders revealing the answer type

Don't put a part-of-speech or type hint inside a blank's placeholder (e.g. `placeholder="noun…"`, `placeholder="verb…"`). It gives away information the exercise is testing. Leave typed-answer inputs with an empty placeholder (or none) unless the book itself provides that hint as part of the exercise.

### HW slide numbering

- Homework slide titles are numbered sequentially in the `h2`: `HW1 — ...`, `HW2 — ...`, etc., matching their order in the deck (not the book's own numbering/lettering).
- If a slide is split into two, or a new one is inserted, **renumber every subsequent HW title and its `slideLabels` entry** in the same edit — don't leave a gap or a duplicate number.

---

## 🎨 Visual & CSS Conventions

> **Colour freedom — important!** You are free to choose whatever colour combination you find nice and fitting for each lesson. Every lesson should feel fresh and have its own personality. It's important that lessons are colourful — selection boxes, match pairs, chips, cards, banners, accents should all use colour intentionally and generously. Don't default to the same palette every time; pick combinations that work well together and suit the lesson's topic or mood. What must stay consistent is the **structure, layout, and font sizes** — the colours are entirely your creative choice.

### Background rules (critical)
- **Cover slide** → dark gradient background — colour chosen per lesson (e.g. dark blue, deep green, navy, burgundy…)
- **Homework cover slide** → dark background — can match the cover gradient or use its own dark tone
- **All other slides** → **white background** (`#ffffff` or `#fafafa`) — no dark backgrounds anywhere else

### Slide layout (non-cover slides)

> ⚠️ **MANDATORY — CHECK EVERY SLIDE BEFORE CONSIDERING A LESSON DONE.**
> Every non-cover, non-homework-cover slide **must** have both a `<h2>` title and instructions. This is not optional — it has been missed before (e.g. a listening slide shipped with no title). Before finishing any lesson, go slide by slide and confirm both are present, using the correct class and no inline font-size/weight overrides (sizes are fixed — see the Font sizes table below).

Every non-cover slide has this exact structure, top to bottom:
1. **Section header banner** — full-width coloured bar; contains **only** the emoji + section name, nothing else (e.g. `💬 Speaking`, `🎧 Listening`) — no subtitles, no exercise numbers, no extra text in the banner
2. **Slide title (`h2`)** — below the banner, describes the specific activity (e.g. "Exercise 3 – Gap Fill"). **Every non-cover slide needs one** — never skip straight from the banner to instructions/content.
3. **Instructions** — brief, adapted for one-on-one (see exercise rules). Use `class="instruction"` (bold, 1.08rem/700) or `class="inst-light"` (regular, 1.05rem/400) — never override their font-size or font-weight inline; if a slide needs a different look, it isn't a "instruction" line, style it separately.
4. **Exercise content** — inputs, checkboxes, chips, etc.
5. **Action buttons** — Check Answers / Suggested Answer + Reset, centred below the exercise

**Recognized exceptions** (no instruction line required, title still required):
- **Lead-in / discussion slides** — may use a `.discuss-label` (e.g. "💬 Share your thoughts") followed by a `.discuss-list` instead of a formal instruction paragraph
- **Lesson Review / recap slides** — a self-explanatory summary of what was covered; no instruction needed since there's nothing to instruct
- **Pure grammar reference/theory slides** (e.g. a tense-formation table) may use a one-line instruction like "Study how each tense is formed and used" rather than an exercise-style instruction

These are the *only* recognized exceptions. Any other slide missing a title or instructions is a bug — fix it, don't rationalize it as a new exception.

### Standard banner labels & CSS classes

> ⚠️ **BANNER RULE — READ THIS EVERY TIME:**
> The banner contains **only** the emoji + section name. That's it.
> **Nothing else is allowed in the banner** — no slide number, no exercise title, no subtitle, no topic description, no extra words.
>
> ✅ Correct: `🎧 Listening`
> ❌ Wrong: `🎧 Listening – Helping in an Emergency`
> ❌ Wrong: `🎧 Listening 2`
> ❌ Wrong: `📐 Grammar – Present Perfect`
>
> The exercise title goes in the `<h2>` below the banner — never inside the banner itself.

Use CSS classes for banner colours — **not inline styles** (except for one-off cases). Define these in the `<style>` block at the top of every lesson:

```css
.banner { width:100%; padding:13px 28px; font-size:1.1rem; font-weight:700;
          letter-spacing:.03em; display:flex; align-items:center; gap:10px;
          flex-shrink:0; color:#fff; }

.banner-bridge    { background: #3E7CB1; }
.banner-leadin    { background: #D35400; }
.banner-vocab     { background: #2A6B42; }
.banner-reading   { background: #2A6B42; }
.banner-listening { background: #0E7A8A; }
.banner-speaking  { background: #1E4D8C; }
.banner-grammar   { background: #4A1A6A; }
.banner-pron      { background: #0E7A8A; }
.banner-review    { background: #2E2A6B; }
.banner-hw        { background: #1C2B3A; }
```

> These are the **default** colours. Since colours are chosen per lesson, you can adjust these values — but always keep the class structure. Never use random inline `style="background:..."` on every banner individually.

#### Complete banner reference — text and class to use

| Section | HTML to use | Default colour |
|---|---|---|
| Bridge | `<div class="banner banner-bridge">🌉 Bridge</div>` | #3E7CB1 |
| Warm-Up | `<div class="banner banner-leadin">🎯 Warm-Up</div>` | #D35400 |
| Vocabulary | `<div class="banner banner-vocab">📚 Vocabulary</div>` | #2A6B42 |
| Reading | `<div class="banner banner-reading">📖 Reading</div>` | #2A6B42 |
| Listening | `<div class="banner banner-listening">🎧 Listening</div>` | #0E7A8A |
| Speaking | `<div class="banner banner-speaking">💬 Speaking</div>` | #1E4D8C |
| Grammar | `<div class="banner banner-grammar">📐 Grammar</div>` | #4A1A6A |
| Pronunciation | `<div class="banner banner-pron">🔊 Pronunciation</div>` | #0E7A8A |
| Lesson Review | `<div class="banner banner-review">⭐ Lesson Review</div>` | #2E2A6B |
| Homework slides | `<div class="banner banner-hw">📝 Homework</div>` | #1C2B3A |

If a slide combines two sections: `<div class="banner banner-listening">🎧 Listening & 💬 Speaking</div>` — keep it short.

#### Full slide header from AEF4 2A (copy this pattern every time):
```html
<div class="banner banner-grammar">📐 Grammar</div>
<div class="slide-main">
  <div class="content">
    <h2>Slide Title Here</h2>
    <p class="instruction">Bold instruction text here.</p>
    <p class="inst-light">Optional lighter instruction here.</p>
    <!-- exercise content -->
  </div>
</div>
```

### General visual
- **Font stack**: `'Segoe UI', system-ui, sans-serif` throughout
- **Body text on white slides**: dark `#1C2B3A`
- **Cards / exercise containers**: `#F4F8FA`, `border-radius: 10–12px`, subtle box-shadow, padding `1.5rem`
- **Slide min-height**: `100vh` (full viewport); content centred with flexbox
- **Navigation bar**: fixed at bottom, dark background `rgba(10,40,54,.96)`, `z-index: 500`
- **Correct / Incorrect feedback**: `#1A7A4A` green for correct, `#C4614A` red for wrong
- **Input fields (ans-input)**: inline, `border-bottom: 2px solid [accent]`, transparent background, `font-size: 1.05rem`, `font-weight: 700`, `width: 120px` default (but see Uniform Answer Blank Width rule — override per-exercise to fit the longest answer, same width for every blank in that exercise)

### Font sizes (match exactly — extracted from AEF4 7A)

> Sizes and weights below are fixed standards. Colours are per lesson choice.

> ⚠️ **Minimum font size floor — 1.05rem.** No lesson content text may ever be smaller than the instruction font size. Floor is **1.05rem** (the smaller of the two instruction variants — `.instruction` is 1.08rem, `.inst-light` is 1.05rem). Nothing a student reads or interacts with should go below this, even elements previously documented with a smaller "secondary" size — the table below already reflects the corrected values. This applies to: instructions, exercise sentences/questions, answer options and chips, table/reference text, story or reading text, notes/labels that convey lesson information, placed/typed answers, word-bank tiles, classify chips, circle/multiple-choice options, matching-pair items, placed answer tags, audio labels, glossary notes, book-placeholder notes, story-text placeholders, suggested-answer boxes.
>
> **Exempt from the floor** (governed by their own already-fixed standards instead):
> - Fixed navigation/UI chrome — nav bar buttons, dots, slide counter, Notes button, notes toolbar buttons, notes textarea, Home button, Save Notes / Print Lesson buttons (these are app controls, not reading content; several are already pinned elsewhere, e.g. the Homework button's `.95rem`)
> - Icon/number-only badges — `.circ-num`, `.example-badge`, small emoji/checkmark glyphs (single digits or icons, not prose)
> - Print-only CSS (`@media print` block: page header, `.lesson-link-print`, `.slide-notes-print`) and the Save Notes printable summary page — export/print artifacts with their own documented sizes
> - Cover / Homework Cover mandatory pinned elements (title lines, homework badge, 🏠 all-courses link) — governed by their own "MANDATORY STANDARD" sections

#### Cover slide
| Element | Size | Weight | Notes |
|---|---|---|---|
| "CONVERSATIONAL ENGLISH" label | `1.1rem` | 500 | uppercase, letter-spacing .18em |
| "with teacher Nanda" sub | `1.15rem` | 400 | |
| Lesson title (`.title-main`) | `3.4rem` | 900 | line-height 1.1 |
| Accent word (`.title-accent`) | inherits | — | colour chosen per lesson |

#### Content slides (white background)
| Element | Size | Weight | Notes |
|---|---|---|---|
| Section banner (`.banner`) | `1.1rem` | 700 | letter-spacing .03em; colour chosen per lesson |
| Slide title (`h2`) | `1.85rem` | 800 | dark colour chosen per lesson |
| Bold instruction (`.instruction`) | `1.08rem` | 700 | line-height 1.7 |
| Light instruction (`.inst-light`) | `1.05rem` | 400 | |
| Discussion question (`.discuss-label`) | `1.08rem` | 700 | line-height 1.7 |

#### Exercise content
| Element | Size | Weight | Notes |
|---|---|---|---|
| Exercise rows (`.ex-row`) | `1.06rem` | 400 | line-height 1.7 |
| Answer inputs (`.ans-input`) | `1.05rem` | 700 | |
| Grammar theory text | `1.06rem` | 400 | line-height 1.7 |
| Grammar theory `h3` | `1.05rem` | 800 | |
| Grammar table cells | `1.05rem` | 400 | |
| Speaking card question | `1.12rem` | 400 | line-height 1.5 |
| Speaking card example | `1.05rem` | 400 | italic |
| Listening questions | `1.06rem` | 400 | |
| Listening answers (revealed) | `1.05rem` | 400 | italic |
| Article / reading text | `1.02rem` | 400 | line-height 1.65 |
| Match problem text | `1.05rem` | 400 | line-height 1.6 |
| Dialogue text | `1.06rem` | 400 | line-height 1.9 |
| Tick/checkbox rows | `1.06rem` | 400 | line-height 1.5 |
| Vocab chips | `1.05rem` | 700 | |
| Quote banner | `1.1rem` | 400 | italic |

#### UI elements
| Element | Size |
|---|---|
| Nav bar buttons | `.95rem` |
| Slide counter | `.9rem` |
| Notes button | `.92rem` |
| Notes toolbar buttons | `.85rem` |
| Notes textarea | `1rem` (line-height 1.55) |
| Audio info title | `1.05rem` |
| Audio info sub | `.9rem` |

---

## 🎓 CELTA-Style Teaching Sequence (Meaning → Form → Pronunciation)

> Applies whenever a slide (or sequence of slides) **introduces or analyzes** a new grammar point or vocabulary set — not to every exercise. Controlled practice exercises later in the section don't need to re-derive meaning/form/pronunciation, just drill what was already established.

### MFP / MPF order

When presenting new grammar or vocabulary, don't jump straight to "here's the rule, now practice it." Follow the CELTA-standard sequence:

1. **Meaning (M)** — establish what the language actually communicates *before* naming it or drilling its form. Use a clear context (a short story, a situation, an image, a timeline) and **Concept Checking Questions (CCQs)** — simple yes/no or either/or questions that check understanding without relying on grammatical terminology.
   - Example (past perfect): *"When I arrived, she had already left." → CCQ: "Did she leave before or after I arrived?" (before) "Were we in the room at the same time?" (no)*
2. **Form (F)** — how it's built: word order, auxiliary verbs, spelling changes, affixes. Show the structure explicitly (e.g. `had + past participle`), highlight the key piece with color/bold, and give 2–3 more example sentences in the same structure.
3. **Pronunciation (P)** — sentence stress, weak forms, contractions, linking (e.g. `had` often weakens to /əd/ or `'d` in connected speech). Give the student a model to notice/repeat.

**Use M-P-F instead of M-F-P** when pronunciation is the main teaching challenge for that point (e.g. weak forms of auxiliary verbs, contractions, linking) — the sound pattern matters more to get right early than a written breakdown of the form.

Order **within a language-focus mini-sequence**: Meaning slide(s) → Form slide(s) → Pronunciation slide(s) → **Controlled practice** (the exercises already documented elsewhere in this file — gap fill, multiple choice, etc., where there's one right answer) → **Freer/personalized practice** (open speaking or writing where the student uses the language about their own life — see the Speaking Activities section below). This mirrors CELTA's **ESA shape** (Engage → Study → Activate): Engage = lead-in/warm-up, Study = the M-F-P + controlled practice, Activate = freer/personalized production.

### Concept Checking Questions (CCQ) slide

A short block of 2–4 yes/no or either/or questions about the example context, used to verify the student has understood the *meaning* before moving to form. Doesn't need a Check/Reset button — this is a spoken/discussed exchange, not a graded exercise. Simple pattern:

```html
<div class="ccq-box">
  <p class="ccq-label">💭 Check your understanding</p>
  <ul class="ccq-list">
    <li>Did she leave before or after I arrived? <em>(before)</em></li>
    <li>Were we in the room at the same time? <em>(no)</em></li>
  </ul>
</div>
```
Keep the answer in a muted `<em>` so it doesn't visually dominate — the point is for the student to answer out loud first.

### Timeline diagrams (tense meaning)

For any tense/aspect point (especially perfect tenses, narrative tenses, future forms), a horizontal timeline visual makes meaning concrete faster than an explanation. Simple CSS-only pattern — a horizontal line with positioned dots/labels, no JS needed:

```html
<div class="timeline">
  <div class="tl-line"></div>
  <div class="tl-point" style="left:15%"><span class="tl-dot"></span><span class="tl-label">she left</span></div>
  <div class="tl-point" style="left:55%"><span class="tl-dot tl-now"></span><span class="tl-label">I arrived</span></div>
  <div class="tl-point" style="left:90%"><span class="tl-label">now</span></div>
</div>
```
```css
.timeline{position:relative;height:70px;margin:24px 20px}
.tl-line{position:absolute;top:30px;left:0;right:0;height:2px;background:#C8D8E8}
.tl-point{position:absolute;top:0;transform:translateX(-50%);text-align:center}
.tl-dot{display:block;width:12px;height:12px;border-radius:50%;background:#1E4D8C;margin:22px auto 6px}
.tl-dot.tl-now{background:#2A6B42}
.tl-label{font-size:.85rem;color:#1C2B3A;white-space:nowrap}
```
Use an arrow between two points (e.g. `←` between two dots) to show sequence when one event clearly precedes another.

### Freer/personalized practice — always end a grammar or vocab sequence with one

After controlled practice, add at least one open-ended slide where the student produces the target language about **their own life/opinions** — this is the "Activate" stage and shouldn't be skipped. Use the existing **Open text box** exercise type (💡 Suggested Answer + Reset), or one of the Speaking Activities / gamified prompts below (dice roll, spin wheel) to make it feel less like a drill.

---

## 🗣 Speaking Activities & Personalization — be creative here

Speaking slides are where a one-on-one lesson comes alive — don't default to a plain "discuss this" prompt every time. Mix in the randomizer mechanics below (dice, wheel) to make freer-practice and warm-up moments feel like an activity, not a worksheet. All of these are self-contained (no external libraries, no `localStorage`), following the same click-driven interaction style as the rest of the deck.

### 🎲 Dice Roller — random speaking prompt picker

Roll a die to land on one of six speaking questions/prompts. Great for warm-ups, freer practice after a grammar point, or a review closer.

```html
<div class="dice-box" id="dice-taxi">
  <div class="die-face" id="dice-taxi-face">⚀</div>
  <button class="btn-check" onclick="rollDie('dice-taxi')">🎲 Roll the Die</button>
  <p class="dice-prompt" id="dice-taxi-prompt"></p>
</div>
```
```js
var diceFaces = ['⚀','⚁','⚂','⚃','⚄','⚅'];
var dicePrompts = {
  'dice-taxi': {
    1: "Tell me about a trip that went wrong.",
    2: "What's the longest flight you've ever taken?",
    3: "Describe your ideal vacation.",
    4: "Have you ever missed a flight? What happened?",
    5: "What do you always pack, no matter where you're going?",
    6: "Talk about a place you'd love to visit and why."
  }
};
function rollDie(id){
  var face = document.getElementById(id+'-face');
  var promptEl = document.getElementById(id+'-prompt');
  var n = 0, rolls = 0;
  var spin = setInterval(function(){
    n = Math.floor(Math.random()*6);
    face.textContent = diceFaces[n];
    rolls++;
    if (rolls > 10){
      clearInterval(spin);
      promptEl.textContent = dicePrompts[id][n+1];
    }
  }, 80);
}
```
- Each lesson's dice prompts live in their own `dicePrompts['dice-{topic}']` object keyed 1–6 — one die per slide, unique id.
- Die face size ~3.5rem, centered; roll animation is just rapid random face-swapping for ~800ms before landing.
- No Check/Reset needed — it's a prompt generator, not a graded exercise.

### 🎡 Spin the Wheel — expanded use cases

Already documented under Special Exercise Types for warm-ups/topic-picking — also reach for it for:
- **Verb conjugation drills**: wheel of verbs, student conjugates whichever one it lands on into the tense just taught
- **Question generator**: wheel of question starters ("Have you ever...", "What would you do if...") for freer speaking practice
- **Vocabulary review**: wheel of the lesson's new words, student defines/uses whichever one it lands on

### 📖 MadLibs-style personalization

A fun bridge between controlled and freer practice: student fills in blanks by word type (noun, verb, place, adjective...) **without seeing the story**, then reveals the finished (often funny) story with their words dropped in. Reuses the existing free-text input pattern; add a `revealMadLib(id)` function that reads each input's value and substitutes it into a template string.

```html
<div class="madlib-inputs">
  <input class="ans-input" id="ml1-place" placeholder="a place">
  <input class="ans-input" id="ml1-verb"  placeholder="a verb (past tense)">
  <input class="ans-input" id="ml1-adj"   placeholder="an adjective">
</div>
<button class="btn-check" onclick="revealMadLib('ml1')">✨ Reveal the Story</button>
<p class="madlib-result" id="ml1-result"></p>
```
```js
function revealMadLib(id){
  var place = document.getElementById(id+'-place').value || '___';
  var verb  = document.getElementById(id+'-verb').value  || '___';
  var adj   = document.getElementById(id+'-adj').value   || '___';
  document.getElementById(id+'-result').textContent =
    'Last summer, I went to ' + place + ' and ' + verb + ' the whole time. It was ' + adj + '!';
}
```
Good use: end of a narrative-tenses grammar section, or a vocabulary section, as playful freer practice.

### 🎯 Bingo — vocabulary review

A grid (4×4 or 5×5) of the lesson's target words/phrases; click a cell to mark it (reuses the existing checkbox-toggle pattern — `toggleCheck(n)` equivalent). No win-check needed; the teacher calls out definitions/example sentences and the student marks the word they hear. Good five-minute warm-down or review activity for a vocab-heavy lesson.

### 🔤 Word Scramble — vocabulary practice

Show a word's letters scrambled/spaced out, student types the unscrambled word into a normal `.ans-input` checked against `data-ans` — visually just a scrambled-letters header above a standard gap-fill input, no new interaction pattern needed.

### 🔓 Virtual Breakout — gamified review closer

A fun way to structure a lesson review: 3–5 "locked" boxes, each unlocked by typing the correct answer/code from a review question into an input (checked against `data-code`, same normalization as `checkSlide`). Unlocking all boxes reveals a congratulatory message/image. Best as an optional review/wrap-up slide, not a core requirement.

```html
<div class="lock-row">
  <div class="lock" data-code="paris">
    <span class="lock-icon">🔒</span>
    <input class="lock-input">
  </div>
</div>
```
```js
function checkLock(lockEl){
  var input = lockEl.querySelector('.lock-input');
  var icon  = lockEl.querySelector('.lock-icon');
  if (norm(input.value) === lockEl.dataset.code){
    icon.textContent = '🔓';
    lockEl.classList.add('unlocked');
  }
}
```
> Note the `.lock-input` above has no `placeholder` — see "No placeholder text in student answer boxes" above, which applies here too.

### What we're *not* adopting from Flippity — and why

Some Flippity activity types are built for classrooms/multiple students and don't fit a one-on-one tutoring format — skip these rather than force-fitting them: **Quiz Show** (team scoring), **Leaderboard**, **Badge Tracker**, **Tournament Bracket**, **Typing Test** (not a speaking/comprehension skill we're teaching), **Color By Number** (not age/level appropriate for adult learners). If a future lesson genuinely calls for a group/team format, revisit this list rather than defaulting to "not applicable."

---

## 🌉 Bridge Slide — connecting to the previous lesson (always slide 2, before the Warm-Up)

> Added after AEF4-1B's "Case Files: Ask About It!" slide worked well as a connector between lessons.

Every lesson now opens with a short **Bridge slide**, positioned right after the Cover and before the Warm-Up. Its job is to re-activate a skill or grammar point from the **previous** lesson through a quick game or communicative task — **never through an explicit statement that this is reviewing the last lesson.** The connection should be felt through the activity itself, not announced to the student.

**Design pattern:**

- Build it as a light game or short interactive task (case-file-style cards, prompts, a quick production exercise) themed to fit the **current** lesson's topic, but built entirely from the skill/grammar taught in the **previous** lesson.
- Keep it fast — 2–4 items, one clear task, no more than a couple of minutes of class time. This is a warm connector, not a full review.
- It's fine (and often good) to end with a short, low-key `gram-note` that plants a seed for today's new grammar — but keep it brief and natural, not a lecture.
- Never use words like "review," "last lesson," or "recap" in anything student-facing (title, instruction, banner). Let the activity itself carry the connection.

### The Bridge is communicative, never a graded grammar drill

**A Bridge slide must be a speaking/production task, not a fill-in-the-blank or multiple-choice grammar exercise with a single graded correct answer.** The whole point is for the student to *use* the target skill to communicate — ask a real question, react, make something up, describe something — not to prove they can conjugate it correctly on a form.

This means, for the Bridge specifically:

- **No `checkSlide`/`checkCircSlide`-style "Check Answers" button testing grammatical accuracy.** That mechanic belongs to the lesson's actual Grammar practice slides, not the Bridge.
- **Open, ungraded production fields are fine and often best** — e.g. a blank `.ans-input` with no `data-ans`, existing only to give the student something to jot down while they speak their answer out loud. Nothing gets marked right or wrong.
- **Favor prompts that require the student to generate their own language**: ask a question about a scenario, react to a statement, describe something invented, make a guess — not complete a sentence with the "correct" verb form.
- The reference implementation (AEF4-1B's "Case Files: Ask About It!") is the model to copy: three short scenario cards, each ending in an open "ask a question about it" field with no grading — the student produces real questions using last lesson's skill, live, out loud.

### Connect through learning points, not through topic

The single most common way to get this wrong: rebuilding the **previous lesson's topic** in new clothes (e.g. another doctor/illness quiz after a "Doctor, doctor!" lesson). That is not a bridge — it's just the old lesson again with a new theme label, and it does nothing to connect to *today's* lesson.

A Bridge slide must instead identify the actual **learning points** taught last time — the specific, nameable things the student practiced — and re-exercise those, dressed in whatever scenario fits *today's* topic. Learning points typically fall into one of these buckets:

- **Grammar / structure** (e.g. present perfect simple, question formation, auxiliary-verb functions)
- **Key functional phrases** (e.g. phrases for describing a problem, asking for clarification, giving advice)
- **Vocabulary set** (e.g. illness/injury words, personality adjectives) — used as *language material* inside a new scenario, not as the scenario's subject
- **Pronunciation focus** (e.g. word stress, a specific sound contrast)

**How to build it:**

1. List out the previous lesson's actual learning points (check the lesson file / manual notes — don't guess).
2. Pick one or two of them — not the topic — as the thing being reactivated.
3. Invent a short task or game for *today's* topic/theme that requires using that grammar, those phrases, that pronunciation pattern, or that vocabulary as a tool — the old topic itself should not reappear.

**Worked example — wrong vs. right**, for a Bridge slide following a "Doctor, doctor!" lesson (learning points: present perfect simple, phrases for describing symptoms/problems, illness vocabulary, word stress) feeding into a "1 & 2 Review" or any unrelated next lesson:

- ❌ **Wrong** (topic-based): a "myth or fact" quiz about burns, nosebleeds, and frostbite. This just re-runs the old lesson's illness/first-aid topic — exactly what this rule forbids.
- ✅ **Right** (learning-point-based): a quick "Have you ever…?" mingling task where the student forms present-perfect questions about experiences unrelated to illness (travel, food, sport), or a rapid-fire task where the student must use last lesson's "describing a problem" phrases ("I've got a…", "It hurts when…") to complain about something totally different (a noisy neighbor, a broken phone) — the grammar/phrases are reactivated, the topic is not.

If it's not obvious which learning points to reactivate, ask: "if I stripped away the theme, what specific language skill was the student practicing?" Bridge that skill forward — never the theme.

**When bridging into a lesson that follows more than one previous lesson** (e.g. a Review lesson after 1A + 1B + 2A), don't limit the Bridge to only the single most-recent lesson's learning point — pull one distinct learning point from each of the recent lessons being connected, so the Bridge reactivates a genuine spread, not just the last thing taught.

### When multiple cards/items are used, mix the task types

Don't give every card the same instruction (e.g. "ask a question about it" three times in a row). Each card should exercise a **different** learning point through a **different kind of task**, so the Bridge feels varied and communicative rather than repetitive drilling of one mechanic. For example, across three cards pulling from three different lessons:

- Card 1 (question-formation skill): "Ask a polite, indirect question about it."
- Card 2 (reacting skill): "React to it! (Same as you? Different? Surprised?)"
- Card 3 (a grammar contrast, e.g. present simple vs. present perfect continuous): "Tell me something you usually do, and something you've been doing a lot recently."

All three stay open-ended and ungraded (per the rule above), but the *shape* of what the student produces changes card to card — a question, a reaction, a pair of personal statements — which is what makes it feel like a real mixed conversation rather than one repeated exercise pattern.

**Banner — add to the approved list:**

| Section | HTML to use | Default colour |
|---|---|---|
| Bridge | `<div class="banner banner-bridge">🌉 Bridge</div>` | #3E7CB1 |

Add `.banner-bridge { background: #3E7CB1; }` to the banner CSS block alongside the others (adjust the shade per lesson palette if needed, same as every other banner colour).

> Reference implementation: **AEF4-1B**, "Case Files: Ask About It!" — three mystery statements, students produce questions using last lesson's auxiliary-verb-question skill, closing with a short gram-note that quietly sets up today's new reacting-with-auxiliary-verbs grammar.

---

## 🎬 Warm-Up Standards — be creative, never default to a quote

The Warm-Up is the first thing the student sees, so it must earn its place. A book quote followed by three discussion questions is the **fallback, not the format** — it should never be the whole warm-up.

**Every warm-up must include at least one active, interactive element** from the list below, chosen to fit the lesson's topic:

- **🧠 Myth or Fact?** — 4–6 surprising statements about the topic; student clicks Myth/Fact, graded green/red, then a 🔑 reveal explaining the real story with a memorable detail.
- **🔢 Guess the number / year** — surprising statistics or dates hidden behind Reveal buttons; the student guesses out loud first.
- **😅 What's wrong with this picture?** — a meme-style or staged image placeholder containing several deliberate mistakes; the student spots and describes them.
- **📖 Funny short story or anecdote** — a 4–6 line true or true-ish story with a twist, followed by reaction questions.
- **🗳️ Would you rather…** — two awkward options; the student picks one and justifies it.
- **🎲 Dice roll / spin the wheel** — a random personal question to open the lesson (see Speaking Activities).

**Rules for warm-ups:**

- **Point it at the target language.** Wherever possible the warm-up should make the student *use* (or at least hear) the lesson's grammar or vocabulary before it's formally taught — e.g., a "how long has X been around?" guessing game before a present perfect lesson.
- **Facts must be true and checkable.** Prefer well-established facts; hedge where a figure is an estimate ("it's commonly estimated that…"). Never invent a statistic to make a warm-up sound good.
- **Keep the book's quote if there is one** — but demote it: put it *after* the interactive element, as a lead-in to the personal questions, not as the opening.
- **Images are placeholders**, described specifically enough that the teacher knows exactly what to source (see the image placeholder standard).
- **Vary the format between lessons.** Don't use Myth or Fact three lessons in a row — rotate through the list so the student never knows what's coming.

> Reference implementations: **AEF4 5A** (survival Myth or Fact), **AEF3 2B** (how-long-have-they-been-around guessing game, which rehearses the target grammar), **AEF3 3A** (driving Myth or Fact + what's-wrong-with-this-picture).

---

## 🗂 Typical Lesson Slide Order

Most lessons follow this sequence (not all sections appear in every lesson):

1. **Cover** — "Conversational English / with teacher Nanda" + Lesson Title only (see rules above)
2. **Bridge** — short game/communicative task connecting to the previous lesson's skill (see 🌉 Bridge Slide standards above) — always before the Warm-Up
3. **Lead-in / Warm-Up** — warm-up activity (topic activation, image discussion, spin the wheel, dice-roll prompt)
4. **Vocabulary** — word list, matching, or labelling exercise (consider a Bingo or Word Scramble review at the end)
5. **Reading** — passage + comprehension exercises (true/false, multiple choice, gap fill)
6. **Listening** — audio placeholder + comprehension task
7. **Speaking** — discussion prompts or role-play adapted for one-on-one — a good spot for a dice-roller or spin-wheel prompt generator
8. **Grammar** — follow the **Meaning → Form → Pronunciation** sequence above: context + CCQs → form breakdown → pronunciation focus → controlled practice → freer/personalized practice (MadLibs or open speaking)
9. **Pronunciation** (when applicable) — pronunciation focus exercise
10. **Writing** (when applicable) — guided writing prompt
11. **Homework** — homework cover + task slides
12. **Review / Wrap-up** — optional recap slide; a Virtual Breakout or dice-driven review is a good option here instead of a plain summary

Use this order as the default; deviate only if the book's lesson flow demands it.

---

## 🏷 Slide ID Naming Conventions

- Cover slide: `id="s1"`
- Lesson-section slides: short, descriptive, lowercase, hyphens only — no underscores or camelCase. Real practice favors brief topic-based ids over a strict numbered scheme, e.g.:
  - `id="s-vocab1"`, `id="s-vocab2"`, `id="s-vocab3"`
  - `id="s-read"`
  - `id="s-listen1"`, `id="s-listen2"`
  - `id="s-speak1"`, `id="s-speak2"`
  - `id="s-gram"`, `id="s-gram2"`, `id="s-gram-nar-meaning"`, `id="s-gram-nar-form"` (compound topic suffixes are fine when there are several closely related grammar slides)
  - `id="s-pron"`, `id="s-pron-anec"`
  - `id="s-spin"` (Spin the Wheel)
  - `id="s-review"` (Lesson Review)
- Homework section: cover is `id="hw-cover"`; task slides use `id="hw-{topic}"` matching the exercise, not a strict sequential number — the sequential numbering lives in the visible `h2` title (`HW1`, `HW2`...), not the id. e.g. `id="hw-voc1"`, `id="hw-pv"` (phrasal verbs), `id="hw-gr1"`, `id="hw-pron"`, `id="hw-wr"` (writing).
- Whatever id you choose, it must be added to **both** `slideIds` and `slideLabels` at the matching DOM position (see the Slide Navigation Data section above) — the id itself just needs to be unique and readable, not follow a rigid numeric pattern.

---

## 💾 Backup Convention

- Create backups **frequently** while building a lesson — don't wait until the end, and always before any risky/destructive change (deleting a slide, large restructuring, etc.)
- Backups are a flat file saved **directly inside the lesson's own folder** (e.g. `AEF-Courses/AEF4-3A/`) — there is no `backups/` subfolder; this matches actual practice across every lesson.
- Filename format: `index_backup_YYYYMMDD_HHMM.html`
  - Example: `index_backup_20260706_1039.html`
- Good moments to back up: after finishing each section, after any major fix, before attempting complex changes, and whenever asked to "save a backup"
- Backup files are excluded from git via `.gitignore` (see AEF-Courses Deployment section) — they're a local safety net only, not meant to be committed
- **Retention cap — max 2 backups per lesson at any time.** Before saving a new backup, check how many `index_backup_*.html` files already exist in that lesson's folder. If there are already 3 or more, delete the older ones first, keeping only the single most recent existing backup, then save the new one (so at most 2 remain after the save). Never let backups pile up unchecked — a growing pile of old backups is clutter, not safety.

---

## 🇺🇸 American English Spelling

**All lessons must use American English spelling throughout — no exceptions.**

This applies to every piece of text in the lesson: instructions, exercise content, labels, buttons, placeholders, grammar explanations, and any other visible text.

Common differences to watch:
- **-ize** not -ise (organize, recognize, realize)
- **-or** not -our (color, behavior, neighbor, humor)
- **-er** not -re (center, theater)
- **-ense** not -ence (defense, offense, license)
- **program** not programme · **fulfill** not fulfil · **check** not cheque · **traveled** not travelled

Always double-check spelling before considering a lesson complete.

---

## 📌 Changing This File

**This file is the single source of truth. No other standards document exists or should be created.** If a correction made during a lesson build reveals a new standing rule (or a fix to an existing one), it does not get written into a separate patch file — it gets proposed to the teacher first, in plain language, and only added directly to this file once the teacher has explicitly approved the exact wording. Never edit or add a rule here without that confirmation first.

---

## ✅ Pre-Launch Checklist

Before considering a lesson complete, verify:

- [ ] Every non-cover slide has a `<h2>` title and instructions (`.instruction` or `.inst-light`, no inline font-size/weight overrides) — except the recognized exceptions (lead-in discussion, review/recap, pure grammar reference slides)
- [ ] All exercises have **Check Answers** or **Suggested Answer** buttons (never both on the same exercise)
- [ ] Check Answers: empty → orange, correct → green, wrong → red; **no answer ever revealed**
- [ ] All **Reset** buttons clear inputs and feedback correctly
- [ ] `data-ans` (and `data-alt` where needed) set on every input
- [ ] No raw audio filenames visible — all audio uses native `<audio controls>` in styled pill wrapper, with nothing else inside the audio container (no glued-on caption/label)
- [ ] All image spots have styled placeholder `<div>`s
- [ ] Navigation bar shows correct slide count and dots
- [ ] Notes system: opens/closes on all slides, cover behaviour correct; toolbar has B/U + 4 highlight colors (yellow/green/pink/blue) + ✕ remove-highlight, same-color click toggles off; Notes button label toggles "📝 Notes" ↔ "✕ Close"; dragging the panel then closing and reopening it always returns it to its default position (see 📒 Notes System → Draggable panel always resets)
- [ ] Nav bar shows **both** 💾 Save Notes (`#2E2A6B`) and 🖨️ Print Lesson (`#0E5A8A`) as two distinct buttons — neither replaces the other
- [ ] "💾 Save Notes" button: opens a printable summary page of every slide with notes (or alerts "No notes to save yet!" if none)
- [ ] "🖨️ Print Lesson" button: all slides print one per page in original layout; cover page gets `.lesson-link-print` banner (lesson title + link); every other slide gets small grey `::before` page header; teacher's notes print at the bottom of relevant pages in light-blue block
- [ ] No lesson content text is smaller than the **1.05rem floor** (instructions, exercise text, options/chips, tables, reading text, notes/labels, answers) — except exempt UI chrome, icon/number badges, print-only CSS, and cover/homework-cover mandatory pinned elements
- [ ] No `placeholder="..."` text inside any student-facing typed-answer `<input>`/`<textarea>` — guidance lives only in the instruction line (`#notesTA`'s notes placeholder is exempt)
- [ ] Every typed-answer blank within the same exercise shares one uniform width, sized to the longest expected answer
- [ ] Wordbank exercises use the correct click pattern — Case A (click-tile-to-place) if every word is used unchanged, Case B (typed blank + click-to-mark-used) if any word changes form
- [ ] Non-homework example numbering verified against the actual book page (never assumed); example answer words use the green highlight chip, not blue italic/underline; example placement follows the odd/even centering logic (see 🟢 Example Presentation Standards)
- [ ] Arrow keys don't trigger navigation while typing in inputs or notes
- [ ] A Bridge slide (🌉 banner) sits right after the Cover and before the Warm-Up, connecting to the previous lesson's skill through a short game/task — never stated explicitly as "review" (see 🌉 Bridge Slide standards)
- [ ] Warm-Up includes at least one active/interactive element (Myth or Fact, guess-the-number, what's-wrong-with-this-picture, story, would-you-rather, dice/wheel) — not just a quote + questions; and the format differs from the previous lesson (see 🎬 Warm-Up Standards)
- [ ] Spin the Wheel redraws on slide entry (if present)
- [ ] Multi-column exercises follow the top-to-bottom, left-to-right column order rule
- [ ] Homework slides: no book-reference letters/track numbers anywhere visible (see Homework Exercise Standards)
- [ ] Homework slides: every example is numbered "1" with the green rounded badge, not a separate "Eg" row
- [ ] Homework slides: exactly one instruction paragraph per slide
- [ ] Homework slides: multiple-choice options sit inline in the sentence, never listed after with letters
- [ ] `slideIds` / `slideLabels` arrays match the DOM `.slide` order exactly, same length, no duplicates — re-verify after any slide add/remove/split
- [ ] No two functions in the file share the same name (check/reset functions especially) — grep before naming a new one
- [ ] All text uses **American English spelling** throughout
- [ ] Backup saved directly inside the lesson's own folder (no `backups/` subfolder) with date-time filename `index_backup_YYYYMMDD_HHMM.html`
- [ ] Lesson folder lives inside `AEF-Courses/`, with no leftover nested `.git` folder
- [ ] 🏠 All-Courses link present on the cover (bottom left, `href="../index.html"`) — see standard above
- [ ] Saved-PDF link (`[LESSON_URL]` in `printAll()` and the cover banner) uses `https://teacher-nanda.github.io/AEF-Courses/[FOLDER]/index.html`
- [ ] Lesson added as a card in `AEF-Courses/index.html`'s `courses` list
- [ ] Lesson URL added to the **🔗 Live Lesson URLs** table above

---

## 💡 How to Use This File

### Starting a new lesson
Send this file and include the following information:

```
Standards file: [this file]
Lesson: AEF[level] [unit][lesson]  (e.g. AEF4 7B)
Sections to include: [list sections, e.g. Lead-in, Reading, Grammar, Homework]
Book exercises: [paste or describe each exercise with its instructions and answer key]
Audio files: [list filenames, e.g. track_4_07.mp3]
Images: [describe what each image shows so placeholders can be labelled correctly]
Live URL (if known): https://aef4-7b.netlify.app/
```

Claude will build the lesson matching all standards above exactly, without asking for clarification on conventions already documented here — including applying the Meaning → Form → Pronunciation sequence to any new grammar/vocab point, and choosing a fitting creative/gamified activity (dice roll, spin wheel, MadLibs, bingo, breakout...) from the Speaking Activities section where it fits, without being asked each time.

The teacher does not need to repeat any of the points below in their prompt — they are permanent standing behavior for every new lesson:

- **Check every single rule in this file** — not just the sections that seem obviously relevant to the lesson at hand. Go through structure, banners, column-order, homework rules, cover/homework-cover spec, notes system, print/PDF setup, backups, and American English spelling before considering the lesson done.
- **Be creative** — don't default to the plainest possible exercise type. Reach for the Speaking Activities / gamified mechanics (dice, wheel, MadLibs, bingo, breakout, timelines, CCQs) wherever they fit, without being asked. **This applies to the Warm-Up above all — see 🎬 Warm-Up Standards.**
- **When in doubt, check a previous lesson before asking the teacher** — AEF4-3A is the reference implementation; if a convention isn't crystal clear from this file, see how an existing lesson actually handled that same situation and match it, rather than guessing or interrupting with a question. **Never invent a new "standard" by copying a pattern from a different lesson file without first verifying it against the current lesson's own book page** — this has caused real errors (see 🟢 Example Presentation Standards).
- **Leave clearly labeled placeholders for any image or audio file not yet provided** — never invent content or silently skip a media slot. A styled placeholder `<div>` (images) or asking the teacher for the expected filename (audio) is correct; leaving the spot blank or inventing a fake file is not.
- **Copy from the book as much as possible** — exercise wording, sentence order, and the answer key should match the textbook exactly. Only the interaction mechanic changes to fit an on-screen click/type format (see Exercise Type Reference) — never paraphrase or invent book content.
- **Verify before calling the lesson done**: JS syntax check (`node --check` on the extracted `<script>`), an HTML tag-balance audit (global and per-slide), a `slideIds`/`slideLabels`/DOM order sync check, a functional sweep of every exercise (jsdom or equivalent), and a timestamped backup saved to the lesson's own folder.
- **Never edit this standards file itself without asking first** — propose the exact rule/wording change to the teacher and wait for approval before writing to this file. This file is the single source of truth; no other standards document should ever be created.
