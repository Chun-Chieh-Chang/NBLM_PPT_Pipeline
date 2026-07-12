#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
image_to_md.py - Image / PDF (scanned) to Markdown Converter

Uses Kreuzberg for intelligent OCR and text extraction from images and scanned PDFs.
Supports JPEG, PNG, GIF, WebP, BMP, TIFF, and scanned PDF files.

Usage:
    python image_to_md.py <image_file> [-o output.md] [--language chi_sim+eng]
    python image_to_md.py image1.jpg image2.png -o combined.md

Dependencies:
    pip install kreuzberg
    System: tesseract-ocr (see installation guide below)

Installation — Kreuzberg + Tesseract:
    pip install kreuzberg

    Windows:
        choco install tesseract tesseract-lang  # Chocolatey
        # Or download from https://github.com/UB-Mannheim/tesseract/wiki

    macOS:
        brew install tesseract tesseract-lang

    Ubuntu/Debian:
        sudo apt install tesseract-ocr tesseract-ocr-chi-sim tesseract-ocr-eng
"""

import argparse
import sys
from pathlib import Path

try:
    from kreuzberg.shared import PSMMode
    from kreuzberg import extract_file_sync
except ImportError:
    print("[ERROR] Kreuzberg not installed.", file=sys.stderr)
    print("Run: pip install kreuzberg", file=sys.stderr)
    sys.exit(1)


SUPPORTED_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff", ".tif",
    ".pdf",  # scanned PDFs only
}


def _detect_language(lang_str: str | None) -> str:
    """Return language string for Tesseract. Default: chi_sim+eng for CJK users."""
    if lang_str:
        return lang_str
    return "chi_sim+eng"


def _extract_image(image_path: Path, language: str) -> tuple[str, str]:
    """Extract text from an image file using Kreuzberg OCR.

    Returns:
        (markdown_content, metadata_json)
    """
    result = extract_file_sync(
        str(image_path),
        language=language,
        psm=PSMMode.AUTO,
    )
    return result.content, result.metadata.model_dump_json() if hasattr(result, 'metadata') and result.metadata else "{}"


def _extract_scanned_pdf(pdf_path: Path, language: str) -> tuple[str, str]:
    """Extract text from a scanned PDF using Kreuzberg OCR.

    Returns:
        (markdown_content, metadata_json)
    """
    result = extract_file_sync(
        str(pdf_path),
        language=language,
        force_ocr=True,  # force OCR for scanned PDFs
    )
    return result.content, result.metadata.model_dump_json() if hasattr(result, 'metadata') and result.metadata else "{}"


def main():
    parser = argparse.ArgumentParser(
        description="Convert images / scanned PDFs to Markdown using OCR.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s photo.jpg
  %(prog)s scan.pdf --language eng
  %(prog)s img1.jpg img2.png -o output.md
  %(prog)s scan.pdf --language chi_sim+eng --psm single-column
        """,
    )
    parser.add_argument(
        "files", nargs="+", help="Image files or scanned PDF(s) to process"
    )
    parser.add_argument(
        "-o", "--output", default=None,
        help="Output Markdown file (default: stdout)",
    )
    parser.add_argument(
        "--language", default=None,
        help="OCR language(s) for Tesseract (e.g., eng, chi_sim, chi_sim+eng). Default: auto-detect based on system locale.",
    )
    parser.add_argument(
        "--psm", default="auto",
        choices=["auto", "single-column", "single-line", "single-word", "osp_uniform"],
        help="Page segmentation mode. Default: auto",
    )
    parser.add_argument(
        "--force-ocr", action="store_true", default=False,
        help="Force OCR even for searchable PDFs",
    )

    args = parser.parse_args()

    # Map PSM string to enum
    psm_map = {
        "auto": PSMMode.AUTO,
        "single-column": PSMMode.SINGLE_COLUMN,
        "single-line": PSMMode.SINGLE_LINE,
        "single-word": PSMMode.SINGLE_WORD,
        "osp-uniform": PSMMode.OSP_UNIFORM,
    }
    psm_mode = psm_map.get(args.psm, PSMMode.AUTO)

    language = _detect_language(args.language)

    outputs = []

    for file_path in args.files:
        path = Path(file_path)
        if not path.exists():
            print(f"[WARN] File not found, skipping: {path}", file=sys.stderr)
            continue

        ext = path.suffix.lower()
        if ext not in SUPPORTED_EXTENSIONS:
            print(f"[WARN] Unsupported format '{ext}', skipping: {path}", file=sys.stderr)
            continue

        try:
            if ext == ".pdf":
                content, metadata = _extract_scanned_pdf(path, language)
            else:
                content, metadata = _extract_image(path, language)
        except Exception as e:
            print(f"[ERROR] Failed to process {path}: {e}", file=sys.stderr)
            continue

        # Add source header
        source_header = f"---\nsource: {path.resolve()}\nmetadata: {metadata}\n---\n\n"
        outputs.append(f"{source_header}{content}\n")

    if not outputs:
        print("[ERROR] No files were successfully processed.", file=sys.stderr)
        sys.exit(1)

    final_output = "\n".join(outputs)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(final_output, encoding="utf-8")
        print(f"[OK] Written to {out_path.resolve()} ({len(final_output)} chars)")
    else:
        print(final_output)


if __name__ == "__main__":
    main()
