---
name: audio-transcriber
description: >
  Transcribe audio and video files to text using Whisper (local, free, no API key needed). Use this
  skill whenever the user asks to transcribe, convert audio to text, get a transcript, subtitle, or
  caption any audio or video file. Supports mp3, wav, m4a, mp4, flac, ogg, webm, and more. Trigger
  for "transcribe", "transcript", "audio to text", "what does this audio say", "convert this recording",
  "speech to text", "subtitles", "captions", "listen to this file", or any request involving extracting
  text from audio or video files.
---

# Audio Transcriber

Transcribe any audio or video file to text using Whisper — runs locally, free, no API keys.

## Requirements (Already Installed)

- `faster-whisper` (Python package) — the transcription engine
- `ffmpeg` (at `~/bin/ffmpeg`) — audio processing
- `transcribe.py` (at this skill's location) — the transcription script

## How to Transcribe

Run the transcription script using Bash:

```bash
python3 ~/.claude/skills/audio-transcriber/transcribe.py "<path_to_audio_file>"
```

### Options

| Flag | Values | Default | What it does |
|------|--------|---------|-------------|
| `--model` | `tiny`, `base`, `small`, `medium`, `large-v3` | `base` | Larger = more accurate but slower |
| `--output` | `text`, `srt`, `vtt`, `segments`, `all` | `text` | Output format |
| `--outfile` | file path | (prints to screen) | Save to file instead of printing |

### Model Selection Guide

| Model | Speed | Accuracy | Best for |
|-------|-------|----------|----------|
| `tiny` | Fastest (~10x realtime) | Good for clear speech | Quick previews, clear recordings |
| `base` | Fast (~5x realtime) | Good | Default — works well for most files |
| `small` | Moderate (~2x realtime) | Very good | Accented speech, background noise |
| `medium` | Slow (~1x realtime) | Excellent | Important transcripts, multiple speakers |
| `large-v3` | Slowest | Best available | Critical accuracy, foreign languages |

**First run of each model size downloads the model (~50MB-3GB). Subsequent runs are instant.**

### Examples

**Basic transcription (print to screen):**
```bash
python3 ~/.claude/skills/audio-transcriber/transcribe.py "/path/to/recording.mp3"
```

**Save to text file:**
```bash
python3 ~/.claude/skills/audio-transcriber/transcribe.py "/path/to/recording.mp3" --outfile "/path/to/transcript.txt"
```

**Higher accuracy with medium model:**
```bash
python3 ~/.claude/skills/audio-transcriber/transcribe.py "/path/to/recording.mp3" --model medium
```

**Generate subtitles (SRT format):**
```bash
python3 ~/.claude/skills/audio-transcriber/transcribe.py "/path/to/video.mp4" --output srt --outfile "/path/to/subtitles.srt"
```

**All formats at once (text + SRT + VTT + segments):**
```bash
python3 ~/.claude/skills/audio-transcriber/transcribe.py "/path/to/audio.m4a" --output all --outfile "/path/to/output.txt"
```

## Supported File Types

Any format ffmpeg can read: `.mp3`, `.wav`, `.m4a`, `.mp4`, `.flac`, `.ogg`, `.webm`, `.aac`, `.wma`, `.mov`, `.avi`, `.mkv`, and many more.

## Workflow

1. **User provides an audio/video file path**
2. **Choose the right model** — `base` for most files, `medium` or `large-v3` for noisy/accented/critical content
3. **Run the transcription script** using Bash tool
4. **Read the output** — either from the Bash output or from the saved file
5. **Post-process if needed** — clean up, summarize, extract key points, etc.

## Tips

- For **long files** (60+ minutes), use `--model base` first for a quick draft, then re-run specific sections with `medium` if needed
- The **first run** of a new model size will download it (~30 seconds to a few minutes). After that, it's cached.
- Output **SRT/VTT** formats if the user wants timestamps with each segment
- The `segments` output shows timestamped chunks — useful for finding specific moments
- If transcription quality is poor, try upgrading the model size one step
- The script auto-detects language — works with English, Spanish, French, and 90+ other languages
