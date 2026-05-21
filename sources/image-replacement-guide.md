# Image replacement manifest

This Quarto repository is prepared for manually downloaded images from the past Google Sites pages.

- Actual local images currently included: **16**
- Placeholder images to replace manually: **24**

The canonical checklist is `sources/image-replacement-manifest.csv`. Replace files at the listed paths directly. The `.qmd` files already point to these paths.

Recommended target dimensions:

- Headshots: 900 × 900 px, `.jpg`
- Hero images: 1920 × 1080 px, `.png`
- Banners: 1920 × 640 px, `.png`
- Figures: 1600 × 1000 px, `.png`
- Logos: 1200 × 600 px or SVG

After replacing files, run:

```bash
quarto preview
```
