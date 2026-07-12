#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
media_to_md.py - Video / Audio to Markdown Transcription

Uses faster-whisper for high-quality, offline speech-to-text transcription.
Supports MP4, MKV, MOV, AVI, WebM, MP3, WAV, M4A, AAC, OGG, FLAC, etc.

Usage:
    python media_to_md.py <video_or_audio_file> [-o output.md] [--language zh]
    python media_to_md.py meeting.mp4 --model medium
    python media_to_md.py podcast.mp3 --language en --output transcript.md

Dependencies:
    pip install faster-whisper
    System: ffmpeg (required for audio extraction from video)

Installation — FFmpeg + faster-whisper:
    pip install faster-whisper

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
import sys
from pathlib import Path

try:
    from faster_whisper import WhisperModel
except ImportError:
    print("[ERROR] faster-whisper not installed.", file=sys.stderr)
    print("Run: pip install faster-whisper", file=sys.stderr)
    sys.exit(1)


SUPPORTED_EXTENSIONS = {
    # Video formats
    ".mp4", ".mkv", ".mov", ".avi", ".webm", ".flv", ".wmv", ".m4v",
    # Audio formats
    ".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac", ".wma", ".opus",
}

MODEL_SIZES = ["tiny", "base", "small", "medium", "large"]
DEFAULT_MODEL = "base"  # Good balance of speed/accuracy


def _detect_language(lang_str: str | None) -> str | None:
    """Return language code or None for auto-detect."""
    if lang_str and lang_str.lower() != "auto":
        return lang_str.lower()
    return None


def _extract_audio_ffmpeg(media_path: Path) -> Path:
    """Extract audio from video file using ffmpeg, return temp wav path."""
    import subprocess

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


def transcribe(media_path: Path, model_size: str, language: str | None,
               device: str = "cpu") -> tuple[list[dict], dict]:
    """Transcribe audio/video file to text segments.

    Returns:
        (segments_list, metadata_dict)
    """
    # Load model
    print(f"[INFO] Loading Whisper model '{model_size}'...", file=sys.stderr)
    model = WhisperModel(model_size, device=device, compute_type="int8")

    # Handle video files — extract audio first
    ext = media_path.suffix.lower()
    if ext in {".mp4", ".mkv", ".mov", ".avi", ".webm", ".flv", ".wmv", ".m4v"}:
        print(f"[INFO] Extracting audio from video...", file=sys.stderr)
        audio_path = _extract_audio_ffmpeg(media_path)
    else:
        audio_path = media_path

    # Transcribe
    print(f"[INFO] Transcribing ({language or 'auto'})...", file=sys.stderr)
    segments, info = model.transcribe(
        str(audio_path),
        language=language,
        beam_size=5,
        vad_filter=True,  # Voice activity detection
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


def segments_to_markdown(segments: list[dict], metadata: dict) -> str:
    """Convert transcription segments to Markdown format."""
    lines = [
        "# Transcript",
        "",
        f"**Source**: {metadata.get('source', 'N/A')}",
        f"**Language**: {metadata['detected_language']}",
        f"**Duration**: {metadata['duration_seconds']}s",
        f"**Segments**: {metadata['total_segments']}",
        f"**Model**: {metadata['model_used']}",
        f"**Generated**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "---",
        "",
    ]

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
        description="Transcribe video/audio files to Markdown using Whisper.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s video.mp4
  %(prog)s podcast.mp3 --language en --model small
  %(prog)s meeting.mkv --language zh -o transcript.md
  %(prog)s audio.wav --model medium --device cuda
        """,
    )
    parser.add_argument(
        "files", nargs="+", help="Video or audio file(s) to transcribe"
    )
    parser.add_argument(
        "-o", "--output", default=None,
        help="Output Markdown file (default: stdout)",
    )
    parser.add_argument(
        "--language", default="auto",
        help="Language code (en, zh, ja, etc.) or 'auto' for detection. Default: auto",
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
        "--json-out", action="store_true", default=False,
        help="Also output raw JSON alongside Markdown",
    )

    args = parser.parse_args()

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
            segments, metadata = transcribe(path, args.model, language, args.device)
        except Exception as e:
            print(f"[ERROR] Failed to process {path}: {e}", file=sys.stderr)
            continue

        metadata["source"] = str(path.resolve())
        md_content = segments_to_markdown(segments, metadata)
        outputs.append(md_content)

        if args.json_out:
            json_path = path.with_suffix(path.suffix + ".transcript.json")
            json_path.write_text(
                json.dumps({"segments": segments, "metadata": metadata}, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            print(f"[OK] JSON transcript saved to {json_path.resolve()}", file=sys.stderr)

    if not outputs:
        print("[ERROR] No files were successfully processed.", file=sys.stderr)
        sys.exit(1)

    final_output = "\n\n".join(outputs)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(final_output, encoding="utf-8")
        print(f"[OK] Written to {out_path.resolve()}")
    else:
        print(final_output)


if __name__ == "__main__":
    main()
