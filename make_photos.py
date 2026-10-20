"""Run this after adding photos to the 'photos' folder:   python make_photos.py
It resizes big photos (long edge 1600px), then writes photos.js with sizes.
Needs Pillow once:  pip install pillow
"""
import os, json
from PIL import Image, ImageOps
D = "photos"; MAX = 1600
out = []
for f in sorted(os.listdir(D)):
    if not f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")): continue
    p = os.path.join(D, f)
    im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
    if max(im.size) > MAX:
        im.thumbnail((MAX, MAX)); im.save(p, quality=85, optimize=True)
    out.append({"src": f"{D}/{f}", "alt": os.path.splitext(f)[0].replace("_", " "), "w": im.width, "h": im.height})
open("photos.js", "w").write("window.PHOTOS = " + json.dumps(out, indent=2) + ";\n")
print(len(out), "photos written to photos.js")
