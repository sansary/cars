# YouTube Audio Downloader

A small command-line tool that downloads audio from YouTube videos or playlists and converts it to a chosen format using `yt-dlp` and FFmpeg.

## Requirements

- Python 3.9+
- [FFmpeg](https://ffmpeg.org/) on your `PATH`
- Python packages: `pip install -r requirements.txt`

## Usage

```bash
python youtube_audio_downloader.py <URL> [<URL> ...] [options]
```

### Options

| Flag | Description | Default |
| --- | --- | --- |
| `-o, --output-dir` | Directory to save audio files | `./downloads` |
| `-f, --format` | Audio format: `mp3`, `m4a`, `opus`, `vorbis`, `wav`, `flac`, `aac` | `mp3` |
| `-q, --quality` | Bitrate in kbps (e.g. `192`, `320`) or VBR `0-9` | `192` |
| `--no-check-certificates` | Skip TLS verification (only for trusted MITM proxies) | off |

### Examples

Download a single video as 192 kbps MP3 to `./downloads`:

```bash
python youtube_audio_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Download a playlist as 320 kbps MP3 into a custom directory:

```bash
python youtube_audio_downloader.py \
  "https://www.youtube.com/playlist?list=PLxxxxxxxxxxxx" \
  -o ~/Music/yt -q 320
```

Download as FLAC:

```bash
python youtube_audio_downloader.py "<URL>" -f flac
```

## Notes

Make sure you have the right to download any content you process with this tool.
