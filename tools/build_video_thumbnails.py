"""Generate the thumbnails for the "Primal Legion Origins" slider.

For every video, one YouTube-provided frame is downloaded (hqdefault, hq1-3 = frames at ~0/25/50/75% of the
video, or maxresdefault), black borders are trimmed, the image is cropped to 16:9 and saved as WebP + JPEG
in website/images/ (video-<youtube id>.webp / .jpg). The website itself never loads anything from YouTube.

Run from the project root (needs Pillow and internet access):  python tools/build_video_thumbnails.py
To change a thumbnail, edit its FRAME below and run the script again.
"""
import io
import urllib.request
from pathlib import Path

from PIL import Image

OUT = Path(__file__).resolve().parent.parent / "website" / "images"

# (youtube id, frame, title) - the title is only for reading this list; the page has its own titles
VIDEOS = [
    ("LQnIpH0J2VI", "hq1", "PL MoltenCore Promo 2005"),
    ("A9Te-oFUQpw", "hq1", "PL Onyxia 2005"),
    ("IfHmNh2KctY", "hqdefault", "PL BlackWing Lair 2005"),
    ("uy8V6CC2S5U", "hq1", "PL BlackWind Lair - Nefarian 2005"),
    ("1hXHz1bA64c", "hq3", "PL Sulfaras 2006"),
    ("A-9yEaQeovA", "hq3", "PL AQ20 ServerFirst 2006"),
    ("s2TPZ3W0y3U", "hqdefault", "PL AQ40 Fankriss-Huhuran 2006"),
    ("ZdQQVecbDc4", "hq2", "PL AQ40 Twins 2006"),
    ("e0rKSQuHNI4", "hq3", "PL Naxxramas 2006"),
    ("RylU3zUkZIk", "hqdefault", "PL Kael Thas 2008"),
    ("kUvEuuMNxNU", "hq3", "PL Kalecgos Sunwell 2008"),
    ("YzfbbGQ11Js", "hq1", "PL Satharion 3D 2009"),
    ("tc_sbT2fG8U", "hq3", "PL Nefarian 10 2011"),
    ("xcqQJuOVKmM", "maxresdefault", "PL Forever 2026"),
    ("T4T4LLr75Zg", "hqdefault", "PL Foredoomed 2005"),
    ("u3O42JzSiA8", "hq1", "PL Foredoomed (2) 2005"),
    ("PNkB0OU81BY", "hq1", "PL Foredoomed (3) 2006"),
    ("__Msbi4Ut3M", "hq1", "PL Foredoomed (4) 2006"),
    ("lDDt_FVpQ-E", "hq1", "PL Foredoomed (5) 2005"),
    ("ovCZ68D2dJc", "hqdefault", "PL Foredoomed (6) 2007"),
]

SIZE = (480, 270)        # 16:9
BLACK_THRESHOLD = 24     # pixels at or below this brightness count as black border


def download(video_id, frame):
    url = f"https://i.ytimg.com/vi/{video_id}/{frame}.jpg"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return Image.open(io.BytesIO(resp.read())).convert("RGB")


def trim_black(im):
    """Cut away black letterbox/pillarbox borders."""
    mask = im.convert("L").point(lambda v: 255 if v > BLACK_THRESHOLD else 0)
    box = mask.getbbox()
    return im.crop(box) if box else im


def crop_16_9(im):
    w, h = im.size
    if w / h > 16 / 9:
        new_w = round(h * 16 / 9)
        left = (w - new_w) // 2
        return im.crop((left, 0, left + new_w, h))
    new_h = round(w * 9 / 16)
    top = (h - new_h) // 2
    return im.crop((0, top, w, top + new_h))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for video_id, frame, title in VIDEOS:
        im = crop_16_9(trim_black(download(video_id, frame)))
        im = im.resize(SIZE, Image.LANCZOS)
        im.save(OUT / f"video-{video_id}.webp", "WEBP", quality=82, method=6)
        im.save(OUT / f"video-{video_id}.jpg", "JPEG", quality=82, optimize=True, progressive=True)
        print(f"{video_id}  {frame:14s} {title}")


if __name__ == "__main__":
    main()
