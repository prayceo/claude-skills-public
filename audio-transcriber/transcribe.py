#!/usr/bin/env python3
"""
Audio Transcriber — powered by faster-whisper (local, free, no API key)
Usage: python3 transcribe.py <audio_file> [--model medium] [--output text|srt|vtt|all] [--outfile path]
"""

import argparse
import sys
import os
import time

def format_timestamp(seconds, srt=False):
    """Convert seconds to timestamp format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    if srt:
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{ms:03d}"
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{ms:03d}"

def transcribe(audio_path, model_size="base", output_format="text", outfile=None):
    """Transcribe an audio file using faster-whisper."""

    if not os.path.exists(audio_path):
        print(f"Error: File not found: {audio_path}")
        sys.exit(1)

    # Set ffmpeg path if installed to ~/bin
    ffmpeg_path = os.path.expanduser("~/bin/ffmpeg")
    if os.path.exists(ffmpeg_path):
        os.environ["PATH"] = os.path.dirname(ffmpeg_path) + ":" + os.environ.get("PATH", "")

    from faster_whisper import WhisperModel

    file_size_mb = os.path.getsize(audio_path) / (1024 * 1024)
    print(f"File: {os.path.basename(audio_path)} ({file_size_mb:.1f} MB)")
    print(f"Model: {model_size}")
    print(f"Loading model...")

    start_time = time.time()

    # Use CPU on Mac (MPS not supported by CTranslate2)
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    print(f"Transcribing... (this may take a few minutes for long files)")

    segments, info = model.transcribe(audio_path, beam_size=5)

    print(f"Detected language: {info.language} (probability: {info.language_probability:.2f})")
    print(f"Duration: {info.duration:.1f} seconds ({info.duration/60:.1f} minutes)")
    print()

    # Collect all segments
    all_segments = []
    full_text = []

    for segment in segments:
        all_segments.append(segment)
        full_text.append(segment.text.strip())

    elapsed = time.time() - start_time

    # Generate output based on format
    if output_format == "text" or output_format == "all":
        text_output = " ".join(full_text)
        if outfile:
            text_path = outfile if output_format == "text" else outfile.rsplit(".", 1)[0] + ".txt"
            with open(text_path, "w") as f:
                f.write(text_output)
            print(f"Text saved to: {text_path}")
        else:
            print("=" * 60)
            print("TRANSCRIPT")
            print("=" * 60)
            print(text_output)
            print("=" * 60)

    if output_format == "srt" or output_format == "all":
        srt_lines = []
        for i, seg in enumerate(all_segments, 1):
            srt_lines.append(str(i))
            srt_lines.append(f"{format_timestamp(seg.start, srt=True)} --> {format_timestamp(seg.end, srt=True)}")
            srt_lines.append(seg.text.strip())
            srt_lines.append("")
        srt_output = "\n".join(srt_lines)
        if outfile:
            srt_path = outfile if output_format == "srt" else outfile.rsplit(".", 1)[0] + ".srt"
            with open(srt_path, "w") as f:
                f.write(srt_output)
            print(f"SRT saved to: {srt_path}")
        else:
            print(srt_output)

    if output_format == "vtt" or output_format == "all":
        vtt_lines = ["WEBVTT", ""]
        for seg in all_segments:
            vtt_lines.append(f"{format_timestamp(seg.start)} --> {format_timestamp(seg.end)}")
            vtt_lines.append(seg.text.strip())
            vtt_lines.append("")
        vtt_output = "\n".join(vtt_lines)
        if outfile:
            vtt_path = outfile if output_format == "vtt" else outfile.rsplit(".", 1)[0] + ".vtt"
            with open(vtt_path, "w") as f:
                f.write(vtt_output)
            print(f"VTT saved to: {vtt_path}")

    if output_format == "segments" or output_format == "all":
        print()
        print("TIMESTAMPED SEGMENTS")
        print("-" * 60)
        for seg in all_segments:
            print(f"[{format_timestamp(seg.start)} --> {format_timestamp(seg.end)}] {seg.text.strip()}")

    print(f"\nCompleted in {elapsed:.1f}s (speed: {info.duration/elapsed:.1f}x realtime)")

    return " ".join(full_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe audio files using Whisper")
    parser.add_argument("audio_file", help="Path to audio file (mp3, wav, m4a, mp4, etc.)")
    parser.add_argument("--model", default="base", choices=["tiny", "base", "small", "medium", "large-v3"],
                       help="Model size: tiny (fastest), base (default), small, medium, large-v3 (best quality)")
    parser.add_argument("--output", default="text", choices=["text", "srt", "vtt", "segments", "all"],
                       help="Output format: text (default), srt, vtt, segments, or all")
    parser.add_argument("--outfile", help="Save output to file instead of printing")

    args = parser.parse_args()
    transcribe(args.audio_file, args.model, args.output, args.outfile)
