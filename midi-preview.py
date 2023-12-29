import argparse
import os
import dawdreamer as daw
from tqdm import tqdm
from scipy.io import wavfile

SAMPLE_RATE = 44100
BUFFER_SIZE = 128

argParser = argparse.ArgumentParser()
argParser.add_argument("-m", "--midi", help="Path to your midi files")
argParser.add_argument("-p", "--plugin", help="Path to VST/VST3/AU plugin")
argParser.add_argument("-s", "--seconds", help="Rendered audio file length (default: 8)", default=8, required=False, type=int)
argParser.add_argument("-o", "--open", help="Should the plugin window be opened to make adjustments?", action="store_true")

args = argParser.parse_args()

engine = daw.RenderEngine(SAMPLE_RATE, BUFFER_SIZE)
plugin = engine.make_plugin_processor("midi-preview", args.plugin)

print('inputs:', plugin.get_num_input_channels())
print('outputs:', plugin.get_num_output_channels())

if args.open:
	plugin.open_editor()

engine.load_graph([(plugin, [])])

midi_files = []

print("Searching for midi files in " + args.midi)
for root, dirs, files in os.walk(args.midi):
	for file in files:
		if file.endswith(".mid"):
			file_path = os.path.join(root, file)
			midi_files.append(file_path)

print("Found " + str(len(midi_files)) + " midi files")
print("Start rendering...")

bar = tqdm(midi_files)
for midi_file in bar:
	plugin.load_midi(midi_file, clear_previous=True, beats=False, all_events=True)

	engine.render(args.seconds) 
	audio = engine.get_audio()
	mono_audio = audio.transpose()[:, :1]

	filename = os.path.splitext(midi_file)[0] + ".wav"
	bar.set_postfix_str(filename)

	wavfile.write(filename, SAMPLE_RATE, mono_audio)
	