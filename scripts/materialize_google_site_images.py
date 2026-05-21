#!/usr/bin/env python3
"""Download Google Sites images listed in sources/google-site-image-manifest.yml.

The Quarto pages intentionally render the original remote image URLs. If these URLs are
accessible from your machine, this script can also save local copies under assets/img/<year>/.
Some Google Sites image URLs may return HTTP 403 outside the original page context; in that
case, download the image manually from the browser and save it to the listed local_target.
"""
from __future__ import annotations
from pathlib import Path
import mimetypes
import sys
import time
import urllib.request
import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "sources" / "google-site-image-manifest.yml"


def main() -> int:
    entries = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ("User-Agent", "Mozilla/5.0"),
        ("Referer", "https://sites.google.com/"),
    ]
    ok = 0
    failed = []
    for entry in entries:
        target = ROOT / entry["local_target"]
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            with opener.open(entry["source_url"], timeout=30) as response:
                data = response.read()
                content_type = response.headers.get("Content-Type", "")
        except Exception as exc:
            failed.append((entry["name"], str(exc)))
            continue
        # Preserve a sensible extension if the returned content type is known.
        ext = mimetypes.guess_extension(content_type.split(";")[0].strip()) or target.suffix
        if ext and ext != target.suffix:
            target = target.with_suffix(ext)
        target.write_bytes(data)
        ok += 1
        time.sleep(0.2)
    print(f"Downloaded {ok} images.")
    if failed:
        print("Failed downloads:")
        for name, err in failed:
            print(f"- {name}: {err}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
