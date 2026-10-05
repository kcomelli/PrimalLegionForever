# Website design & decisions

## Layout (`website/index.html`, styles in `website/style.css`)
- Background: fixed full-viewport `<picture>`, `object-fit: cover`.
  - Landscape: `bg-*` versions, chosen by browser via `srcset`; `object-position: 29% 50%` keeps dwarf & bear in view when cropped.
  - Portrait orientation: `bg-portrait-*` (pre-cropped 9:16 around dwarf & bear).
- Crest (header): centered horizontally, vertically centered in the **top third** of the viewport.
  - > 700px wide: symbol – logo – symbol in one row, scaling with viewport (logo `min(56vw, 900px, 72svh)`, symbols 30% of logo width).
  - ≤ 700px wide: one symbol **above** the logo, second symbol hidden.
- Logo is inside the `<h1>` (alt text = guild name).
- Glow: static dark-brown `filter: drop-shadow` on logo + symbols (`rgb(26 9 0)`, 4px @ 0.9 + 14px @ 0.65).
- Countdown (inline JS at end of `index.html`) below the logo, absolutely positioned so the logo keeps its place:
  - Target: WoW Forever release **4 Nov 2026, 15:00 PST = 23:00 UTC** (`Date.UTC(2026, 10, 4, 23)`), shown in the user's own time zone automatically.
  - German labels (Tag/Tage, Stunde/Stunden, ...) small below the numbers; tooltip `Primal Legion Forever in ...` (see Tooltips).
  - Box: white 80% opacity, padding 0.2em 0.4em 0.4em 0 (no left), top margin clamp(1rem, 3vw, 2.5rem), radius 0.25em; numbers `--gold-dark`, labels `--bronze`.
  - Hidden without JavaScript and once the release time is reached.
- Discord link below the countdown (same top margin `--below-gap`), inside the shared `.below-logo` container:
  - `images/discord.svg` = copy of `media/discord.svg`, white background removed, cropped, recolored to `--gold-dark` (by `tools/build_images.py`).
  - Width `4.32em` of the countdown font size; no glow; slight zoom on hover.
  - Link `https://discord.gg/gnGRPBTTb`, opens in a new tab, tooltip "Primal Legion Discord Server".
- Tooltips (custom, no `title` attributes): `<span class="tooltip">` with `role="tooltip"` + `aria-describedby`.
  - Style: navy-deep 90% background, 1px `--gold-mid` border, cream text, small arrow, 150ms fade + slide.
  - Countdown: `.tooltip-side` = left of the box on screens > 900px, above it on ≤ 900px.
  - Discord: `.tooltip-bottom` = below the logo.
  - Shown on hover after a 400 ms delay (only devices with a mouse), immediately on keyboard focus, and on touch devices by tapping the countdown (JS toggles `.show-tip`, tap elsewhere closes). Discord shows no tooltip on touch (tap opens the link).
  - Respects `prefers-reduced-motion`.
- Footer (index.html): small cream link "Impressum & Datenschutz" at the bottom right (`.site-footer`, `.page-link`).

## Fonts (self-hosted in `website/fonts/`, SIL OFL licenses included)
- **Cinzel** 400/700 (`--font-display`): logo-like Roman capitals – footer/back links, Impressum captions and headings. Note: Cinzel has no lowercase, so "ß" renders as "SS".
- **EB Garamond** 400/700 (`--font-text`): running text in the Impressum boxes.
- Countdown keeps Georgia (owner decision).
- Fonts are hosted locally on purpose: the Datenschutzinfo promises no external font services (e.g. Google Fonts).

## Impressum page (`website/impressum.html`, `lang="de"`)
- Same background + crest as index; crest is in normal flow (`.page-impressum .crest { position: relative }`) so the boxes follow below.
- Logo links back to `index.html`; plus "← Zurück zur Startseite" link below the boxes.
- Two `.info-box` sections (white 80%, rounded, like the countdown box): "Impressum / Offenlegung gemäß § 25 MedienG" and "Datenschutzinfo".
  Side by side (each as high as its content), stacked vertically on ≤ 700px.
- Colors: captions/headings `--gold-dark`, body text `--brown-dark` (readability).
- E-mail spam protection: `<a class="email" data-user data-domain>`; inline JS builds the `mailto:` link. Without JS: "fuddler [at] primal-legion.net" as text.
- Page title is a visually hidden `<h1>` (`.sr-only`).

## Decisions log (asked owner)
| Date | Decision |
|---|---|
| 2026-10-05 | Image tool: Python Pillow, WebP + JPEG/PNG fallback |
| 2026-10-05 | Phone background focus: dwarf & bear (left-center) |
| 2026-10-05 | No dark gradient overlay over the background |
| 2026-10-05 | Phones: only one symbol, placed above the logo |
| 2026-10-05 | Logo + symbols: static, medium, dark-brown glow (CSS drop-shadow) |
| 2026-10-05 | Countdown: German labels, no caption, tooltip "Primal Legion Forever in ...", hide at zero, white 60% box |
| 2026-10-05 | Countdown box: 80% opacity, padding halved, radius halved (0.25em) |
| 2026-10-05 | Countdown box: padding top 0.2em / right 0.4em / bottom 0.4em / left 0; top margin doubled |
| 2026-10-05 | Discord SVG link below countdown, same color as countdown text, new tab |
| 2026-10-05 | Discord logo: reduced to 60% (9em → 5.4em), glow removed |
| 2026-10-05 | Custom tooltips: navy + gold border, fade + slide; countdown left/top (responsive), Discord below; tap-to-show countdown tooltip on touch |
| 2026-10-05 | All CSS moved from index.html into website/style.css |
| 2026-10-05 | Impressum page: footer link on index, logo + "Zurück" link back, spam-protected mailto, gold captions + dark brown text |
| 2026-10-05 | Footer link right-aligned; fonts Cinzel (captions/links) + EB Garamond (text), self-hosted; countdown unchanged |
| 2026-10-05 | Vertical scrollbar always shown (`html { overflow-y: scroll }`) so pages don't shift when switching |
| 2026-10-05 | Tooltips: 400 ms hover delay (focus/tap immediate, hiding immediate) |
| 2026-10-05 | Discord logo reduced to 80% (5.4em → 4.32em) |
