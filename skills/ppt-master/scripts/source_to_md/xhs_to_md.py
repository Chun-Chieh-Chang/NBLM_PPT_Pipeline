#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
xhs_to_md.py - Xiaohongshu (小红书 / RED) Note to Markdown Converter

Uses Playwright for browser-based extraction of Xiaohongshu notes.
Supports both direct URL and share-text input.

Usage:
    python xhs_to_md.py <url_or_share_text> [-o output.md]
    python xhs_to_md.py "https://www.xiaohongshu.com/explore/ABC123"
    python xhs_to_md.py "算法面经... [http://xhslink.com/o/ABC123] ..."

Dependencies:
    pip install playwright requests beautifulsoup4
    playwright install chromium

Installation — Playwright:
    pip install playwright
    playwright install chromium

    If playwright fails to install, install xhs-extractor instead:
    pip install xhs-extractor
    Then use its CLI: python -m xhs_extractor_module.cli

Notes:
    - First run requires logging into Xiaohongshu via the Playwright browser.
      Login state is persisted in ~/.notebooklm/xhs_cookies.json or
      <project_dir>/.xhs_cookies.json.
    - This script uses a lightweight approach (no Streamlit UI). For full
      features (OCR, batch download), consider using xhs-extractor directly.
"""

import argparse
import datetime
import json
import os
import re
import sys
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("[WARN] BeautifulSoup not installed. Install: pip install beautifulsoup4", file=sys.stderr)

# Prefer xhs-extractor's CLI if available; otherwise fall back to Playwright.
_XHS_EXTRACTOR_AVAILABLE = False
try:
    import subprocess
    _XHS_EXTRACTOR_AVAILABLE = True
except ImportError:
    pass


def _find_cookie_path(project_root: str = ".") -> Path | None:
    """Find persisted login cookie from xhs-extractor or Playwright."""
    candidates = [
        Path(project_root) / ".xhs_cookies.json",
        Path.home() / ".notebooklm" / "xhs_state.json",
        Path.home() / ".notebooklm" / "xhs_cookies.json",
        Path.home() / ".xhs_cookie.txt",
    ]
    for p in candidates:
        if p.exists():
            return p
    return None


def _extract_via_xhs_extractor_cli(note_url: str, output_dir: Path) -> Path | None:
    """Try to extract using xhs-extractor CLI if available."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "xhs_extractor_module.cli",
             "--url", note_url,
             "--output-dir", str(output_dir),
             "--no-image", "--no-ocr"],
            capture_output=True, text=True, timeout=120,
        )
        if result.returncode == 0:
            # Find the generated .md file
            md_files = list(output_dir.glob("*.md"))
            if md_files:
                return md_files[0]
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return None


def _extract_via_playwright(note_input: str, output_dir: Path, headless: bool = True) -> tuple[str, list[str], dict]:
    """Extract Xiaohongshu note content using Playwright.

    Returns:
        (markdown_content, image_paths_dict, metadata_dict)
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("[ERROR] Playwright not installed.", file=sys.stderr)
        print("Run: pip install playwright && playwright install chromium", file=sys.stderr)
        sys.exit(1)

    # Parse input: could be URL or share text containing URL
    url = note_input
    # Try to extract URL from share text
    url_match = re.search(r'(https?://[^\s]+)', note_input)
    if url_match:
        url = url_match.group(1)

    # Normalize xhs short links
    url = url.replace("http://", "https://")

    markdown_parts = []
    image_paths = []
    metadata = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 900},
        )

        # Load cookies if available
        cookie_path = _find_cookie_path(str(output_dir))
        if cookie_path and cookie_path.exists():
            try:
                if cookie_path.suffix == ".txt":
                    # Cookie file from xhs-extractor
                    with open(cookie_path, 'r', encoding='utf-8') as f:
                        cookies_raw = f.read().strip()
                    if cookies_raw:
                        cookies = [{"name": "login", "value": cookies_raw,
                                    "domain": ".xiaohongshu.com", "path": "/"}]
                        context.add_cookies(cookies)
                else:
                    with open(cookie_path, 'r', encoding='utf-8') as f:
                        cookies_data = json.load(f)
                    if isinstance(cookies_data, list):
                        context.add_cookies(cookies_data)
                    elif isinstance(cookies_data, dict) and "cookies" in cookies_data:
                        context.add_cookies(cookies_data["cookies"])
            except Exception:
                pass  # Continue without cookies

        page = context.new_page()

        try:
            print(f"[INFO] Navigating to {url} ...", file=sys.stderr)
            page.goto(url, wait_until="networkidle", timeout=30000)

            # Wait for content to render
            page.wait_for_timeout(3000)

            # Check if login is required
            login_btn = page.query_selector(".xhs-login-dialog .confirm-btn, .xhs-login-dialog button")
            if login_btn:
                print("[WARN] Login required. Please log in manually in the browser window.", file=sys.stderr)
                print("[INFO] Press Enter after logging in...", file=sys.stderr)
                input()  # Block until user logs in

            # Extract note content
            # Title
            title_el = page.query_selector(".note-header .title, .note-header .note-title, h1, .title")
            title = title_el.inner_text().strip() if title_el else "Untitled"

            # Content/description
            desc_el = page.query_selector(".note-content, .desc, .content, .note-text")
            description = desc_el.inner_text().strip() if desc_el else ""

            # Images
            images = page.query_selector_all(".note-img img, .image-list img, [class*='image'] img, .cover-img")
            image_urls = []
            for img in images[:20]:  # Limit to 20 images
                src = img.get_attribute("src") or img.get_attribute("data-src") or ""
                if src:
                    image_urls.append(src)

            # Author info
            author_el = page.query_selector(".author .name, .user-name, .nickname")
            author = author_el.inner_text().strip() if author_el else ""

            # Date
            date_el = page.query_selector(".note-header .time, .publish-time, .date")
            publish_date = date_el.inner_text().strip() if date_el else ""

            # Likes/comments
            interact_el = page.query_selector(".interact-info, .stats, .like-count")
            stats = interact_el.inner_text().strip() if interact_el else ""

            metadata = {
                "title": title,
                "author": author,
                "publish_date": publish_date,
                "stats": stats,
                "source_url": url,
                "image_count": len(image_urls),
            }

            # Build markdown
            markdown_parts.append(f"# {title}\n")
            if description:
                markdown_parts.append(f"\n{description}\n")

            if image_urls:
                markdown_parts.append(f"\n## 圖片 ({len(image_urls)}張)\n")
                for i, img_url in enumerate(image_urls, 1):
                    markdown_parts.append(f"![圖片 {i}]({img_url})\n")

            if stats:
                markdown_parts.append(f"\n**互動數據**: {stats}\n")

            markdown_parts.append(f"\n---\n\n> 來源: {url}")
            markdown_parts.append(f"> 作者: {author or '未知'}")
            if publish_date:
                markdown_parts.append(f"> 發布日期: {publish_date}")

        finally:
            browser.close()

    return "\n".join(markdown_parts), image_urls, metadata


def main():
    parser = argparse.ArgumentParser(
        description="Convert Xiaohongshu (小红书) notes to Markdown.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "https://www.xiaohongshu.com/explore/ABC123"
  %(prog)s "算法面经... [http://xhslink.com/o/ABC123] 复制后打开【小红书】查看笔记！"
  %(prog)s <url> -o output.md
        """,
    )
    parser.add_argument(
        "input", help="Xiaohongshu URL or share text"
    )
    parser.add_argument(
        "-o", "--output", default=None,
        help="Output Markdown file (default: stdout)",
    )
    parser.add_argument(
        "--headless", action="store_true", default=False,
        help="Run browser in headless mode (requires prior login)",
    )
    parser.add_argument(
        "--force-xhs-extractor", action="store_true", default=False,
        help="Force using xhs-extractor CLI instead of Playwright",
    )

    args = parser.parse_args()

    # Determine output directory
    output_path = Path(args.output) if args.output else None
    output_dir = (output_path.parent if output_path else Path.cwd())

    # Try xhs-extractor CLI first if available
    if not args.headless and _XHS_EXTRACTOR_AVAILABLE and not args.force_xhs_extractor:
        result_file = _extract_via_xhs_extractor_cli(args.input, output_dir)
        if result_file and result_file.exists():
            content = result_file.read_text(encoding="utf-8")
            if args.output:
                output_path.write_text(content, encoding="utf-8")
                print(f"[OK] Written to {output_path.resolve()}")
            else:
                print(content)
            return

    # Fallback to Playwright
    print("[INFO] Using Playwright for extraction...", file=sys.stderr)
    md_content, image_urls, metadata = _extract_via_playwright(
        args.input, output_dir, headless=args.headless
    )

    # Add metadata header
    meta_lines = [
        "<!--",
        f"  Source: {metadata.get('source_url', 'N/A')}",
        f"  Title: {metadata.get('title', 'N/A')}",
        f"  Author: {metadata.get('author', 'N/A')}",
        f"  Published: {metadata.get('publish_date', 'N/A')}",
        f"  Images: {metadata.get('image_count', 0)}",
        f"  Crawled: {datetime.datetime.now().isoformat()}",
        "-->",
        "",
    ]

    final_output = "\n".join(meta_lines) + md_content

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(final_output, encoding="utf-8")
        print(f"[OK] Written to {out_path.resolve()} ({len(final_output)} chars)")
    else:
        print(final_output)


if __name__ == "__main__":
    main()
