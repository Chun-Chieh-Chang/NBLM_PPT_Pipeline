#!/usr/bin/env python3
"""
Agnes AI Image Generation Backend

Generates images via Agnes AI API.
Used by image_gen.py as a backend module.

Configuration keys:
  AGNES_API_KEY    (required) API key
  AGNES_BASE_URL   (optional) Default: https://apihub.agnes-ai.com/v1
  AGNES_MODEL      (optional) Default: agnes-image-2.1-flash
"""

import sys

if __name__ == "__main__" and any(arg in {"-h", "--help", "help"} for arg in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0)

import os
from image_backends import backend_openai

def generate(prompt: str,
             aspect_ratio: str = "1:1", image_size: str = "1K",
             output_dir: str = None, filename: str = None,
             model: str = None, max_retries: int = 3) -> str:
    """Entry point for image_gen.py to generate a single image using Agnes AI."""
    api_key = os.environ.get("AGNES_API_KEY")
    if not api_key:
        raise ValueError("AGNES_API_KEY environment variable is missing.")
        
    base_url = os.environ.get("AGNES_BASE_URL", "https://apihub.agnes-ai.com/v1")
    model = os.environ.get("AGNES_MODEL", "agnes-image-2.1-flash")

    # Store old values
    old_key = os.environ.get("OPENAI_API_KEY")
    old_base = os.environ.get("OPENAI_BASE_URL")
    old_model = os.environ.get("OPENAI_MODEL")
    
    # Temporarily override OPENAI env vars so backend_openai works
    os.environ["OPENAI_API_KEY"] = api_key
    os.environ["OPENAI_BASE_URL"] = base_url
    os.environ["OPENAI_MODEL"] = model
    
    try:
        return backend_openai.generate(
            prompt=prompt,
            aspect_ratio=aspect_ratio,
            image_size=image_size,
            output_dir=output_dir,
            filename=filename,
            model=os.environ.get("OPENAI_MODEL"),
            max_retries=max_retries
        )
    finally:
        # Restore old values
        if old_key is not None:
            os.environ["OPENAI_API_KEY"] = old_key
        else:
            if "OPENAI_API_KEY" in os.environ:
                del os.environ["OPENAI_API_KEY"]
                
        if old_base is not None:
            os.environ["OPENAI_BASE_URL"] = old_base
        else:
            if "OPENAI_BASE_URL" in os.environ:
                del os.environ["OPENAI_BASE_URL"]
                
        if old_model is not None:
            os.environ["OPENAI_MODEL"] = old_model
        else:
            if "OPENAI_MODEL" in os.environ:
                del os.environ["OPENAI_MODEL"]
