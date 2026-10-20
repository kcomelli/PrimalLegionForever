# 008 – "Unsere Geschichte" video slider

**Status:** done (2026-10-20)

## Description
Slider with 1-5 video thumbnails (responsive) of the guild's old videos, caption "Primal Legion Origins" (later renamed "Unsere Geschichte", frame removed),
links to YouTube in a new tab, local thumbnails, title on hover, framed box, prev/next buttons and auto-scroll.

## Acceptance criteria
- [x] 18 videos from the owner's list, each linking to YouTube (`_blank`)
- [x] Thumbnails stored under `website/images/` (best YouTube frame per video, `tools/build_video_thumbnails.py`)
- [x] 1 to 5 videos visible depending on screen width
- [x] Title shown on hover (caption bar; always visible on touch)
- [x] Frame matching the site's look (gold/navy), prev/next buttons
- [x] Auto-scroll one video every 3 s, endless loop, pauses on hover
