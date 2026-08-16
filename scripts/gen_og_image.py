#!/usr/bin/env python3
"""Generate a 1200x630 Open Graph share image for the farm site."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
IMG = "og.png"

BG_TOP = (22, 99, 108)
BG_BOT = (15, 76, 83)
YOLK = (255, 201, 60)
YOLK_DEEP = (237, 168, 22)
CREAM = (250, 246, 236)
GREEN = (15, 76, 83)
TEAL = (168, 220, 226)

FONT_BOLD = "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def egg(d, cx, cy, scale=1.0):
    def s(v):
        return int(v * scale)

    # shell
    d.ellipse([cx - s(150), cy - s(120), cx + s(150), cy + s(170)], fill=(255, 250, 236), outline=GREEN, width=s(8))
    # inner ring
    d.ellipse([cx - s(95), cy - s(70), cx + s(95), cy + s(120)], outline=(15, 76, 83), width=s(5))
    # yolk cap
    d.pieslice([cx - s(150), cy - s(120), cx + s(150), cy + s(170)], 180, 330, fill=YOLK, outline=GREEN, width=s(8))
    # yolk shine
    d.ellipse([cx - s(60), cy - s(70), cx - s(20), cy - s(30)], fill=(255, 233, 158))


def main():
    img = Image.new("RGB", (W, H), BG_TOP)
    d = ImageDraw.Draw(img)

    # vertical gradient
    for y in range(H):
        t = y / H
        c = tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)

    # decorative circles
    d.ellipse([-140, 380, 260, 780], fill=(255, 201, 60), outline=None)
    d.ellipse([1080, -180, 1500, 240], fill=None, outline=TEAL, width=10)
    d.ellipse([-80, -140, 240, 180], fill=None, outline=(168, 220, 226), width=6)
    d.ellipse([900, 430, 1260, 790], fill=None, outline=(255, 201, 60), width=8)

    # egg illustration on the right
    egg(d, 920, 300)

    # text
    d.rounded_rectangle([70, 62, 480, 118], radius=28, fill=(15, 76, 83))
    d.text((100, 78), "FRESH DUCK EGGS", font=font(FONT_BOLD, 26), fill=YOLK)

    d.text((70, 150), "Shree BajraBarahi", font=font(FONT_BOLD, 66), fill=CREAM)
    d.text((70, 232), "Farm", font=font(FONT_BOLD, 66), fill=YOLK)

    d.text((72, 350), "Naturally raised, free-range duck eggs.", font=font(FONT_REG, 30), fill=(220, 236, 238))
    d.text((72, 398), "Chapagaun, Lalitpur \u00b7 farm-fresh daily", font=font(FONT_REG, 28), fill=(185, 214, 218))

    d.rounded_rectangle([70, 470, 470, 540], radius=36, fill=YOLK)
    d.text((102, 484), "Crate of 30 eggs \u2014 Rs. 900", font=font(FONT_BOLD, 30), fill=GREEN)

    img.save(IMG)
    print(f"Saved {IMG} ({W}x{H})")


if __name__ == "__main__":
    main()
