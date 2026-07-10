# -*- coding: utf-8 -*-
"""
PPT Master Dashboard - Flask Backend
"""

import sys
import os
import re
import shutil
import subprocess
import json
import time
import urllib.request
import atexit
import io
from pathlib import Path
from datetime import datetime

# Configure Python path to find skills scripts
root_dir = Path(__file__).resolve().parent.parent.parent
scripts_dir = root_dir / "skills" / "ppt-master" / "scripts"
if str(scripts_dir) not in sys.path:
    sys.path.insert(0, str(scripts_dir))

# Force sys.stdout and sys.stderr to UTF-8 encoding on Windows to prevent UnicodeEncodeError
if sys.platform.startswith('win'):
    try:
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
            if mod_name == "edgeTTS":
                # pyrefly: ignore [missing-import]
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
            
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req_file)])
            print("\n[環境部署] 🎉 恭喜！所有必要環境依賴套件已自動下載並部署完畢！")
            print("=" * 70)
            return True
        except subprocess.CalledProcessError as e:
            print(f"\n[環境部署] ❌ 自動安裝失敗。錯誤程式碼: {e.returncode}")
            print("[環境部署] 請嘗試手動在終端機中執行：")
            print(f"  pip install -r requirements.txt")
            print("=" * 70)
            return False
    else:
        print("[環境部署] ✅ 經自動檢查，所有必要 Python 依賴套件均已完備！")
        return True

# Check and deploy environment before executing Flask imports
check_and_deploy_env()

# pyrefly: ignore [missing-import]
from flask import Flask, jsonify, request, Response, render_template, send_from_directory, redirect

try:
    # pyrefly: ignore [missing-import]
    import project_utils
    # pyrefly: ignore [missing-import]
    from config import CANVAS_FORMATS
except ImportError:
    project_utils = None
    CANVAS_FORMATS = {}

app = Flask(
    __name__,
    template_folder=str(root_dir / "gui" / "frontend"),
    static_folder=str(root_dir / "gui" / "frontend"),
    static_url_path="/static"
)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.after_request
def add_header(r):
    # Disable caching globally for development to ensure prompt updates of HTML, JS, CSS and APIs
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

# Configuration
PROJECTS_DIR = root_dir / "projects"
ENV_FILE = root_dir / ".env"
ENV_EXAMPLE = root_dir / ".env.example"

# Track the active SVG Editor process
active_editor_process = None
active_editor_project = None

def cleanup_editor_on_exit():
    global active_editor_process
    if active_editor_process:
        try:
            active_editor_process.terminate()
        except Exception:
            pass
atexit.register(cleanup_editor_on_exit)

# Helpers
def get_python_executable():
    return sys.executable

def mask_api_key(key, val):
    if not val:
        return ""
    if "KEY" in key or "TOKEN" in key or "SECRET" in key:
        if len(val) <= 8:
            return "********"
        return f"{val[:4]}...{val[-4:]}"
    return val

def locate_project_path(name):
    """
    Locate a project directory in PROJECTS_DIR using a case-insensitive fallback strategy.
    Returns the resolved Path object.
    """
    project_path = PROJECTS_DIR / name
    if project_path.exists():
        return project_path.resolve()
        
    target_name_lower = name.lower()
    if PROJECTS_DIR.exists():
        matched_dirs = [item for item in PROJECTS_DIR.iterdir() if item.is_dir() and item.name.lower() == target_name_lower]
        if matched_dirs:
            return matched_dirs[0].resolve()
            
        matches = sorted(PROJECTS_DIR.glob(f"{name}_*"), key=lambda x: x.name.lower())
        if not matches:
            matches = sorted([item for item in PROJECTS_DIR.iterdir() if item.is_dir() and item.name.lower().startswith(target_name_lower + "_")], key=lambda x: x.name.lower())
        if matches:
            return matches[-1].resolve()
            
    return project_path

# HTML Page Routes
@app.route('/favicon.ico')
def route_favicon():
    # Return 204 No Content to suppress browser console 404 warnings cleanly
    return Response(status=204)

@app.route('/')
def route_index():
    return render_template('index.html')

@app.route('/project/<name>')
def route_project(name):
    return render_template('project.html', project_name=name)

@app.route('/project/<name>/edit')
def route_project_edit(name):
    global active_editor_process, active_editor_project
    
    # Locate project directory (case-insensitive fallback)
    project_path = locate_project_path(name)
            
    if not project_path.exists():
        return "Project not found", 404
        
    project_name = project_path.name
    
    # If the active editor is already running for this project, just redirect
    if active_editor_process and active_editor_project == project_name:
        if active_editor_process.poll() is None:
            return redirect("http://127.0.0.1:5050/")
            
    # Otherwise, shutdown any server currently on port 5050
    try:
        req = urllib.request.Request(
            "http://127.0.0.1:5050/api/shutdown",
            data=json.dumps({"reason": "switch_project"}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=1.0) as response:
            response.read()
        time.sleep(0.3)  # wait for port cleanup
    except Exception:
        pass
        
    # Terminate tracked process if it exists
    if active_editor_process:
        try:
            active_editor_process.terminate()
            active_editor_process.wait(timeout=1.0)
        except Exception:
            pass
        active_editor_process = None
        
    # Launch new SVG Editor server
    cmd = [
        get_python_executable(),
        str(scripts_dir / "svg_editor" / "server.py"),
        str(project_path),
        "--port", "5050",
        "--no-browser",
        "--live"  # Dynamic mode allows empty directory
    ]
    
    try:
        # Setup logs directory and capture server outputs to resolve blackbox failures
        logs_dir = root_dir / "logs"
        logs_dir.mkdir(exist_ok=True)
        log_file = open(logs_dir / "svg_editor.log", "a", encoding="utf-8")
        
        active_editor_process = subprocess.Popen(
            cmd,
            cwd=str(root_dir),
            stdout=log_file,
            stderr=log_file
        )
        active_editor_project = project_name
        
        # Wait for server to boot up and safely close parent log handle
        time.sleep(1.0)
        try:
            log_file.close()
        except Exception:
            pass
            
        return redirect("http://127.0.0.1:5050/")
    except Exception as e:
        return f"Failed to start SVG Editor server: {str(e)}", 500

@app.route('/settings')
def route_settings():
    return render_template('settings.html')

@app.route('/guide')
def route_guide():
    return render_template('usage_guide.html')

# API Routes
@app.route('/api/projects', methods=['GET'])
def api_projects_list():
    if not PROJECTS_DIR.exists():
        return jsonify([])
    
    projects = []
    for item in sorted(PROJECTS_DIR.iterdir()):
        if item.is_dir() and not item.name.startswith('.'):
            # Check if this is a project directory
            has_svg = (item / 'svg_output').exists()
            has_spec = any((item / f).exists() for f in ['design_spec.md', '設計規範與內容大綱.md', '設計規範.md', '設計規範與內容大綱.md', '設計規範.md', 'design_specification.md'])
            
            if has_svg or has_spec or (item / 'sources').exists() or (item / 'notes').exists():
                try:
                    info = project_utils.get_project_info(str(item)) if project_utils else {}
                except Exception as e:
                    info = {
                        'name': item.name,
                        'format': 'unknown',
                        'format_name': 'Unknown',
                        'svg_count': 0
                    }
                
                # Check actual state
                state = "Initialized"
                if (item / "exports").exists() and list((item / "exports").glob("*.pptx")):
                    state = "Exported"
                elif (item / "svg_output").exists() and len(list((item / "svg_output").glob("*.svg"))) > 0:
                    state = "Designing"
                elif (item / "notes" / "total.md").exists():
                    state = "Outline Ready"
                elif (item / "sources").exists() and len(list((item / "sources").glob("*"))) > 0:
                    state = "Sources Loaded"
                
                projects.append({
                    'dir_name': item.name,
                    'name': info.get('name', item.name),
                    'format': info.get('format', 'unknown'),
                    'format_name': info.get('format_name', 'Unknown'),
                    'date_formatted': info.get('date_formatted', 'Unknown Date'),
                    'svg_count': info.get('svg_count', 0),
                    'source_count': info.get('source_count', 0),
                    'state': state
                })
                
    return jsonify(projects)

@app.route('/api/projects/create', methods=['POST'])
def api_projects_create():
    data = request.json or {}
    name = data.get('name', '').strip()
    fmt = data.get('format', 'ppt169').strip()
    
    if not name:
        return jsonify({'error': 'Project name is required'}), 400
        
    # Clean project name
    clean_name = re.sub(r'[^a-zA-Z0-9_\-]', '', name)
    if not clean_name:
        return jsonify({'error': 'Invalid project name'}), 400
        
    # Standard format: name_format_YYYYMMDD.
    # The project_manager.py handles date suffix automatically.
    cmd = [
        get_python_executable(),
        str(scripts_dir / "project_manager.py"),
        "init",
        clean_name,
        "--format",
        fmt
    ]
    
    try:
        res = subprocess.run(cmd, cwd=str(root_dir), capture_output=True, text=True, encoding='utf-8', errors='replace')
        if res.returncode == 0:
            # Let's locate the newly created folder
            created_dir = None
            for item in PROJECTS_DIR.iterdir():
                if item.is_dir() and item.name.startswith(clean_name):
                    created_dir = item.name
            
            return jsonify({
                'success': True,
                'project_name': clean_name,
                'dir_name': created_dir or clean_name,
                'output': res.stdout
            })
        else:
            return jsonify({
                'error': f'Initialization script failed: {res.stderr or res.stdout}'
            }), 500
    except Exception as e:
        return jsonify({'error': f'Exception during execution: {str(e)}'}), 500

@app.route('/api/projects/<name>', methods=['DELETE'])
def api_projects_delete(name):
    project_path = locate_project_path(name)
            
    if not project_path.exists():
        # If the project folder already does not exist, treat it as successfully deleted (idempotent DELETE)
        return jsonify({'success': True, 'message': f'Project {name} already deleted or does not exist.'})
        
    try:
        # Safety precaution to prevent path traversal vulnerability
        resolved_path = project_path.resolve()
        resolved_projects_dir = PROJECTS_DIR.resolve()
        
        # Case-insensitive path prefix verification for Windows compatibility
        if not str(resolved_path).lower().startswith(str(resolved_projects_dir).lower()):
            return jsonify({'error': 'Security violation: Unauthorized path deletion attempt'}), 400
            
        # Clean up active SVG editor if we are deleting the currently edited project
        global active_editor_process, active_editor_project
        if active_editor_project and (active_editor_project == name or active_editor_project == resolved_path.name):
            if active_editor_process:
                try:
                    active_editor_process.terminate()
                    active_editor_process.wait(timeout=1.0)
                except Exception:
                    pass
                active_editor_process = None
                active_editor_project = None
            
        # Remove directory recursively
        shutil.rmtree(resolved_path)
        return jsonify({'success': True, 'message': f'Project {name} has been deleted.'})
    except Exception as e:
        return jsonify({'error': f'Failed to delete project folder: {str(e)}'}), 500

@app.route('/api/projects/<name>/info', methods=['GET'])
def api_project_info(name):
    # Locate project directory
    project_path = locate_project_path(name)
            
    if not project_path.exists():
        return jsonify({'error': 'Project not found'}), 404
        
    try:
        info = project_utils.get_project_info(str(project_path)) if project_utils else {}
    except Exception as e:
        return jsonify({'error': f'Failed to read info: {str(e)}'}), 500
        
    # Add files list
    sources_dir = project_path / "sources"
    source_files = []
    if sources_dir.exists():
        source_files = [f.name for f in sources_dir.iterdir() if f.is_file()]
        
    exports_dir = project_path / "exports"
    export_files = []
    if exports_dir.exists():
        export_files = [f.name for f in exports_dir.iterdir() if f.is_file()]
        
    info['source_files'] = source_files
    info['export_files'] = export_files
    info['dir_name'] = project_path.name
    
    # Check if NotebookLM animations.json exists
    info['has_notebooklm_sync'] = (project_path / "notes" / "animations.json").exists()
    
    # Check if total.md exists
    total_md_path = project_path / "notes" / "total.md"
    info['has_total_md'] = total_md_path.exists()
    if total_md_path.exists():
        try:
            info['total_md_size'] = total_md_path.stat().st_size
        except Exception:
            info['total_md_size'] = 0
            
    # Check if outline split has occurred (other .md files in notes/ besides total.md)
    notes_dir = project_path / "notes"
    has_split = False
    if notes_dir.exists():
        md_files = [f.name for f in notes_dir.iterdir() if f.is_file() and f.suffix.lower() == '.md' and f.name != 'total.md']
        if md_files:
            has_split = True
    info['has_split'] = has_split
            
    return jsonify(info)

@app.route('/api/projects/<name>/upload', methods=['POST'])
def api_project_upload(name):
    project_path = locate_project_path(name)
            
    if not project_path.exists():
        return jsonify({'error': 'Project not found'}), 404
        
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
        
    sources_dir = project_path / "sources"
    sources_dir.mkdir(parents=True, exist_ok=True)
    
    filename = secure_filename_local(file.filename)
    dest_path = sources_dir / filename
    
    try:
        file.save(str(dest_path))
        return jsonify({
            'success': True,
            'filename': filename,
            'size': dest_path.stat().st_size
        })
    except Exception as e:
        return jsonify({'error': f'Failed to save file: {str(e)}'}), 500

def secure_filename_local(name):
    # Simple secure filename implementation
    name = os.path.basename(name)
    name = re.sub(r'[^a-zA-Z0-9_\.\-]', '_', name)
    return name

@app.route('/api/projects/<name>/export', methods=['GET'])
def api_project_download_pptx(name):
    project_path = locate_project_path(name)
            
    if not project_path.exists():
        return jsonify({'error': 'Project not found'}), 404
        
    exports_dir = project_path / "exports"
    if not exports_dir.exists():
        return jsonify({'error': 'No exports found'}), 404
        
    export_files = sorted(exports_dir.glob("*.pptx"))
    if not export_files:
        # Check for HTML exports (for guizang styles)
        html_files = sorted(exports_dir.glob("*.html"))
        if html_files:
            return send_from_directory(str(exports_dir), html_files[-1].name, as_attachment=True)
        return jsonify({'error': 'No PPTX or HTML export file found'}), 404
        
    # Return the latest compiled pptx
    latest_pptx = export_files[-1]
    return send_from_directory(str(exports_dir), latest_pptx.name, as_attachment=True)

# SSE Pipeline execution
@app.route('/api/projects/<name>/run/<step>', methods=['GET', 'POST'])
def api_project_run_step(name, step):
    rebuild = request.args.get('rebuild', '').lower() == 'true'
    project_path = locate_project_path(name)
            
    if not project_path.exists():
        return jsonify({'error': 'Project not found'}), 404
        
    cmd_args = []
    
    # Read project format
    info_file = project_path / "project_info.json"
    project_format = ""
    if info_file.exists():
        try:
            import json
            with open(info_file, 'r', encoding='utf-8') as f:
                info = json.load(f)
                project_format = info.get('format', '')
        except:
            pass

    if project_format.startswith('guizang_'):
        if step == 'split':
            cmd_args = [
                get_python_executable(),
                str(scripts_dir / "guizang_pipeline.py"),
                str(project_path),
                "--style", project_format.replace('guizang_', '')
            ]
        else:
            def fake_success():
                yield f"data: [SUCCESS] Bypassed step {step} for HTML presentation.\\n\\n"
            return Response(stream_with_context(fake_success()), content_type='text/event-stream')
    elif step == 'split':
        cmd_args = [
            get_python_executable(),
            str(scripts_dir / "total_md_split.py"),
            str(project_path)
        ]
    elif step == 'image_gen':
        cmd_args = [
            get_python_executable(),
            str(scripts_dir / "image_gen.py"),
            "--manifest",
            str(project_path / "images" / "image_prompts.json"),
            "-o",
            str(project_path / "images")
        ]
    elif step == 'finalize':
        cmd_args = [
            get_python_executable(),
            str(scripts_dir / "finalize_svg.py"),
            str(project_path)
        ]
    elif step == 'export':
        cmd_args = [
            get_python_executable(),
            str(scripts_dir / "svg_to_pptx.py"),
            str(project_path),
            "-s", "final"
        ]
        # Check for sliced audio files
        audio_dir = project_path / "audio"
        if audio_dir.exists() and any(audio_dir.glob("*.mp3")):
            cmd_args.extend(["--recorded-narration", str(audio_dir)])
            
    elif step == 'notebooklm_setup':
        source = request.args.get('source', '')
        podcast = request.args.get('podcast', '')
        transcript = request.args.get('transcript', '')
        
        if not source:
            return jsonify({'error': 'NotebookLM Source file is required for setup phase'}), 400
            
        source_path = project_path / "sources" / source
        if not source_path.exists():
            return jsonify({'error': f'Source file {source} does not exist'}), 404
            
        cmd_args = [
            get_python_executable(),
            str(scripts_dir / "notebooklm_pipeline.py"),
            "--project",
            project_path.name,
            "--phase",
            "setup",
            "--source",
            str(source_path)
        ]
        
        if podcast:
            podcast_path = project_path / "sources" / podcast
            if podcast_path.exists():
                cmd_args.extend(["--podcast", str(podcast_path)])
            if transcript:
                trans_path = project_path / "sources" / transcript
                if trans_path.exists():
                    cmd_args.extend(["--transcript", str(trans_path)])
                    
    elif step == 'notebooklm_export':
        cmd_args = [
            get_python_executable(),
            str(scripts_dir / "notebooklm_pipeline.py"),
            "--project",
            project_path.name,
            "--phase",
            "export"
        ]
    elif step == 'skills_sync':
        cmd_args = [
            get_python_executable(),
            str(root_dir / "integrate_skills.py")
        ]
    else:
        return jsonify({'error': f'Unknown pipeline step: {step}'}), 400
        
    def generate_events():
        env = os.environ.copy()
        env["PYTHONUNBUFFERED"] = "1"
        env["PAGER"] = "cat"
        
        yield "data: [START] Running step '{}'...\n\n".format(step)
        
        # ─────────────────────────────────────────────────────────────
        # Step Preprocessing Logic
        # ─────────────────────────────────────────────────────────────
        
        if step == 'split':
            total_md = project_path / "notes" / "total.md"
            if rebuild:
                yield "data: [SYSTEM] 🔄 偵測到強制【全新乾淨重建】引數，正在清理舊有大綱與投影片...\n\n"
                if total_md.exists():
                    try:
                        total_md.unlink()
                    except Exception:
                        pass
                svg_dir = project_path / "svg_output"
                if svg_dir.exists():
                    try:
                        shutil.rmtree(svg_dir)
                        svg_dir.mkdir(parents=True, exist_ok=True)
                    except Exception:
                        pass
            if not total_md.exists():
                yield "data: [SYSTEM] 🔍 偵測到 notes/total.md 大綱不存在，正在自動掃描 sources/ 目錄...\n\n"
                sources_dir = project_path / "sources"
                source_files = list(sources_dir.glob("*")) if sources_dir.exists() else []
                source_files = [f for f in source_files if f.is_file() and not f.name.startswith(".")]
                
                if not source_files:
                    yield "data: [ERROR] ❌ 專案的 sources/ 目錄中無任何簡報素材。請先上傳 PDF, Word 或 Markdown 檔案後再執行此步驟！\n\n"
                    return
                
                # Check for MD file
                md_sources = [f for f in source_files if f.suffix.lower() in {".md", ".markdown"}]
                if md_sources:
                    primary_md = md_sources[0]
                    total_md.parent.mkdir(parents=True, exist_ok=True)
                    try:
                        shutil.copy2(primary_md, total_md)
                        yield "data: [SYSTEM] 📝 偵測到來源目錄中包含 Markdown 素材，已為您自動載入為 notes/total.md 大綱！\n\n"
                    except Exception as e:
                        yield "data: [EXCEPTION] 複製大綱檔案失敗: {}\n\n".format(str(e))
                        return
                else:
                    convertible = [f for f in source_files if f.suffix.lower() in {".docx", ".pdf", ".pptx", ".xlsx"}]
                    if convertible:
                        primary_file = convertible[0]
                        yield "data: [SYSTEM] 🔄 偵測到您上傳了檔案素材 {}，正在自動呼叫 project_manager.py 進行轉換...\n\n".format(primary_file.name)
                        
                        import_cmd = [
                            get_python_executable(),
                            str(scripts_dir / "project_manager.py"),
                            "import-sources",
                            str(project_path),
                            str(primary_file),
                            "--copy"
                        ]
                        
                        try:
                            res = subprocess.run(import_cmd, cwd=str(root_dir), capture_output=True, text=True, encoding='utf-8', errors='replace')
                            if res.returncode == 0:
                                md_files = list(sources_dir.glob("*.md"))
                                if md_files:
                                    primary_md = sorted(md_files, key=lambda x: x.stat().st_mtime)[-1]
                                    total_md.parent.mkdir(parents=True, exist_ok=True)
                                    shutil.copy2(primary_md, total_md)
                                    yield "data: [SYSTEM] 📝 素材轉換成功，已載入為 notes/total.md 大綱！\n\n"
                                else:
                                    yield "data: [ERROR] ❌ 轉換後未能在 sources/ 目錄下尋找到 Markdown 檔案！\n\n"
                                    return
                            else:
                                yield "data: [ERROR] ❌ 素材轉換失敗。指令碼輸出: {}\n\n".format(res.stderr or res.stdout)
                                return
                        except Exception as e:
                            yield "data: [EXCEPTION] 轉換素材出錯: {}\n\n".format(str(e))
                            return
                    else:
                        yield "data: [ERROR] ❌ 找不到可自動轉換的簡報素材 (PDF, DOCX, MD, PPTX)。\n\n"
                        return

            # Check if svg_output/ is empty
            svg_dir = project_path / "svg_output"
            svg_files = list(svg_dir.glob("*.svg")) if svg_dir.exists() else []
            if not svg_files:
                yield "data: [SYSTEM] 🎨 偵測到 svg_output/ 為空，正在自動解析 total.md 並為每一頁生成高對比度 Dark Mode 佔位 SVG 投影片...\n\n"
                
                headings = []
                try:
                    content = total_md.read_text(encoding='utf-8')
                    for line in content.splitlines():
                        m = re.match(r'^(#{1,3})\s*(.+?)\s*$', line.strip())
                        if m:
                            title = m.group(2).strip()
                            if title not in headings:
                                headings.append(title)
                except Exception as e:
                    yield "data: [EXCEPTION] 讀取/解析 total.md 大綱失敗: {}\n\n".format(str(e))
                    return
                
                if not headings:
                    yield "data: [ERROR] ❌ 無法在 notes/total.md 中解析出任何投影片標題 (必須以 #, ## 或 ### 開頭)。\n\n"
                    return
                
                svg_dir.mkdir(parents=True, exist_ok=True)
                
                def normalize_title(title_str: str) -> str:
                    if not title_str:
                        return ''
                    t = title_str.strip()
                    t = re.sub(r'[^0-9A-Za-z\u4e00-\u9fff]+', '_', t)
                    t = re.sub(r'_+', '_', t).strip('_')
                    return t
                
                created_count = 0
                for title in headings:
                    stem = normalize_title(title)
                    if not stem:
                        continue
                    mock_svg = svg_dir / f"{stem}.svg"
                    if not mock_svg.exists():
                        placeholder_svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="100%" height="100%">
  <!-- Slide Stem: {stem} -->
  <rect width="1280" height="720" fill="#0F172A"/> <!-- Slate 900 base background -->
  <text x="64" y="100" fill="#F1F5F9" font-family="sans-serif" font-size="36" font-weight="bold">{title}</text>
  <text x="64" y="180" fill="#94A3B8" font-family="sans-serif" font-size="18">Placeholder: Please write actual high-fidelity consulting card layout SVG here.</text>
</svg>'''
                        try:
                            mock_svg.write_text(placeholder_svg_content, encoding="utf-8")
                            created_count += 1
                        except Exception as e:
                            yield "data: [WARN] 無法寫入 SVG 佔位檔: {}\n\n".format(str(e))
                            
                yield "data: [SYSTEM] ✅ 已成功為 {} 個投影片大綱生成對應的 Slate 900 SVG 預設視覺骨架！\n\n".format(created_count)

        elif step == 'image_gen':
            manifest_path = project_path / "images" / "image_prompts.json"
            images_dir = project_path / "images"
            
            # If manifest does not exist, let's scan SVGs for referenced images
            if not manifest_path.exists():
                yield "data: [SYSTEM] 🔍 偵測到 images/image_prompts.json 不存在，正在掃描 svg_output/ 進行配圖分析...\n\n"
                
                referenced_images = []
                svg_dir = project_path / "svg_output"
                if svg_dir.exists():
                    for svg_path in svg_dir.glob("*.svg"):
                        try:
                            content = svg_path.read_text(encoding="utf-8")
                            matches = re.findall(r'(?:href|xlink:href)=["\'](?:images/)?([^"\']+\.(?:png|jpg|jpeg|webp))["\']', content)
                            for m in matches:
                                fname = os.path.basename(m)
                                if fname not in [item["filename"] for item in referenced_images]:
                                    referenced_images.append({
                                        "filename": fname,
                                        "svg_stem": svg_path.stem
                                    })
                        except Exception:
                            pass
                            
                if referenced_images:
                    manifest_data = {
                        "project": project_path.name,
                        "generated_at": datetime.now().strftime("%Y-%m-%d"),
                        "deck_rendering": "minimalist-swiss",
                        "deck_palette": "mono-ink",
                        "items": []
                    }
                    for img in referenced_images:
                        manifest_data["items"].append({
                            "filename": img["filename"],
                            "purpose": f"Visual asset for slide {img['svg_stem']}",
                            "type": "illustration",
                            "page_role": "content_accent",
                            "text_policy": "none",
                            "aspect_ratio": "16:9",
                            "image_size": "1K",
                            "prompt": f"Minimalist clean visual asset representing {img['svg_stem'].replace('_', ' ')} in flat vector style, royal blue accent, transparent or clean white background, josef muller-brockmann style.",
                            "alt_text": f"Minimalist illustration for {img['svg_stem']}",
                            "status": "Pending"
                        })
                    try:
                        images_dir.mkdir(parents=True, exist_ok=True)
                        with open(manifest_path, "w", encoding="utf-8") as f:
                            json.dump(manifest_data, f, ensure_ascii=False, indent=2)
                        yield "data: [SYSTEM] ✅ 已自動為您建立配圖清單 {} (含 {} 個專案)！\n\n".format(manifest_path.name, len(referenced_images))
                    except Exception as e:
                        yield "data: [EXCEPTION] 無法建立配圖清單: {}\n\n".format(str(e))
                        return
                else:
                    yield "data: [SYSTEM] 🔍 偵測到本簡報中沒有配置任何影象元素，已自動跳過 AI 配圖步驟！\n\n"
                    yield "data: [SUCCESS] Step 'image_gen' completed successfully!\n\n"
                    return
            
            # Check if we have IMAGE_BACKEND in env or .env
            has_image_backend = False
            env_file = root_dir / ".env"
            if env_file.exists():
                try:
                    with open(env_file, 'r', encoding='utf-8') as f:
                        for line in f:
                            if line.strip().startswith("IMAGE_BACKEND="):
                                val = line.split("=", 1)[1].strip()
                                if val and not val.startswith("#"):
                                    has_image_backend = True
                except Exception:
                    pass
            has_image_backend = bool(os.environ.get("IMAGE_BACKEND")) or has_image_backend
            
            if not has_image_backend:
                yield "data: [環境提示] ⚠️ 偵測到系統未配置 IMAGE_BACKEND 繪圖金鑰（如 GEMINI_API_KEY 或 OPENAI_API_KEY）。\n\n"
                yield "data: [環境提示] 👉 為保持一鍵流水線的完整性，系統將配圖專案自動轉為「手動處理 (Needs-Manual)」狀態，您可以手動放圖。\n\n"
                yield "data: [環境提示] 💡 您可以在右上角的「設定」頁面中配置您的 API 金鑰以啟用自動繪圖功能。\n\n"
                
                try:
                    with open(manifest_path, 'r', encoding='utf-8') as f:
                        manifest_data = json.load(f)
                    
                    updated = False
                    for item in manifest_data.get("items", []):
                        if item.get("status") in {"Pending", "Failed"}:
                            item["status"] = "Needs-Manual"
                            updated = True
                            
                    if updated:
                        with open(manifest_path, 'w', encoding='utf-8') as f:
                            json.dump(manifest_data, f, ensure_ascii=False, indent=2)
                        yield "data: [SYSTEM] 已將配圖專案全部轉為「手動處理 (Needs-Manual)」狀態。\n\n"
                except Exception as e:
                    yield "data: [WARN] 無法更新配圖清單狀態: {}\n\n".format(str(e))
                
                yield "data: [SUCCESS] Step 'image_gen' completed successfully!\n\n"
                return

        yield "data: Command: {}\n\n".format(" ".join(cmd_args))
        
        try:
            process = subprocess.Popen(
                cmd_args,
                cwd=str(root_dir),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding='utf-8',
                errors='replace',
                bufsize=1,
                env=env
            )
            
            for line in iter(process.stdout.readline, ""):
                yield "data: {}\n\n".format(line.rstrip())
                
            process.stdout.close()
            return_code = process.wait()
            
            if return_code == 0:
                yield "data: [SUCCESS] Step '{}' completed successfully!\n\n".format(step)
            else:
                yield "data: [ERROR] Step '{}' failed with code {}.\n\n".format(step, return_code)
                
        except Exception as e:
            yield "data: [EXCEPTION] Failed to launch subprocess: {}\n\n".format(str(e))
        finally:
            # Give a brief moment for the socket to flush all data cleanly to the client before closing
            time.sleep(0.5)
            
    return Response(generate_events(), mimetype='text/event-stream', headers={
        'Cache-Control': 'no-cache',
        'X-Accel-Buffering': 'no',
        'Connection': 'keep-alive'
    })

# Settings API
@app.route('/api/settings', methods=['GET'])
def api_get_settings():
    # Read env keys
    settings = {}
    
    # Read from .env first, fallback to .env.example
    env_to_read = ENV_FILE if ENV_FILE.exists() else ENV_EXAMPLE
    if not env_to_read.exists():
        return jsonify({})
        
    with open(env_to_read, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, val = line.split('=', 1)
                key = key.strip()
                val = val.strip()
                settings[key] = val
                
    # Mask API keys for security in UI representation
    masked_settings = {}
    for key, val in settings.items():
        masked_settings[key] = {
            'value': mask_api_key(key, val),
            'raw': val,
            'is_secret': "KEY" in key or "TOKEN" in key or "SECRET" in key
        }
        
    return jsonify(masked_settings)

@app.route('/api/settings', methods=['POST'])
def api_save_settings():
    data = request.json or {}
    
    # Read existing env file to maintain comments and formatting, or start from scratch
    existing_lines = []
    if ENV_FILE.exists():
        with open(ENV_FILE, 'r', encoding='utf-8') as f:
            existing_lines = f.readlines()
    elif ENV_EXAMPLE.exists():
        with open(ENV_EXAMPLE, 'r', encoding='utf-8') as f:
            existing_lines = f.readlines()
            
    new_lines = []
    processed_keys = set()
    
    # Replace keys in existing lines
    for line in existing_lines:
        line_strip = line.strip()
        if line_strip and not line_strip.startswith('#') and '=' in line_strip:
            key, _ = line_strip.split('=', 1)
            key = key.strip()
            if key in data:
                new_lines.append(f"{key}={data[key]}\n")
                processed_keys.add(key)
                continue
        new_lines.append(line)
        
    # Append any brand new keys
    for key, val in data.items():
        if key not in processed_keys:
            new_lines.append(f"{key}={val}\n")
            
    # Write back to .env
    try:
        with open(ENV_FILE, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': f'Failed to write to .env: {str(e)}'}), 500

@app.route('/api/skillsbuilder/status', methods=['GET'])
def api_skillsbuilder_status():
    skills_builder_dir = Path("C:\\Users\\USER\\Downloads\\SkillsBuilder")
    exists = skills_builder_dir.exists()
    integrated = False
    
    if exists:
        dest_skill_dir = skills_builder_dir / "skills" / "dev" / "ppt-master"
        integrated = dest_skill_dir.exists()
        
    return jsonify({
        'skills_builder_exists': exists,
        'integrated': integrated,
        'path': str(skills_builder_dir) if exists else None
    })

def start_server(port=7070):
    app.run(host="127.0.0.1", port=port, debug=False)

if __name__ == '__main__':
    start_server()
