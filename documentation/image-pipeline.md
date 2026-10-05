# Image pipeline

Script: `tools/build_images.py` (Python + Pillow). Run from project root:

```
python -m pip install --user Pillow   # once
python tools/build_images.py
```

- Source files in `media/` are **only read**, never changed. Output → `website/images/`.
- Every image is written as **WebP** plus a fallback (**JPEG** for photos, **PNG** for transparent images).
- `media/` is git-ignored, so the generated `website/images/` must be committed.

## Generated files
| Output | Source | Notes |
|---|---|---|
| `bg-1280/1920/2560/3840.(webp,jpg)` | `WoW_Forever_Cinematic_Still_1.jpeg` (3840×1600) | Landscape background |
| `bg-portrait-450/900.(webp,jpg)` | same | 9:16 crop centered on dwarf & bear (x≈1100px) for portrait screens |
| `logo-800/1600.(webp,png)` | `PLLogoDraft7.png` (2172×724) | Guild logo |
| `symbol-256/512.(webp,png)` | `guild_symbol_9_512x512_transparent.png` | Guild symbol |
| `favicon.png` | guild symbol | 64×64 |
| `discord.svg` | `discord.svg` | White background rects removed, viewBox cropped to `10 8 191 28`, fill → `#9e6926` |

To change sources, crop focus or sizes, edit the constants at the top of the script.
