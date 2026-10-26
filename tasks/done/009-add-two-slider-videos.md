# 009 – Add two videos to the slider

**Status:** done (2026-10-26)

## Description
Add "PL Onyxia 2005" (between "PL MoltenCore Promo 2005" and "PL BlackWing Lair 2005") and
"PL AQ40 Fankriss-Huhuran 2006" (between "PL AQ20 ServerFirst 2006" and "PL AQ40 Twins 2006") to the slider,
with generated thumbnails and hover titles.

## Acceptance criteria
- [x] Thumbnails generated (`tools/build_video_thumbnails.py`, `website/images/video-<id>.webp/.jpg`)
- [x] Both videos link to YouTube (`_blank`) at the requested positions
- [x] Slider loop still works with 20 videos
