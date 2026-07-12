#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
universal_to_md.py - Universal File to Markdown Converter (Fallback)

Uses Microsoft MarkItDown as a universal converter for files not handled by
dedicated scripts. Covers edge cases: ZIP archives, YouTube URLs, and files
with unusual formats.

Also supports LLM-powered image descriptions when OPENAI_API_KEY is set.

Usage:
    python universal_to_md.py <file_or_url> [-o output.md]
    python universal_to_md.py data.zip
    python universal_to_md.py https://www.youtube.com/watch?v=xxx
    python universal_to_md.py photo.jpg --llm-desc   # requires OPENAI_API_KEY

Dependencies:
    pip install markitdown[all]

    For LLM image descriptions:
    pip install openai
    export OPENAI_API_KEY="sk-..."

Installation:
    pip install 'markitdown[all]'
"""

import argparse
import os
import sys
from pathlib import Path

try:
    import markitdown
except ImportError:
    print("[ERROR] markitdown not installed.", file=sys.stderr)
    print("Run: pip install 'markitdown[all]'", file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Universal file-to-Markdown converter using Microsoft MarkItDown.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s archive.zip
  %(prog)s https://www.youtube.com/watch?v=dQw4w9WgXcQ
  %(prog)s photo.jpg --llm-desc
  %(prog)s document.pdf -o output.md

Supported formats (via MarkItDown):
  PDF, DOCX, PPTX, XLSX, EPUB, HTML, ZIP, CSV, JSON, XML
  YouTube URLs, Images (with optional LLM descriptions)
        """,
    )
    parser.add_argument(
        "input", help="File path or URL to convert"
    )
    parser.add_argument(
        "-o", "--output", default=None,
        help="Output Markdown file (default: stdout)",
    )
    parser.add_argument(
        "--llm-desc", action="store_true", default=False,
        help="Use LLM (OpenAI) to generate image descriptions. Requires OPENAI_API_KEY.",
    )
    parser.add_argument(
        "--llm-model", default="gpt-4o",
        help="LLM model for image descriptions. Default: gpt-4o",
    )
    parser.add_argument(
        "--llm-prompt", default=None,
        help="Custom prompt for image descriptions.",
    )

    args = parser.parse_args()

    # Configure LLM client if requested
    llm_client = None
    llm_model = None
    llm_prompt = args.llm_prompt

    if args.llm_desc:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("[WARN] --llm-desc requires OPENAI_API_KEY environment variable.", file=sys.stderr)
            print("         Image descriptions will be skipped.", file=sys.stderr)
        else:
            try:
                from openai import OpenAI
                llm_client = OpenAI(api_key=api_key)
                llm_model = args.llm_model
            except ImportError:
                print("[WARN] openai package not installed. Install: pip install openai", file=sys.stderr)
                print("        Image descriptions will be skipped.", file=sys.stderr)

    # Create converter
    md = markitdown.MarkItDown(
        llm_client=llm_client,
        llm_model=llm_model,
        llm_prompt=llm_prompt,
    )

    input_path = Path(args.input)

    try:
        # Determine conversion method based on input type
        if input_path.is_file():
            # Local file
            result = md.convert_local(str(input_path))
        elif args.input.startswith(("http://", "https://")):
            # URL
            result = md.convert_uri(args.input)
        else:
            # Try local file first, then URI
            if input_path.exists():
                result = md.convert_local(str(input_path))
            else:
                result = md.convert_uri(args.input)

        content = result.text_content

        if args.output:
            out_path = Path(args.output)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(content, encoding="utf-8")
            print(f"[OK] Written to {out_path.resolve()} ({len(content)} chars)")
        else:
            print(content)

    except Exception as e:
        print(f"[ERROR] Conversion failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
