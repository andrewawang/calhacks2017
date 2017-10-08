# Magenta code and RNN provided by 
# Ian Simon and Sageev Oore. "Performance RNN: Generating Music with Expressive
# Timing and Dynamics." Magenta Blog, 2017.
# https://magenta.tensorflow.org/performance-rnn
from magenta.music import midi_synth
import IPython
import os
from magenta.models.performance_rnn import performance_sequence_generator
from magenta.protobuf import generator_pb2
from magenta.protobuf import music_pb2
import numpy as np
from scipy.io.wavfile import write
import magenta.music as mm
from magenta.music import midi_io
import time
import threading
from playsound import playsound as ps

# Constants.
DEFAULT_SAMPLE_RATE = 44100
SAMPLE_MULT = 1
DURATION = 5
TEMP = 0.6
BUNDLE_DIR = '/Users/wangan/Documents/calhacks2017/magenta/'
MODEL_NAME = 'multiconditioned_performance_with_dynamics'
BUNDLE_NAME = MODEL_NAME + '.mag'


def play_music(array_of_floats):
    write('temp.wav', 44100, array_of_floats)
    ps.playsound("/Users/wangan/Documents/calhacks2017/temp.wav")

mm.notebook_utils.download_bundle(BUNDLE_NAME, BUNDLE_DIR)
bundle = mm.sequence_generator_bundle.read_bundle_file(os.path.join(BUNDLE_DIR, BUNDLE_NAME))
generator_map = performance_sequence_generator.get_generator_map()
generator = generator_map[MODEL_NAME](checkpoint=None, bundle=bundle)
generator.initialize()
generator_options = generator_pb2.GeneratorOptions()
generator_options.args['temperature'].float_value = TEMP  # Higher is more random; 1.0 is default. 
generate_section = generator_options.generate_sections.add(start_time=0, end_time=DURATION)
sequence = generator.generate(music_pb2.NoteSequence(), generator_options)

# Play and view this masterpiece.
mm.plot_sequence(sequence)
# audio_object = modified_play_sequence(sequence, mm.midi_synth.fluidsynth, sample_rate=DEFAULT_SAMPLE_RATE * SAMPLE_MULT)
# mm.play_sequence(sequence, mm.midi_synth.fluidsynth, sample_rate=DEFAULT_SAMPLE_RATE * SAMPLE_MULT)

sample_rate=DEFAULT_SAMPLE_RATE * SAMPLE_MULT
array_of_floats = mm.midi_synth.fluidsynth(sequence, sample_rate=sample_rate)

# audio_killed = int(sample_rate * 1)
# array_of_floats = array_of_floats[audio_killed:]

# IPython.display.Audio(array_of_floats, rate=sample_rate, autoplay=True)

i = 0
while(True):
    array_of_floats = []
    generator_map2 = performance_sequence_generator.get_generator_map()
    generator2 = generator_map2[MODEL_NAME](checkpoint=None, bundle=bundle)
    generator2.initialize()
    generator_options2 = generator_pb2.GeneratorOptions()
    generator_options2.args['temperature'].float_value = TEMP  # Higher is more random; 1.0 is default. 
    generate_section = generator_options2.generate_sections.add(start_time=(i*DURATION), end_time=(i+1)*DURATION)
    sequenceNew = generator2.generate(sequence, generator_options2)

    # Play and view this masterpiece.
    mm.plot_sequence(sequenceNew)
    # audio_object = modified_play_sequence(sequence, mm.midi_synth.fluidsynth, sample_rate=DEFAULT_SAMPLE_RATE * SAMPLE_MULT)
    # mm.play_sequence(sequence, mm.midi_synth.fluidsynth, sample_rate=DEFAULT_SAMPLE_RATE * SAMPLE_MULT)

    sample_rate= 1*DEFAULT_SAMPLE_RATE * SAMPLE_MULT
    array_of_floats = mm.midi_synth.fluidsynth(sequenceNew, sample_rate=sample_rate)
    sequence = sequenceNew

#     audio_killed = int(sample_rate * 1)
    old_array_size = int(sample_rate * DURATION * i)
    array_of_floats = array_of_floats[old_array_size:]
#     array_of_floats = array_of_floats[audio_killed:]
#     print("NOTE SEQUENCE: ", music_pb2.NoteSequence)
    music_thread = threading.Thread(target=play_music, args=[array_of_floats], name="temp")
    music_thread.run()
#     play_music(array_of_floats)
    del generator_map2
    del generator2
    del generator_options2
    del generate_section
    del sequenceNew
    i += 1
    os.remove("temp.wav")
    print("active thread count: ", threading.activeCount())