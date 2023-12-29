# MIDI 🎹 Preview

## Usage

Preview MIDI files through a VST/VST3/AU plugin.
It generates WAV file previews of rendered MIDI through an instrument plugin of your choice

```bash
usage: midi-preview.py [-h] [-m MIDI] [-p PLUGIN] [-s SECONDS] [-o]

optional arguments:
  -h, --help            show this help message and exit
  -m MIDI, --midi MIDI  Path to your midi files
  -p PLUGIN, --plugin PLUGIN
                        Path to VST/VST3/AU plugin
  -s SECONDS, --seconds SECONDS
                        Rendered audio file length (default: 8)
  -o, --open            Should the plugin window be opened to make adjustments?
```
