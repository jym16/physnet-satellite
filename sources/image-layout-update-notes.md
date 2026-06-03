# Image layout update notes

Updated after the detailed-program/theme revision.

## Logo transparency

- Replaced `assets/img/common/logos/common_logo_physnet-mark.png` with a transparent PNG derived from the user-provided satellite logo.
- Added `assets/img/common/logos/common_logo_physnet-mark-transparent.png` as an explicit transparent duplicate for future reference.
- Removed the solid white background rectangles from `assets/img/physnet-logo.svg` and `assets/img/physnet-mark.svg`.

## Past-edition banner and hero layout

- Added local hero-image slots to the 2023, 2024, and 2025 archive pages.
- Added `assets/img/2025/hero/2025_hero_physical-network-render.png` as a 1920 x 1080 placeholder.
- Added CSS so `.edition-banner` and `.edition-hero-image` use the available page width, scale down on narrow screens, and avoid cropping.

Replacement convention:

```text
assets/img/YYYY/banners/YYYY_banner_*.png
assets/img/YYYY/hero/YYYY_hero_physical-network-render.png
```

The files can be overwritten directly after manual download and editing. No `.qmd` edits are needed if the filenames are preserved.
