# Shree BajraBarahi Farm

Naturally raised, free-range duck eggs from a small family farm in Chapagaun, Lalitpur.

## Site

Served at https://farm.srijantangnamimagar.com.np via GitHub Pages.

## Structure

- `index.html` — single-page farm site
- `styles.css` — natural farm theme
- `farm.js` — small interactions (reveal on scroll)
- `CNAME` — custom domain for GitHub Pages

## Before going live
-----------------

Replace the remaining placeholders in `index.html`:

- Phone / WhatsApp number (`+977 98XX XXXXXX`) — used in the Contact box, the
  `tel:` order link, and the JSON-LD structured data (`telephone`)
- Delivery areas if narrower than the valley

Prices are set: Rs. 450 / half crate (15 eggs), Rs. 900 / full crate (30 eggs).

Photos for the gallery can be dropped in later by replacing each `.gallery-slot`
placeholder with a real `<img>`.

SEO
---

- `index.html` carries Open Graph / Twitter cards, geo tags, canonical, and
  LocalBusiness JSON-LD with the farm's exact coordinates and price offer.
- `og.png` (1200x630) is the social share image. Regenerate it after changing
  prices/name with: `python3 scripts/gen_og_image.py`
- `sitemap.xml` and `robots.txt` are configured for the custom domain.
- After publishing, submit the URL in Google Search Console:
  https://search.google.com/search-console (add `farm.srijantangnamimagar.com.np`)

Deploys automatically to GitHub Pages on every push to `main`.
