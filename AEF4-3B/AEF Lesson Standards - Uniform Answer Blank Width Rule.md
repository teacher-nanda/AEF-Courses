# 🔎 New Standard — Uniform Width for Typed Answer Blanks

This adds a new rule to `AEF Lesson Standards.md` (the master file is read-only, so this is tracked separately — fold it in the next time the master file is edited directly).

---

## The rule

**Every typed-answer blank (`.ans-input`) within the same exercise must be the same fixed width — never sized to match, or hint at, the length of its own expected answer.**

- Variable widths leak the answer. If one blank is narrow and another is wide, a student can guess the grammatical form (e.g. short simple form vs. long continuous form) just by looking at the size of the space, without knowing the language.
- Fix: pick one width that comfortably fits the *longest* expected answer in the exercise, and apply that same width to every blank in the set — including the short ones, which will now have visible empty space at the end. That empty space is intentional and correct; it's what keeps the exercise fair.
- This applies to any inline `style="width:...px;"` (or a shared class) placed on `.ans-input` elements — not just present perfect simple/continuous exercises, but any gap-fill where answers could vary in length (verb forms, contractions, one-word vs. multi-word answers, etc.).
- The base `.ans-input` class only defines `min-width:80px` with no default fixed width, so any exercise using variable per-blank widths needs to be checked and corrected under this rule.

## What's exempt

- Blanks in genuinely different exercises/slides where there's no shared answer-length pattern to give away (e.g. a single standalone blank with no sibling blanks in the same task).
- Widths driven by layout/space constraints rather than answer length (e.g. a blank sized to fit inline in a short phrase where every possible answer in that specific slot is naturally similar length) — but default to uniform width whenever in doubt.

## Applied to AEF4-2A on 2026-07-16

Slide 17 ("Applying" — present perfect simple vs. continuous, `id="s-gram4"`) had 8 `.ans-input` blanks with inline widths scaling from 118px to 245px directly by answer length, letting students tell simple from continuous just by blank size. All 8 were reset to a single uniform `width:260px` (sized to comfortably fit the longest answer, "have you been working out"). No other slide in the file had this issue.

---

# 🔎 Companion Standard — Height for Single-Line Textarea Answer Lines

This is the height counterpart to the width rule above: it governs `textarea.ans-input` height, not width.

## The rule

**A `textarea.ans-input` used for a single line of free-response text (one sentence, e.g. dictation) must render at single-line height — never inherit the tall multi-line box meant for paragraph-length answers.**

- The shared base rule `textarea.ans-input { min-height:70px; resize:vertical; }` exists for genuinely multi-line free-response tasks (e.g. "write 4-5 sentences about..."), where a tall box is correct and expected.
- Applying that same 70px-tall box to a `rows="1"` textarea meant to hold one short sentence (e.g. a dictation exercise, six textareas stacked one per line) makes every line look like an oversized empty rectangle with dead space, even though only one line of text is expected — this reads as sloppy and wastes vertical space.
- Fix: any `textarea.ans-input[rows="1"]` gets a scoped override to a compact fixed height (`height:38px; min-height:38px; resize:none;`) instead of the 70px multi-line default. This keeps the visual line-height reasonable for one sentence while still using a `<textarea>` element (needed for text that may wrap on narrow screens).
- `resize:none` is intentional for these — a single-sentence line shouldn't invite the student to drag it taller, unlike genuine multi-line free-response boxes which should stay resizable.

## What's exempt

- Any `textarea.ans-input` with `rows` of 2 or more, or genuinely open-ended multi-sentence prompts — these keep the default 70px+ resizable box.

## Applied to AEF3-2A on 2026-07-16

The dictation exercise (6 `rows="1"` textareas, "Listen and write the six sentences you hear," now living on slide 10 / `id="s-pron2"`) was rendering all 6 lines at the full 70px multi-line height with visible empty space below each one-sentence answer. Added the `textarea.ans-input[rows="1"]` override above; no other slide in AEF3-2A or AEF4-2A currently uses `rows="1"` textareas, so no other slide was affected.
