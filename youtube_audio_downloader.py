#!/usr/bin/env python3
"""Download audio from YouTube videos using yt-dlp."""

import argparse
import sys
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    sys.stderr.write(
        "yt-dlp is required. Install it with: pip install yt-dlp\n"
        "FFmpeg must also be available on PATH for audio extraction.\n"
    )
    sys.exit(1)


def build_ydl_options(
    output_dir: Path,
    audio_format: str,
    audio_quality: str,
    no_check_certificates: bool = False,
) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    return {
        "format": "bestaudio/best",
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "noplaylist": False,
        "quiet": False,
        "no_warnings": False,
        "nocheckcertificate": no_check_certificates,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": audio_format,
                "preferredquality": audio_quality,
            }
        ],
    }


def download(
    urls: list[str],
    output_dir: Path,
    audio_format: str,
    audio_quality: str,
    no_check_certificates: bool = False,
) -> int:
    options = build_ydl_options(output_dir, audio_format, audio_quality, no_check_certificates)
    with yt_dlp.YoutubeDL(options) as ydl:
        return ydl.download(urls)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download audio from one or more YouTube URLs.",
    )
    parser.add_argument("urls", nargs="+", help="YouTube video or playlist URLs")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=Path("downloads"),
        help="Directory to save audio files (default: ./downloads)",
    )
    parser.add_argument(
        "-f",
        "--format",
        dest="audio_format",
        default="mp3",
        choices=["mp3", "m4a", "opus", "vorbis", "wav", "flac", "aac"],
        help="Audio format to convert to (default: mp3)",
    )
    parser.add_argument(
        "-q",
        "--quality",
        dest="audio_quality",
        default="192",
        help="Audio quality in kbps or 0-9 VBR (default: 192)",
    )
    parser.add_argument(
        "--no-check-certificates",
        action="store_true",
        help="Skip TLS certificate verification (use only behind trusted MITM proxies)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return download(
        args.urls,
        args.output_dir,
        args.audio_format,
        args.audio_quality,
        args.no_check_certificates,
    )


if __name__ == "__main__":
    sys.exit(main())
