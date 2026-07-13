# 📒 Notes System — Correction (matches AEF4 3A actual implementation)

This patches the **"📒 Notes System"** and **"🖨️ Print Lesson button"** sections of `AEF Lesson Standards.md`. The master file said "Print Lesson replaces Save Notes" and specified a single yellow highlight — that does not match what AEF4 3A (the reference lesson) actually has. AEF4 3A has **both** buttons plus 4-color highlighting with toggle-off. Use this version going forward.

---

## Nav bar — both buttons, not a replacement

```
◀ Prev | dots | counter | Next ▶ | 💾 Save Notes | 🖨️ Print Lesson
```

- **💾 Save Notes** (`savePDF()`) — background `#2E2A6B`. Opens a new tab with a clean, printable summary of every slide that has notes (slide number + label as a card header, note content below), then triggers `window.print()` after a short delay. If no notes exist yet, alerts "No notes to save yet!" instead of opening a blank tab.
- **🖨️ Print Lesson** (`printAll()`) — background `#0E5A8A`. Unchanged from the master file: prints the entire lesson deck, one slide per page, in original layout, with the cover banner and per-slide teacher-notes blocks.

These are two distinct, complementary tools — Save Notes exports just the notes as a standalone reference page; Print Lesson exports the whole lesson with notes embedded in context. Neither replaces the other.

## Notes toolbar — 4 highlight colors + remove, with toggle-off

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
- Function names: `notesFormat(cmd)` for bold/underline, `notesHilite(color)` for all highlight actions — not `fmt()` / `fmtHilite()`.
- `#notesTA` uses `data-placeholder` + `:empty::before` for the placeholder text (not a plain `contenteditable` with no placeholder), and saves on `oninput="saveNotes()"` directly on the element rather than a separate `addEventListener`.

## Notes button label toggles

```js
function toggleNotes(){
  notesOpen = !notesOpen;
  var panel = document.getElementById('notesPanel');
  panel.classList.toggle('open', notesOpen);
  if (current === 0) panel.classList.toggle('cover', notesOpen);
  document.getElementById('notesBtn').textContent = notesOpen ? '✕ Close' : '📝 Notes';
}
```

Requires a top-level `var notesOpen = false;` alongside `notesData`/`current`. The button text itself changes between "📝 Notes" and "✕ Close" — it isn't a fixed label.

## Panel animation

`#notesPanel` uses `max-height: 0 → 320px` + `opacity` transition (not `display:none/flex`) for a smooth slide-open, and has a dark frosted-glass style (`background: rgba(10,40,54,.92)` on the textarea, `backdrop-filter: blur`) rather than a plain white box.

---

*Applied to AEF4 3B on 2026-07-12. Recommend folding this into the master `AEF Lesson Standards.md` the next time it's edited directly.*
