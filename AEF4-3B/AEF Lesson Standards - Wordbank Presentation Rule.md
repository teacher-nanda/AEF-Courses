# 🔎 New Standard — Wordbank Presentation: Click-to-Place vs. Click-to-Mark-Used

This adds a new rule to `AEF Lesson Standards.md` (the master file is read-only, so this is tracked separately — fold it in the next time the master file is edited directly).

The Exercise Type Reference table already documents two relevant interaction patterns ("Word bank → fill blank" and "Word order chips") but doesn't say which one to use when. This rule makes that choice explicit and mandatory — every wordbank/word-list exercise must be **clickable**, using whichever of the two patterns below fits the exercise.

---

## The rule: decide by whether the word changes form

Before building any exercise that gives the student a list of words to complete sentences/blanks, check the answer key: **does every word get used exactly as written in the bank, with no change at all?**

### Case A — words are used unchanged → click-tile-then-click-blank (word gets placed)

If every word in the bank is dropped into its blank exactly as written (no conjugation, no pluralizing, no added words), use the existing **"Word bank → fill blank"** pattern:
- Click a tile in the bank → click the blank it belongs in → the tile's text fills the blank and the tile grays out ("used").
- Click a **filled** blank again to remove it and return the tile to the bank.
- `wbPick` / `wbPlace` / `checkWbSlide` / `resetWbSlide` — already fully generic and reusable.
- If the exercise's worked example consumes one tile, that tile starts already marked "used" (grayed out, not clickable) — see the Homework "Word-bank tiles that get used up" section, which already documents this for homework and now applies everywhere.

### Case B — one or more words need to change form → click-to-mark-used, typed blank

If **any** word in the bank needs to change (verb conjugation/tense, add -s, add "is"/"are", pluralize, etc.) to fit its sentence, a placed-tile mechanic would silently produce wrong sentences. Instead:
- The blank stays a normal **typed** `.ans-input`, graded with `checkSlide`/`data-ans` as usual.
- The wordbank itself is still fully **clickable** — clicking a word toggles a crossed-out/grayed "used" visual state, purely as a self-tracking aid so the student can see at a glance which base words they've already drawn on. This state is **not graded** and does not feed into `checkSlide` — it's bookkeeping, not part of the answer.
- Generic helper: `mvWordToggle(el){ el.classList.toggle('used'); }` — one class toggle, reusable across any lesson's wordbank of this type. Give the wrapping CSS classes a lesson-specific prefix if convenient, but the toggle function itself needs no per-slide variant.
- If the worked example already uses one of the words, that word starts pre-marked "used" and is **not clickable** (`cursor:default`, no `onclick`) — same logic as Case A's pre-used tile.
- **Per the answer-blank width rule** (see the separate Uniform Answer Blank Width patch note): since Case B blanks hold answers of varying length by definition (that's *why* it's Case B), all blanks in the exercise must still share one uniform width — never size a blank to the length of its own answer.

### Exception — reusable word lists ("you can use these more than once")

If the exercise's own instruction says a word may be reused (e.g., "Complete with an adverb from the list — you can use the adverbs more than once"), don't apply either click-tracking pattern: a single click-to-mark-used toggle is misleading when a word is meant to be drawn on multiple times, and consumable-tile placement doesn't fit either. Leave this kind of list as **plain static reference text** (not clickable), styled distinctly from the exercise content (e.g., inside a `.card`).

### Non-exception — pure reference/discussion word lists

A word list shown only to support a discussion or observation question (not feeding any blank at all — e.g., "look at these words, which two are pronounced differently?") isn't a "wordbank" under this rule at all. Leave it as plain static text; there's nothing to place and nothing to mark used.

---

## Applied to AEF3-2A on 2026-07-16

- **s-vocab5** ("Money — nouns") and **hw-voc3** ("Bank Advertisement") were already correctly built as Case A (`wbPick`/`wbPlace`) — no change needed.
- **s-vocab3** ("Money Verbs") was Case B (two of the thirteen words need a form change: *charge* → *charges*, *be worth* → *is worth*) but its wordbank was plain static text with no click interaction — added `mv-word`/`mvWordToggle()` so every word (except the pre-used example "inherit") is now clickable and crosses itself out on tap; the answer blanks were already uniform width from the earlier Answer Blank Width fix.
- **s-gram-ex2**'s adverb list (already/ever/never/yet, explicitly reusable per its own instruction) correctly stays as plain static reference text under the exception above — no change needed.
- **s-pron2**'s word list (afford/mortgage/order/organized/store/worth) is a pure pronunciation-observation reference, not a blank-filling wordbank — correctly non-interactive, no change needed.
