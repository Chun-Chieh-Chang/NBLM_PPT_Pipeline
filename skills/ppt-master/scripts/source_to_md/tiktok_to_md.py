#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tiktok_to_md.py - TikTok Video to Markdown Transcription

Downloads TikTok video (or uses provided file) and transcribes audio to Markdown
using yt-dlp + faster-whisper. Also extracts captions/subtitles if available.

Usage:
    python tiktok_to_md.py <tiktok_url> [-o output.md]
    python tiktok_to_md.py video.mp4 --local
    python tiktok_to_md.py https://www.tiktok.com/@user/video/123 --language zh

Dependencies:
    pip install yt-dlp faster-whisper
    System: ffmpeg (required for audio extraction)

Installation — yt-dlp + FFmpeg + Whisper:
    pip install yt-dlp faster-whisper

    Windows:
        choco install ffmpeg   # Chocolatey
        # Or download from https://ffmpeg.org/download.html

    macOS:
        brew install ffmpeg

    Ubuntu/Debian:
        sudo apt install ffmpeg
"""

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
from pathlib import Path

try:
    from faster_whisper import WhisperModel
except ImportError:
    print("[ERROR] faster-whisper not installed.", file=sys.stderr)
    print("Run: pip install faster-whisper", file=sys.stderr)
    sys.exit(1)


SUPPORTED_VIDEO_EXTENSIONS = {
    ".mp4", ".mkv", ".mov", ".avi", ".webm", ".flv", ".wmv", ".m4v",
}

MODEL_SIZES = ["tiny", "base", "small", "medium", "large"]
DEFAULT_MODEL = "base"  # Good balance of speed/accuracy


def _download_tiktok(url: str, output_dir: Path) -> tuple[Path, dict]:
    """Download TikTok video using yt-dlp.

    Returns:
        (video_path, info_dict)
    """
    try:
        import yt_dlp
    except ImportError:
        print("[ERROR] yt-dlp not installed.", file=sys.stderr)
        print("Run: pip install yt-dlp", file=sys.stderr)
        sys.exit(1)

    ydl_opts = {
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "format": "bestaudio[ext=m4a]/bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality": "192",
        }],
        "quiet": False,
        "no_warnings": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        # Find the downloaded audio file
        for ext in [".wav", ".m4a", ".mp3"]:
            for f in output_dir.glob(f"*{ext}"):
                return f, info

    raise RuntimeError("yt-dlp download completed but no audio file found.")


def _extract_captions_tiktok(url: str, output_dir: Path) -> list[dict] | None:
    """Try to extract TikTok captions/subtitles via yt-dlp."""
    try:
        import yt_dlp
    except ImportError:
        return None

    ydl_opts = {
        "skip_download": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["zh-Hant", "zh-Hans", "zh", "en", "ja", "ko"],
        "subtitlesformat": "best",
        "quiet": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if info and "subtitles" in info:
                # Get the first available subtitle
                for lang, subs in info["subtitles"].items():
                    if subs:
                        sub_url = subs[-1]["url"]
                        # Download subtitle file
                        import urllib.request
                        sub_path = output_dir / f"captions_{lang}.vtt"
                        urllib.request.urlretrieve(sub_url, str(sub_path))
                        return _parse_vtt(str(sub_path), lang)
    except Exception:
        pass
    return None


def _parse_vtt(vtt_path: str, language: str) -> list[dict]:
    """Parse VTT subtitle file to segments."""
    segments = []
    try:
        with open(vtt_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line or line == "WEBVTT":
                i += 1
                continue

            # Try to find timestamp
            ts_match = re.search(r'(\d+:\d{2}:\d{2}\.\d+)\s*-->\s*(\d+:\d{2}:\d{2}\.\d+)', line)
            if ts_match:
                start_str = ts_match.group(1)
                end_str = ts_match.group(2)
                start = _vtt_time_to_seconds(start_str)
                end = _vtt_time_to_seconds(end_str)
                i += 1
                text_lines = []
                while i < len(lines) and lines[i].strip():
                    text_lines.append(lines[i].strip())
                    i += 1
                text = " ".join(text_lines)
                if text:
                    segments.append({
                        "start": round(start, 2),
                        "end": round(end, 2),
                        "text": text,
                    })
            else:
                i += 1
    except Exception:
        pass
    return segments


def _vtt_time_to_seconds(time_str: str) -> float:
    """Convert VTT timestamp to seconds."""
    parts = time_str.split(":")
    if len(parts) == 3:
        h, m, s = parts
        return int(h) * 3600 + int(m) * 60 + float(s)
    elif len(parts) == 2:
        m, s = parts
        return int(m) * 60 + float(s)
    return float(parts[0])


def _extract_audio_ffmpeg(media_path: Path) -> Path:
    """Extract audio from video file using ffmpeg."""
    temp_dir = media_path.parent / ".temp_media_extract"
    temp_dir.mkdir(exist_ok=True)
    temp_wav = temp_dir / f"{media_path.stem}_audio.wav"

    cmd = [
        "ffmpeg", "-y", "-i", str(media_path),
        "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1",
        str(temp_wav)
    ]

    try:
        subprocess.run(cmd, capture_output=True, check=True, timeout=300)
        return temp_wav
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"ffmpeg failed: {e.stderr.decode('utf-8', errors='replace')[:200]}")
    except FileNotFoundError:
        raise RuntimeError(
            "ffmpeg not found. Install it:\n"
            "  Windows: choco install ffmpeg\n"
            "  macOS: brew install ffmpeg\n"
            "  Linux: sudo apt install ffmpeg"
        )


def transcribe_video(video_path: Path, model_size: str, language: str | None,
                     device: str = "cpu") -> tuple[list[dict], dict]:
    """Transcribe video/audio file to text segments using Whisper.

    Returns:
        (segments_list, metadata_dict)
    """
    print(f"[INFO] Loading Whisper model '{model_size}'...", file=sys.stderr)
    model = WhisperModel(model_size, device=device, compute_type="int8")

    # Handle video files
    ext = video_path.suffix.lower()
    if ext in SUPPORTED_VIDEO_EXTENSIONS:
        print(f"[INFO] Extracting audio from video...", file=sys.stderr)
        audio_path = _extract_audio_ffmpeg(video_path)
    else:
        audio_path = video_path

    print(f"[INFO] Transcribing ({language or 'auto'})...", file=sys.stderr)
    segments, info = model.transcribe(
        str(audio_path),
        language=language,
        beam_size=5,
        vad_filter=True,
    )

    segments_list = []
    for seg in segments:
        segments_list.append({
            "start": round(seg.start, 2),
            "end": round(seg.end, 2),
            "text": seg.text.strip(),
        })

    metadata = {
        "detected_language": info.language,
        "language_probability": round(info.language_probability, 4),
        "duration_seconds": round(info.duration, 2) if hasattr(info, 'duration') else 0,
        "model_used": model_size,
        "device": device,
        "total_segments": len(segments_list),
    }

    return segments_list, metadata


def segments_to_markdown(segments: list[dict], captions: list[dict] | None,
                         metadata: dict, source: str) -> str:
    """Convert transcription segments to Markdown format."""
    lines = [
        "# TikTok Transcript",
        "",
        f"**Source**: {source}",
        f"**Language**: {metadata.get('detected_language', 'N/A')}",
        f"**Duration**: {metadata.get('duration_seconds', 0)}s",
        f"**Segments**: {metadata.get('total_segments', 0)}",
        f"**Model**: {metadata.get('model_used', 'N/A')}",
        f"**Generated**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "---",
        "",
    ]

    if captions:
        lines.extend([
            "# Captions / Subtitles (from video)",
            "",
        ])
        for seg in captions:
            start = datetime.timedelta(seconds=seg["start"])
            end = datetime.timedelta(seconds=seg["end"])
            start_str = f"{start.total_seconds():.1f}s"
            end_str = f"{end.total_seconds():.1f}s"
            lines.append(f"[{start_str}] {seg['text']}")
            lines.append("")

    lines.extend([
        "---",
        "",
        "# Whisper Transcription",
        "",
    ])

    for seg in segments:
        start = datetime.timedelta(seconds=seg["start"])
        end = datetime.timedelta(seconds=seg["end"])
        start_str = f"{start.total_seconds():.1f}s"
        end_str = f"{end.total_seconds():.1f}s"
        lines.append(f"[{start_str}] {seg['text']}")
        lines.append("")

    # Add full text summary
    all_text = " ".join(seg["text"] for seg in segments)
    lines.extend([
        "---",
        "",
        "# Full Text",
        "",
        all_text,
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe TikTok videos to Markdown.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s https://www.tiktok.com/@user/video/123
  %(prog)s https://vm.tiktok.com/ABC123 --language zh --model small
  %(prog)s video.mp4 --local --language en
  %(prog)s <url> -o transcript.md
        """,
    )
    parser.add_argument(
        "input", help="TikTok URL or local video file"
    )
    parser.add_argument(
        "-o", "--output", default=None,
        help="Output Markdown file (default: stdout)",
    )
    parser.add_argument(
        "--language", default="auto",
        help="Language code (en, zh, ja, etc.) or 'auto'. Default: auto",
    )
    parser.add_argument(
        "--model", default=DEFAULT_MODEL,
        choices=MODEL_SIZES,
        help=f"Whisper model size. Default: {DEFAULT_MODEL}",
    )
    parser.add_argument(
        "--device", default="cpu",
        choices=["cpu", "cuda"],
        help="Compute device. Use 'cuda' if you have NVIDIA GPU. Default: cpu",
    )
    parser.add_argument(
        "--local", action="store_true", default=False,
        help="Input is a local video file, not a URL",
    )
    parser.add_argument(
        "--json-out", action="store_true", default=False,
        help="Also output raw JSON alongside Markdown",
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    language = None if args.language.lower() == "auto" else args.language.lower()

    segments = []
    captions = None
    metadata = {}
    source_url = args.input

    try:
        if args.local:
            if not input_path.exists():
                print(f"[ERROR] Local file not found: {input_path}", file=sys.stderr)
                sys.exit(1)
            ext = input_path.suffix.lower()
            if ext not in SUPPORTED_VIDEO_EXTENSIONS:
                print(f"[ERROR] Unsupported local file format: {ext}", file=sys.stderr)
                sys.exit(1)
            print(f"[INFO] Processing local file: {input_path}", file=sys.stderr)
            segments, metadata = transcribe_video(input_path, args.model, language, args.device)
        else:
            # TikTok URL
            output_dir = input_path.parent if input_path.is_dir() else Path.cwd()
            print(f"[INFO] Downloading TikTok video...", file=sys.stderr)
            video_path, yt_info = _download_tiktok(args.input, output_dir)
            print(f"[INFO] Transcribing audio...", file=sys.stderr)
            segments, metadata = transcribe_video(video_path, args.model, language, args.device)

            # Try to extract captions
            print(f"[INFO] Trying to extract captions...", file=sys.stderr)
            captions = _extract_captions_tiktok(args.input, output_dir)

            metadata["source"] = args.input
            metadata["yt_title"] = yt_info.get("title", "") if yt_info else ""
            metadata["yt_author"] = yt_info.get("uploader", "") if yt_info else ""

    except Exception as e:
        print(f"[ERROR] Failed: {e}", file=sys.stderr)
        sys.exit(1)

    md_content = segments_to_markdown(segments, captions, metadata, source_url)

    if args.json_out:
        json_data = {
            "segments": segments,
            "captions": captions or [],
            "metadata": metadata,
        }
        out_base = Path(args.output).stem if args.output else "transcript"
        json_path = Path(args.output).with_suffix(".json") if args.output else Path(out_base + ".json")
        json_path.write_text(
            json.dumps(json_data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"[OK] JSON saved to {json_path.resolve()}", file=sys.stderr)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md_content, encoding="utf-8")
        print(f"[OK] Written to {out_path.resolve()}")
    else:
        print(md_content)


if __name__ == "__main__":
    import re
    main()
