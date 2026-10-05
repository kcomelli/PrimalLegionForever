# CLAUDE.md
This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.
Read it at the start of every session.

# Context
A simple static website presenting our World of Warcraft Forever guild **"Primal Legion Forever"**.
Currently no dynamic php content like CMS or BulletinBoards planned.

# Working rules (from the owner)
- **Never assume – always ask** before making a decision. Keep questions/answers short and meaningful.
- **Never modify files in `media/`.** Copy or derive them into `website/` (via `tools/build_images.py`).
- Document knowledge in `documentation/`; manage work in `tasks/` (see below).
- Website must be **responsive** (desktop, tablet, mobile phones).

# Folder structure
| Folder | Purpose |
|---|---|
| `website/` | Everything that gets deployed. `index.html`, `impressum.html`, `style.css` + `images/` |
| `website/fonts/` | Self-hosted web fonts (Cinzel, EB Garamond) + OFL licenses. Never use external font CDNs (privacy statement) |
| `website/images/` | Generated, web-optimized images (do not edit by hand – regenerate) |
| `media/` | Raw source media from the owner (big files). **Read-only.** Ignored by git (`.gitignore`) |
| `tools/` | Helper scripts, e.g. `build_images.py` |
| `documentation/` | Knowledge base (design, color scheme, image pipeline, decisions) |
| `tasks/` | Open tasks as markdown files; move to `tasks/done/` when finished |

# Website overview
- Single page `website/index.html` (plain HTML + inline JS for the release countdown), styles in `website/style.css`.
- Full-screen background image (`<picture>` with WebP + JPEG, landscape sizes + a portrait crop for phones).
- Crest in the top third: guild symbol – guild logo – guild symbol. On screens ≤ 700px: one symbol above the logo.
- Countdown to the WoW Forever release (4 Nov 2026, 15:00 PST) below the logo, German labels.
- Discord link (recolored `discord.svg`) below the countdown.
- Custom styled tooltips (navy + gold) for countdown and Discord link.
- Small footer link "Impressum & Datenschutz" → `website/impressum.html`.
- `website/impressum.html`: same design (logo links back), two info boxes (Impressum / Datenschutzinfo) side by side, stacked on phones; spam-protected e-mail (assembled by JS).
- See `documentation/website-design.md` and `documentation/color-scheme.md`.

# Image pipeline
`python tools/build_images.py` (requires Pillow: `python -m pip install --user Pillow`).
Reads from `media/`, writes to `website/images/`. Details: `documentation/image-pipeline.md`.

# Tasks workflow
- One markdown file per task in `tasks/`, named `NNN-short-name.md` (status, description, acceptance criteria).
- When done: set status to done and move the file to `tasks/done/`.
