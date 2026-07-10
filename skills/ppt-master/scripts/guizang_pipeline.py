#!/usr/bin/env python3
"""
NBLM PPT Pipeline - Guizang HTML Generator
Automates the guizang-ppt-skill HTML generation process via Gemini API.
"""

import sys
import argparse
import os
import json
from pathlib import Path

# Try to import from config
try:
    from config import load_prefixed_env_file, resolve_env_path
except ImportError:
    # Fallback if run standalone
    def load_prefixed_env_file(*args, **kwargs):
        pass

def parse_args():
    parser = argparse.ArgumentParser(description="Generate Guizang HTML Presentation")
    parser.add_argument("project_dir", help="Project directory path")
    parser.add_argument("--style", default="magazine", choices=["magazine", "swiss"], help="Guizang style to use")
    return parser.parse_args()

def main():
    args = parse_args()
    project_path = Path(args.project_dir).resolve()
    
    # Setup paths
    sources_dir = project_path / "sources"
    exports_dir = project_path / "exports"
    exports_dir.mkdir(parents=True, exist_ok=True)
    
    # Load env
    try:
        from dotenv import load_dotenv
        env_path = Path(__file__).resolve().parent.parent.parent.parent / ".env"
        load_dotenv(env_path)
    except Exception:
        pass
        
    agnes_api_key = os.environ.get("AGNES_API_KEY")
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not agnes_api_key and not gemini_api_key:
        print("[ERROR] Neither AGNES_API_KEY nor GEMINI_API_KEY is set. Cannot generate HTML.")
        sys.exit(1)

    print(f"[START] Starting Guizang HTML Generation (Style: {args.style})")
    
    # Read all source markdowns
    source_texts = []
    if sources_dir.exists():
        for file_path in sources_dir.glob("*"):
            if file_path.suffix.lower() in ['.md', '.txt']:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        source_texts.append(f.read())
                except Exception as e:
                    print(f"Failed to read {file_path.name}: {e}")
                    
    combined_source = "\n\n---\n\n".join(source_texts)
    if not combined_source.strip():
        print("[ERROR] No valid source text found in sources directory.")
        sys.exit(1)

    # Load template
    skill_dir = Path(__file__).resolve().parent.parent.parent / "guizang-ppt-skill"
    template_file = "template-swiss.html" if args.style == "swiss" else "template.html"
    template_path = skill_dir / "assets" / template_file
    
    if not template_path.exists():
        print(f"[ERROR] Template {template_file} not found at {template_path}")
        sys.exit(1)
        
    with open(template_path, 'r', encoding='utf-8') as f:
        template_html = f.read()

    # Call AI
    print("[INFO] Calling AI API to compile HTML presentation...")
    try:
        prompt = f"""
Below is a provided HTML template and some raw source content.
Your task is to populate the HTML template with the source content, creating a beautiful and well-structured presentation.
Keep the exact same styling, scripts, and CSS provided in the template. Just add/modify the <section class="slide"> elements in the <body>.

### Template (HTML)
```html
{template_html}
```

### Source Content
{combined_source}

Generate the final, complete HTML document. DO NOT include any markdown code blocks (e.g. ```html). Just output the raw HTML string starting with <!DOCTYPE html>.
"""
        if agnes_api_key:
            import openai
            print("[INFO] Using Agnes AI (agnes-2.0-flash) for HTML compilation...")
            client = openai.OpenAI(
                api_key=agnes_api_key,
                base_url="https://apihub.agnes-ai.com/v1"
            )
            response = client.chat.completions.create(
                model="agnes-2.0-flash",
                messages=[
                    {"role": "system", "content": "You are an expert presentation designer."},
                    {"role": "user", "content": prompt}
                ]
            )
            final_html = response.choices[0].message.content.strip()
        else:
            from google import genai
            print("[INFO] Using Gemini (gemini-2.5-flash) for HTML compilation...")
            client = genai.Client(api_key=gemini_api_key)
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"You are an expert presentation designer.\n{prompt}",
            )
            final_html = response.text.strip()
        if final_html.startswith("```html"):
            final_html = final_html[7:]
        if final_html.endswith("```"):
            final_html = final_html[:-3]
            
        final_html = final_html.strip()
        
        output_file = exports_dir / "presentation.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_html)
            
        print(f"[SUCCESS] HTML presentation generated at {output_file.name}")
        
        # Update project_info.json
        info_file = project_path / "project_info.json"
        if info_file.exists():
            with open(info_file, 'r', encoding='utf-8') as f:
                info = json.load(f)
            
            info['has_split'] = True
            info['has_total_md'] = True
            info['svg_count'] = 1
            info['state'] = "Exported"
            
            with open(info_file, 'w', encoding='utf-8') as f:
                json.dump(info, f, ensure_ascii=False, indent=2)
                
    except Exception as e:
        print(f"[ERROR] Gemini API call failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
