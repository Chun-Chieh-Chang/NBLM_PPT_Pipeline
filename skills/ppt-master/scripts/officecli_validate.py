#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
officecli_validate.py - Validate and inspect PPTX using OfficeCLI

Runs OfficeCLI's built-in validation and issue detection on generated PPTX files.
Provides structured JSON output for automated quality gates.

Usage:
    python officecli_validate.py <project_path> [--check format|content|structure]
    python officecli_validate.py projects/my-deck --check issues
    python officecli_validate.py projects/my-deck --json

Prerequisites:
    Install OfficeCLI binary:
        macOS/Linux: curl -fsSL https://d.officecli.ai/install.sh | bash
        Windows:     irm https://d.officecli.ai/install.ps1 | iex

    Verify: officecli --version

Dependencies:
    None (external binary only)
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path


def check_officecli_available() -> bool:
    """Check if OfficeCLI binary is available."""
    try:
        result = subprocess.run(
            ["officecli", "--version"],
            capture_output=True, text=True, timeout=10,
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def run_officecli(args: list[str], cwd: str | None = None, timeout: int = 120) -> tuple[int, str, str]:
    """Run an OfficeCLI command and return (returncode, stdout, stderr)."""
    result = subprocess.run(
        ["officecli"] + args,
        capture_output=True, text=True, timeout=timeout, cwd=cwd,
    )
    return result.returncode, result.stdout, result.stderr


def validate_pptx(pptx_path: Path, check_type: str = "all") -> dict:
    """Validate a PPTX file using OfficeCLI.

    Args:
        pptx_path: Path to the .pptx file
        check_type: One of 'all', 'format', 'content', 'structure', 'issues'

    Returns:
        Dict with validation results
    """
    results = {
        "file": str(pptx_path.resolve()),
        "valid": True,
        "checks": {},
        "issues": [],
    }

    # 1. Schema validation
    rc, stdout, stderr = run_officecli(["validate", str(pptx_path)])
    results["checks"]["schema_valid"] = rc == 0
    if rc != 0:
        results["valid"] = False
        results["issues"].append({"type": "schema", "severity": "error", "message": stderr.strip()})

    # 2. Issue detection
    check_flag = ""
    if check_type != "all":
        check_flag = f"--type {check_type}"

    rc, stdout, stderr = run_officecli(["view", str(pptx_path), "issues", check_flag])
    if rc == 0 and stdout.strip():
        issues_text = stdout.strip()
        # Parse issue lines (OfficeCLI outputs one issue per line)
        for line in issues_text.split("\n"):
            line = line.strip()
            if not line:
                continue
            # Try to parse as JSON first
            try:
                issue = json.loads(line)
                results["issues"].append(issue)
            except json.JSONDecodeError:
                # Fallback: treat as plain text issue
                results["issues"].append({
                    "type": "general",
                    "severity": "warning",
                    "message": line,
                })

    # 3. Structure analysis
    rc, stdout, stderr = run_officecli([
        "view", str(pptx_path), "outline", "--json"
    ])
    if rc == 0:
        try:
            results["checks"]["outline"] = json.loads(stdout)
        except json.JSONDecodeError:
            results["checks"]["outline_raw"] = stdout

    # 4. Statistics
    rc, stdout, stderr = run_officecli([
        "view", str(pptx_path), "stats"
    ])
    if rc == 0:
        results["checks"]["stats"] = stdout.strip()

    # 5. HTML render check (verifies rendering engine works)
    rc, stdout, stderr = run_officecli([
        "view", str(pptx_path), "html"
    ])
    results["checks"]["html_renderable"] = rc == 0

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Validate PPTX files using Microsoft OfficeCLI.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s projects/my-deck          # Full validation
  %(prog)s projects/my-deck --check format   # Format issues only
  %(prog)s projects/my-deck --json            # JSON output
        """,
    )
    parser.add_argument(
        "path", help="Project directory or PPTX file path"
    )
    parser.add_argument(
        "--check", default="all",
        choices=["all", "format", "content", "structure", "issues"],
        help="Type of check to perform. Default: all",
    )
    parser.add_argument(
        "--json", action="store_true", default=False,
        help="Output results as JSON",
    )

    args = parser.parse_args()

    # Check OfficeCLI availability
    if not check_officecli_available():
        print("[ERROR] OfficeCLI not found.", file=sys.stderr)
        print("Install: curl -fsSL https://d.officecli.ai/install.sh | bash", file=sys.stderr)
        print("         (Windows: irm https://d.officecli.ai/install.ps1 | iex)", file=sys.stderr)
        sys.exit(1)

    # Resolve target
    path = Path(args.path)
    if not path.exists():
        print(f"[ERROR] Path not found: {path}", file=sys.stderr)
        sys.exit(1)

    # Find PPTX file
    if path.suffix.lower() == ".pptx":
        pptx_file = path
    else:
        # Look for .pptx in exports/ or project root
        exports_dir = path / "exports"
        if exports_dir.exists():
            pptx_files = list(exports_dir.glob("*.pptx"))
            if pptx_files:
                pptx_file = max(pptx_files, key=lambda f: f.stat().st_mtime)
            else:
                pptx_files = list(path.glob("*.pptx"))
                pptx_file = max(pptx_files, key=lambda f: f.stat().st_mtime) if pptx_files else None
        else:
            pptx_files = list(path.glob("*.pptx"))
            pptx_file = max(pptx_files, key=lambda f: f.stat().st_mtime) if pptx_files else None

        if not pptx_file:
            print(f"[ERROR] No .pptx file found in {path}", file=sys.stderr)
            sys.exit(1)

    print(f"[INFO] Validating: {pptx_file.resolve()}", file=sys.stderr)

    # Run validation
    results = validate_pptx(pptx_file, args.check)

    # Output
    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(f"\n{'='*50}")
        print(f"PPTX Validation Report")
        print(f"{'='*50}")
        print(f"File: {results['file']}")
        print(f"Valid: {'Yes' if results['valid'] else 'No'}")
        print(f"Issues found: {len(results['issues'])}")

        for check_name, check_result in results["checks"].items():
            if isinstance(check_result, bool):
                status = "PASS" if check_result else "FAIL"
                print(f"  [{status}] {check_name}")
            elif isinstance(check_result, str):
                print(f"  [INFO] {check_name}: {check_result[:100]}...")

        if results["issues"]:
            print(f"\nIssues:")
            for issue in results["issues"]:
                severity = issue.get("severity", "warning").upper()
                msg = issue.get("message", issue.get("description", "Unknown issue"))
                print(f"  [{severity}] {msg}")

    # Exit code based on validity
    sys.exit(0 if results["valid"] else 1)


if __name__ == "__main__":
    main()
