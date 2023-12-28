import dawdreamer as daw
from scipy.io import wavfile
from playsound import playsound
import os

SAMPLE_RATE = 44100
BUFFER_SIZE = 128 # Parameters will undergo automation at this buffer/block size.
PLUGIN_PATH = "/Library/Audio/Plug-Ins/Components/VD-DEEP.component"  # extensions: .dll, .vst3, .vst, .component
MIDI_PATH = "/Users/thomas/Music/Groove-Monkee-Progressive/Other-MIDI-Mappings/Progressive-Ujam/4-4-Grooves/180-4-4-01-D.mid"

engine = daw.RenderEngine(SAMPLE_RATE, BUFFER_SIZE)
plugin = engine.make_plugin_processor("midi-preview", PLUGIN_PATH)

plugin.load_midi(MIDI_PATH, clear_previous=True, beats=False, all_events=True)

graph = [
	(plugin, [])
]

engine.load_graph(graph)
engine.render(5) 

audio = engine.get_audio()

TMP_FILE = "tmp.wav"
wavfile.write(TMP_FILE, SAMPLE_RATE, audio.transpose())
playsound(TMP_FILE, block=True)

# Remove the file synth_demo.wav
os.remove(TMP_FILE)

