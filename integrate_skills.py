# -*- coding: utf-8 -*-
"""
PPT Master & SkillsBuilder Bidirectional Integration Script
Usage: python integrate_skills.py
"""

import os
import sys
import subprocess
import shutil

def safe_print(text):
    try:
        print(text)
    except UnicodeEncodeError:
        try:
            print(text.encode('ascii', 'ignore').decode('ascii'))
        except Exception:
            pass

def main():
    safe_print("=" * 60)
    safe_print("[INFO] Starting PPT Master and SkillsBuilder Integration...")
    safe_print("=" * 60)
    
    ppt_master_dir = os.getcwd()
    skills_builder_dir = "C:\\Users\\USER\\Downloads\\SkillsBuilder"
    
    if not os.path.exists(skills_builder_dir):
        safe_print(f"[ERROR] SkillsBuilder directory not found at: {skills_builder_dir}")
        safe_print("Please edit the script to point to the correct directory if needed.")
        return
        
    dev_skills_dir = os.path.join(skills_builder_dir, "skills", "dev")
    os.makedirs(dev_skills_dir, exist_ok=True)
    
    ppt_master_skill_src = os.path.join(ppt_master_dir, "skills", "ppt-master")
    ppt_master_skill_dest = os.path.join(dev_skills_dir, "ppt-master")
    
    safe_print(f"[LINK] Syncing skill source:")
    safe_print(f"   From: {ppt_master_skill_src}")
    safe_print(f"   To:   {ppt_master_skill_dest}")
    
    # 1. Clean up old link/folder if exists
    if os.path.exists(ppt_master_skill_dest) or os.path.islink(ppt_master_skill_dest):
        safe_print("[CLEAN] Previous destination detected, cleaning up...")
        try:
            if os.path.islink(ppt_master_skill_dest) or os.path.isfile(ppt_master_skill_dest):
                os.remove(ppt_master_skill_dest)
            elif os.path.isdir(ppt_master_skill_dest):
                shutil.rmtree(ppt_master_skill_dest)
        except Exception as e:
            safe_print(f"[ERROR] Error cleaning up old target: {e}")
            return
            
    # 2. Establish sync (try Symlink first, fallback to deep Copy)
    linked_successfully = False
    try:
        os.symlink(ppt_master_skill_src, ppt_master_skill_dest, target_is_directory=True)
        safe_print("[SUCCESS] Directory symbolic link created successfully via Python os.symlink!")
        linked_successfully = True
    except Exception as e:
        safe_print("[WARNING] Native os.symlink failed. Trying cmd mklink...")
        cmd = f'mklink /d "{ppt_master_skill_dest}" "{ppt_master_skill_src}"'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            safe_print("[SUCCESS] Symbolic link created successfully via mklink!")
            linked_successfully = True
        else:
            safe_print("[INFO] Symlink failed (requires Administrator). Falling back to direct folder copy...")
            
    if not linked_successfully:
        try:
            # Recursively copy ppt-master skill folder to SkillsBuilder/skills/dev/ppt-master
            # Ignore dynamic projects, logs or other runtimes to keep it clean
            def ignore_patterns(path, names):
                ignored = []
                for name in names:
                    if name in ['.git', 'projects', 'exports', '__pycache__', 'node_modules', '.venv', 'env']:
                        ignored.append(name)
                return ignored
                
            shutil.copytree(ppt_master_skill_src, ppt_master_skill_dest, ignore=ignore_patterns)
            safe_print("[SUCCESS] ppt-master skill folder copied successfully into SkillsBuilder!")
        except Exception as ex:
            safe_print(f"[ERROR] Copy failed: {ex}")
            return

    # 3. Invoke SkillsBuilder's INSTALL.ps1 to register all skills
    safe_print("\n[SYNC] Triggering SkillsBuilder INSTALL.ps1 to sync global skills pool...")
    try:
        install_script = os.path.join(skills_builder_dir, "INSTALL.ps1")
        cmd_ps = f'powershell -ExecutionPolicy Bypass -File "{install_script}"'
        result = subprocess.run(cmd_ps, cwd=skills_builder_dir, shell=True, capture_output=True, text=True)
        
        safe_print("-" * 50)
        for line in result.stdout.splitlines():
            safe_print(line)
        safe_print("-" * 50)
        
        if result.returncode == 0:
            safe_print("[SUCCESS] Integration SUCCESS! PPT Master is now linked inside SkillsBuilder dev list.")
            safe_print("You can call ppt-master in any workspace across the system now!")
        else:
            safe_print(f"[ERROR] INSTALL.ps1 exited with error code {result.returncode}")
            safe_print(result.stderr)
    except Exception as ex:
        safe_print(f"[ERROR] Failed to launch INSTALL.ps1: {ex}")

    safe_print("=" * 60)

if __name__ == "__main__":
    main()
