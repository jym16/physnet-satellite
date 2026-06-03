# Data directory

This directory contains the structured source data used to generate the Physical Networks website.

## Files

```text
series.yml              # Series-level settings and homepage mode
editions.yml            # Generated compact edition index
editions.json           # Generated compact edition index
editions/YYYY.yml       # Source-of-truth metadata for each edition
```

Edit `series.yml` to switch the homepage between the current-edition mode and archive mode. Edit `editions/YYYY.yml` to update the program, speakers, organizers, keywords, and source notes for a specific year.

After editing data, regenerate pages from the repository root:

```bash
python scripts/validate_data.py
python scripts/generate_landing_images.py --all
python scripts/build_pages.py
```
