# Image replacement guide

This repository uses canonical local image paths so that the Quarto pages do not need to change when you replace placeholder images.

## Replacement rule

Replace the file at the same path with your edited image. Keep the filename and extension unchanged whenever possible. Then run:

```bash
quarto preview
```

## Target dimensions

| Type | Target size | Typical format | Notes |
|---|---:|---|---|
| Speaker or organizer headshot | 900 × 900 px | `.jpg` | Square portrait. The site crops with `object-fit: cover`. |
| Hero image | 1920 × 1080 px | `.png` | Wide image for the landing page. |
| Banner | 1920 × 640 px | `.png` | Wide page banner or edition header image. |
| Figure/illustration | 1600 × 1000 px | `.png` | Used in text sections. |
| Logo | 1200 × 600 px or 1200 × 800 px | `.png` or `.svg` | Use transparent background when available. |

## Naming convention

```text
assets/img/YYYY/category/YYYY_category_subject_variant.ext
```

Examples:

```text
assets/img/2026/speakers/2026_speaker_mason-a-porter_headshot.jpg
assets/img/2024/speakers/2024_speaker_adilson-e-motter_headshot.jpg
assets/img/2023/banners/2023_banner_netsci23-banner.png
assets/img/common/logos/common_logo_physnet-mark.png
```

The complete checklist is in `sources/image-replacement-manifest.csv`.

## Transparent logo and archive-width images

The main PhysNet mark is stored as a transparent PNG at:

```text
assets/img/common/logos/common_logo_physnet-mark.png
```

A duplicate transparent reference copy is stored as:

```text
assets/img/common/logos/common_logo_physnet-mark-transparent.png
```

Past-edition archive pages use fixed content-width image slots that scale to the screen width:

```text
assets/img/2023/banners/2023_banner_netsci23-banner.png
assets/img/2023/hero/2023_hero_physical-network-render.png
assets/img/2024/banners/2024_banner_netsci24-banner.png
assets/img/2024/hero/2024_hero_physical-network-render.png
assets/img/2025/banners/2025_banner_netsci25.png
assets/img/2025/hero/2025_hero_physical-network-render.png
```

Overwrite these files directly with manually downloaded and edited images. Recommended target sizes are 1920 x 640 for banners and 1920 x 1080 for hero images.

## Landing-title assets

The edition landing-title images are stored in `assets/img/common/landing/`.
They have transparent backgrounds and are safe to place on white, pale blue, or other site backgrounds.

Replace only these files if the title treatment changes:

- `2023_landing-title-logo-left-transparent.png`
- `2024_landing-title-logo-left-transparent.png`
- `2025_landing-title-logo-left-transparent.png`
- `2026_landing-title-logo-left-transparent.png`

Recommended dimensions: `1920 x 720 px` with transparent background.
