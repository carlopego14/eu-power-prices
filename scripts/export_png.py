"""Export each page of the Power BI PDF report to a PNG image for the README.

Usage (from the project folder):
    pip install pymupdf
    python scripts/export_png.py
"""
from pathlib import Path

import fitz  # PyMuPDF

PROJECT = Path(__file__).resolve().parent.parent
PDF_PATH = PROJECT / "report" / "eu-power-prices-report.pdf"
OUT_DIR = PROJECT / "images"
NAMES = ["overview.png", "daily-profile.png", "extremes-data-quality.png"]

OUT_DIR.mkdir(exist_ok=True)
doc = fitz.open(PDF_PATH)
print(f"PDF pages: {doc.page_count}")

for page, name in zip(doc, NAMES):
    pix = page.get_pixmap(dpi=150)
    pix.save(OUT_DIR / name)
    print(f"Saved {OUT_DIR / name} ({pix.width}x{pix.height} px)")
