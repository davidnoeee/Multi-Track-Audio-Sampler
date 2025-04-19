from pydub import AudioSegment

# MAIN CONFIG

USE_BARS = True
BPM = 120
BAR_LENGTH_MS = 60000 / BPM * 4 # 4 beats per bar
NAMING_SEGMENTS_FIRST = True # If True, exported filenames start with the region name (e.g. chorus_bass.wav). If False, the original filename is used as the prefix (e.g. bass_chorus.wav).

SHIFT_MS = 0 # Optional manual offset (in milliseconds) to compensate for silence or pre-roll at the start of the audio file.

# AUDIO FILES
# Upload your files to the SAME folder as this script
# If not in same folder, use full filepaths instead

files = {
        "bass": "bass.wav",
        "drums": "drums.wav",
        "vocals": "vocals.wav",
}

# AUDIO SEGMENTS
# Define segments/regions as either (start_bar, end_bar) or (start_ms, end_ms) depending on if USE_BARS = True

segments = {
    "intro": (0, 4),
    "verse_1": (4, 12),
    "pre_chorus": (12, 16),
    "chorus": (16, 24),
    "verse_2": (24, 32),
    "chorus": (32, 40),
    "bridge": (40, 44),
    "breakdown": (44, 48),
    "drop": (48, 56),
    "outro": (56, 64)
}

# PROCESSING

for name, path in files.items():
    audio = AudioSegment.from_wav(path)
    for segment, (start, end) in segments.items():
        if USE_BARS:
            start_ms = int(start * BAR_LENGTH_MS) + SHIFT_MS
            end_ms = int(end * BAR_LENGTH_MS) + SHIFT_MS
        else:
            start_ms = start + SHIFT_MS
            end_ms = end + SHIFT_MS
        
        segment = audio[start_ms:end_ms]
        if NAMING_SEGMENTS_FIRST:
            segment.export(f"{segment}_{name}.wav", format="wav")
        else:
            segment.export(f"{name}_{segment}.wav", format="wav")

print("Audio Segments exported successfully! :)")