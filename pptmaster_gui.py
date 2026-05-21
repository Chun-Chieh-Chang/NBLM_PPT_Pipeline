# -*- coding: utf-8 -*-
"""
PPT Master Dashboard - GUI Entry Point
Usage: python pptmaster_gui.py
"""

import sys
import os
import webbrowser
import threading
import time
from pathlib import Path

# Insert local directories into sys.path to guarantee import resolution
root_dir = Path(__file__).resolve().parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

# Force sys.stdout and sys.stderr to UTF-8 encoding on Windows to prevent UnicodeEncodeError
if sys.platform.startswith('win'):
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass

def check_and_deploy_env():
    """
    Automatically check and deploy dependencies before starting project.
    """
    critical_modules = {
        "flask": "flask",
        "pptx": "python-pptx",
        "fitz": "PyMuPDF",
        "edgeTTS": "edge-tts",
        "PIL": "Pillow",
        "openpyxl": "openpyxl",
        "requests": "requests",
        "bs4": "beautifulsoup4",
        "mammoth": "mammoth"
    }
    missing_packages = []
    for mod_name, pkg_name in critical_modules.items():
        try:
            # edgeTTS uses edge-tts, we import edgeTTS as testing name
            if mod_name == "edgeTTS":
                import edgeTTS
            else:
                __import__(mod_name)
        except ImportError:
            missing_packages.append(pkg_name)
            
    if missing_packages:
        print("=" * 70)
        print(f"[環境部署] 🔍 偵測到系統缺少必要 Python 依賴套件: {', '.join(missing_packages)}")
        print("[環境部署] ⚡ 正在為您自動執行環境部署與安裝 (pip install)...")
        print("=" * 70)
        
        req_file = root_dir / "requirements.txt"
        if not req_file.exists():
            print(f"[環境部署] ❌ 錯誤: 找不到 requirements.txt 檔案，無法自動安裝！")
            return False
            
        import subprocess
        try:
            # Use sys.executable to run pip install
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req_file)])
            print("\n[環境部署] 🎉 恭喜！所有必要環境依賴套件已自動下載並部署完畢！")
            print("=" * 70)
            return True
        except subprocess.CalledProcessError as e:
            print(f"\n[環境部署] ❌ 自動安裝失敗。錯誤代碼: {e.returncode}")
            print("[環境部署] 請嘗試手動在終端機中執行：")
            print(f"  pip install -r requirements.txt")
            print("=" * 70)
            return False
    else:
        print("[環境部署] ✅ 經自動檢查，所有必要 Python 依賴套件均已完備！")
        return True

# Check and deploy dependencies
check_and_deploy_env()

from gui.backend.app import start_server

def launch_browser():
    # Allow 1.5 seconds for Flask server to initialize
    time.sleep(1.5)
    url = "http://127.0.0.1:7070/"
    print(f"\n[GUI] Launching default web browser to: {url}")
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"[GUI] Warning: Could not automatically open browser: {e}")
        print(f"[GUI] Please open your browser manually and visit: {url}")

if __name__ == '__main__':
    # Banner and startup output
    print("=" * 70)
    print("        NBLM_PPT_Pipeline - PPT MASTER DASHBOARD")
    print("        ========================================")
    print("        A Native DrawingML PowerPoint Sync & Audio Pipeline")
    print("=" * 70)
    print(f"[GUI] Project directory: {root_dir}")
    print("[GUI] Spawning browser thread...")
    
    # Start browser launch thread
    browser_thread = threading.Thread(target=launch_browser, daemon=True)
    browser_thread.start()
    
    print("[GUI] Launching Flask server on 127.0.0.1:7070...")
    print("[GUI] Press Ctrl+C in this terminal to shutdown the server cleanly.")
    print("-" * 70)
    
    try:
        start_server(port=7070)
    except KeyboardInterrupt:
        print("\n[GUI] Shutting down local server. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n[GUI] Error starting server: {e}")
        sys.exit(1)
