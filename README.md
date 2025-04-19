# Multi-Track Audio Sampler

A simple Multi-Track Audio Sampler to splice up bars consistently across synchronised audio stems.

It takes up multiple synchronised `.wav` stem tracks (bass, drums, vocals, etc.) and slices them based on your selected musical segments (bars / milliseconds).

Exports the resulting samples into new files.

## REQUIREMENTS

### **ONLY WORKS UP TO PYTHON 3.11.x!**
Python 3.13+ is **not supported** due to removed dependencies.

## Dependencies:
- `pydub`
- `ffmpeg`

## INSTALLATION

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/multitrack-audio-slicer.git
cd multitrack-audio-slicer
```

### 2. Install Python 3.11

```bash
brew install python@3.11
```

run
```bash
brew link python@3.11 --force --overwrite
```
if encountering filepath issues

### 3. Create and activate a virtual environment
```bash
/opt/homebrew/bin/python3.11 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install pydub
brew install ffmpeg
```

## USAGE

1. Place `.wav`files in same folder as the script.
2. Update the `files` dictionary with your filenames.
3. Define segments/regions to splice up using either of the two options:
    - Bar ranges: (start_bar, end_bar)
    - Milliseconds: (start_ms, end_ms)
    - Set USE_BARS to True/False respectively.
4. Run script 
```bash 
python AudioSampler.py
```

## NOTES

- You can adjust `SHIFT_MS` - Optional manual offset (in milliseconds) to compensate for silence or pre-roll at the start of the audio file.
- If you re-run script with changes made, originally generated files get **overwritten** (fix by changing filenames!)
