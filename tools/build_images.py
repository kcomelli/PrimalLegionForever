"""Generate web-optimized images for the website from the raw files in media/.

Files in media/ are only READ, never modified. All output goes to website/images/.
Requires Pillow:  python -m pip install --user Pillow
Run from the project root:  python tools/build_images.py
"""
import re
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
MEDIA = ROOT / "media"
OUT = ROOT / "website" / "images"

BACKGROUND = "WoW_Forever_Cinematic_Still_1.jpeg"
LOGO = "PLLogoDraft7.png"
SYMBOL = "guild_symbol_9_512x512_transparent.png"
DISCORD = "discord.svg"
DISCORD_COLOR = "#9e6926"  # --gold-dark, same as the countdown numbers

# Landscape versions of the background (widths in px)
BG_WIDTHS = [1280, 1920, 2560, 3840]
# Portrait crop (for phones) centered on the dwarf & bear, x-center in source px
PORTRAIT_CENTER_X = 1100
PORTRAIT_RATIO = 9 / 16
PORTRAIT_HEIGHTS = [800, 1600]


def save_pair(im, name, quality=82, alpha=False):
    """Save as WebP plus a fallback (PNG if transparent, else JPEG)."""
    im.save(OUT / f"{name}.webp", "WEBP", quality=quality, method=6)
    if alpha:
        im.save(OUT / f"{name}.png", "PNG", optimize=True)
    else:
        im.convert("RGB").save(OUT / f"{name}.jpg", "JPEG", quality=quality, optimize=True, progressive=True)


def resize_w(im, width):
    if width >= im.width:
        return im.copy()
    return im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)


def build_discord_svg():
    """Copy discord.svg: drop the white background rects, crop to the artwork, recolor to --gold-dark."""
    svg = (MEDIA / DISCORD).read_text(encoding="utf-8")
    svg = re.sub(r"<rect[^>]*/>\s*", "", svg)
    svg = svg.replace('width="211" height="44" viewBox="0 0 211 44"',
                      'width="191" height="28" viewBox="10 8 191 28"')
    svg = svg.replace('fill="black"', f'fill="{DISCORD_COLOR}"')
    (OUT / "discord.svg").write_text(svg, encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    with Image.open(MEDIA / BACKGROUND) as src:
        bg = src.convert("RGB")
    for w in BG_WIDTHS:
        save_pair(resize_w(bg, w), f"bg-{w}")

    crop_w = round(bg.height * PORTRAIT_RATIO)
    left = max(0, min(bg.width - crop_w, PORTRAIT_CENTER_X - crop_w // 2))
    portrait = bg.crop((left, 0, left + crop_w, bg.height))
    for h in PORTRAIT_HEIGHTS:
        w = round(h * PORTRAIT_RATIO)
        save_pair(portrait.resize((w, h), Image.LANCZOS) if h < portrait.height else portrait, f"bg-portrait-{w}")

    with Image.open(MEDIA / LOGO) as src:
        logo = src.convert("RGBA")
    for w in [800, 1600]:
        save_pair(resize_w(logo, w), f"logo-{w}", quality=88, alpha=True)

    with Image.open(MEDIA / SYMBOL) as src:
        symbol = src.convert("RGBA")
    for w in [256, 512]:
        save_pair(resize_w(symbol, w), f"symbol-{w}", quality=88, alpha=True)
    # Favicon from the guild symbol
    resize_w(symbol, 64).save(OUT / "favicon.png", "PNG", optimize=True)

    build_discord_svg()

    for f in sorted(OUT.iterdir()):
        print(f"{f.name:28s} {f.stat().st_size / 1024:8.0f} KB")


if __name__ == "__main__":
    main()
