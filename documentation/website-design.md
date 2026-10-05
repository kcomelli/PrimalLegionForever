# Website design & decisions

## Layout (`website/index.html`)
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
  - Width `5.4em` of the countdown font size; no glow; slight zoom on hover.
  - Link `https://discord.gg/gnGRPBTTb`, opens in a new tab, tooltip "Primal Legion Discord Server".
- Tooltips (custom, no `title` attributes): `<span class="tooltip">` with `role="tooltip"` + `aria-describedby`.
  - Style: navy-deep 90% background, 1px `--gold-mid` border, cream text, small arrow, 150ms fade + slide.
  - Countdown: `.tooltip-side` = left of the box on screens > 900px, above it on ≤ 900px.
  - Discord: `.tooltip-bottom` = below the logo.
  - Shown on hover (only devices with a mouse), keyboard focus, and on touch devices by tapping the countdown (JS toggles `.show-tip`, tap elsewhere closes). Discord shows no tooltip on touch (tap opens the link).
  - Respects `prefers-reduced-motion`.

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
