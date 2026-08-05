#!/usr/bin/env python3
"""Center-crop generated scene art to an exact 16:9 canvas without upscaling.

The image service may return a near-16:9 raster (for example 1376×768). Run this
immediately after each scene-image batch, before rebuilding the gallery:
    ../.venv/bin/python normalize_16x9.py

Reference portraits are intentionally excluded; only images/act1 through act3 are
scene images and must be delivered at exactly 16:9.
"""
from __future__ import annotations

from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def target_size(width: int, height: int) -> tuple[int, int]:
    """Find the largest whole-pixel 16:9 frame that fits inside the source."""
    max_height = min(height, (width * 9) // 16)
    target_height = max_height - (max_height % 9)
    target_width = (target_height * 16) // 9
    if target_width == 0 or target_height == 0:
        raise ValueError(f"Image too small for 16:9 crop: {width}x{height}")
    return target_width, target_height


def normalize(path: Path) -> bool:
    with Image.open(path) as source:
        width, height = source.size
        new_width, new_height = target_size(width, height)
        if (width, height) == (new_width, new_height):
            return False
        left = (width - new_width) // 2
        top = (height - new_height) // 2
        cropped = source.crop((left, top, left + new_width, top + new_height))
        kwargs = {"optimize": True}
        if path.suffix.lower() in {".jpg", ".jpeg"}:
            kwargs["quality"] = 95
        cropped.save(path, **kwargs)
    print(f"Normalized {path.relative_to(ROOT)}: {width}x{height} → {new_width}x{new_height}")
    return True


def main() -> None:
    changed = 0
    for act in ("act1", "act2", "act3"):
        folder = ROOT / "images" / act
        if folder.exists():
            for path in sorted(folder.iterdir()):
                if path.is_file() and path.suffix.lower() in EXTENSIONS:
                    changed += normalize(path)
    print(f"Exact 16:9 normalization complete; {changed} file(s) cropped.")

if __name__ == "__main__":
    main()
