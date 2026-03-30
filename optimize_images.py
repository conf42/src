#!/usr/bin/env python3
"""Optimize images in docs/assets/ for web — compress only, no resizing.

Strategy:
  - splash/*.png  → convert to JPEG quality 82 (keep dimensions, delete PNG)
                    generate.py already prefers .jpg over .png via pick_picture_file()
  - other *.png   → lossless PNG re-compression (logos/branding may have transparency)
  - *.jpg/jpeg    → re-save at JPEG quality 82
"""

from pathlib import Path
from PIL import Image

ASSETS_DIR = Path("docs/assets")
SKIP_DIRS = {"favicon", "css", "js", "fonts"}
JPEG_QUALITY = 82
MIN_FILE_SIZE = 10 * 1024  # skip files under 10KB


def png_to_jpeg(path):
    """Convert a PNG photo to JPEG (same dimensions). Deletes source PNG."""
    if path.stat().st_size < MIN_FILE_SIZE:
        return 0, 0
    try:
        img = Image.open(path)
        original_size = path.stat().st_size
        if img.mode in ("RGBA", "P"):
            bg = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "P":
                img = img.convert("RGBA")
            bg.paste(img, mask=img.split()[3] if img.mode == "RGBA" else None)
            img = bg
        elif img.mode != "RGB":
            img = img.convert("RGB")
        jpg_path = path.with_suffix(".jpg")
        img.save(jpg_path, "JPEG", quality=JPEG_QUALITY, optimize=True)
        new_size = jpg_path.stat().st_size
        path.unlink()  # remove original PNG
        saving = original_size - new_size
        pct = saving * 100 // original_size
        print(f"  {path.name} -> .jpg: {original_size // 1024}KB -> {new_size // 1024}KB  (-{pct}%)")
        return original_size, new_size
    except Exception as e:
        print(f"  WARNING {path.name}: {e}")
        return 0, 0


def optimize_jpeg(path):
    """Re-compress JPEG at target quality (no resize)."""
    if path.stat().st_size < MIN_FILE_SIZE:
        return 0, 0
    try:
        img = Image.open(path)
        original_size = path.stat().st_size
        if img.mode == "RGBA":
            bg = Image.new("RGB", img.size, (255, 255, 255))
            bg.paste(img, mask=img.split()[3])
            img = bg
        elif img.mode not in ("RGB", "L"):
            img = img.convert("RGB")
        img.save(path, "JPEG", quality=JPEG_QUALITY, optimize=True)
        new_size = path.stat().st_size
        saving = original_size - new_size
        pct = saving * 100 // original_size if original_size > 0 else 0
        if pct > 0:
            print(f"  {path.name}: {original_size // 1024}KB -> {new_size // 1024}KB  (-{pct}%)")
        return original_size, new_size
    except Exception as e:
        print(f"  WARNING {path.name}: {e}")
        return 0, 0


def optimize_png(path):
    """Lossless PNG re-compression (for logos/branding with transparency)."""
    if path.stat().st_size < MIN_FILE_SIZE:
        return 0, 0
    try:
        img = Image.open(path)
        original_size = path.stat().st_size
        img.save(path, "PNG", optimize=True, compress_level=9)
        new_size = path.stat().st_size
        saving = original_size - new_size
        pct = saving * 100 // original_size if original_size > 0 else 0
        if pct > 0:
            print(f"  {path.name}: {original_size // 1024}KB -> {new_size // 1024}KB  (-{pct}%)")
        return original_size, new_size
    except Exception as e:
        print(f"  WARNING {path.name}: {e}")
        return 0, 0


def main():
    if not ASSETS_DIR.exists():
        print("No docs/assets/ directory found")
        return

    total_before = 0
    total_after = 0

    for subdir in sorted(ASSETS_DIR.iterdir()):
        if not subdir.is_dir() or subdir.name in SKIP_DIRS:
            continue
        seen_keys = set()
        images = []
        for p in sorted(
            list(subdir.glob("*.jpg")) + list(subdir.glob("*.jpeg")) +
            list(subdir.glob("*.png")) + list(subdir.glob("*.PNG"))
        ):
            key = p.name.lower()
            if key not in seen_keys:
                seen_keys.add(key)
                images.append(p)
        if not images:
            continue
        print(f"\n{subdir.name}/ ({len(images)} images)")
        for img_path in images:
            suffix = img_path.suffix.lower()
            if suffix == ".png" and subdir.name == "splash":
                b, a = png_to_jpeg(img_path)
            elif suffix in (".jpg", ".jpeg"):
                b, a = optimize_jpeg(img_path)
            elif suffix == ".png":
                b, a = optimize_png(img_path)
            else:
                continue
            total_before += b
            total_after += a

    if total_before > 0:
        saved = total_before - total_after
        print(f"\n{'=' * 60}")
        print(f"Total: {total_before // 1024}KB -> {total_after // 1024}KB  "
              f"(saved {saved // 1024}KB, {saved * 100 // total_before}%)")
    else:
        print("\nNo images found to optimize.")


if __name__ == "__main__":
    main()
