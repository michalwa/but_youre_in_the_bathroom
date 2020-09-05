from typing import Optional
from pydub import AudioSegment
from pydub.playback import play
from pysndfx import AudioEffectsChain
import sys
import numpy as np
import array


def go_to_bathroom(audio: AudioSegment, background: Optional[AudioSegment] = None) -> AudioSegment:

    # Convert pydub audio to numpy array
    samples = np.array(audio.get_array_of_samples()).astype(np.int16)

    fx = (
        AudioEffectsChain()
        .reverb(reverberance=100)
        .lowpass(600, q=.4)
        .lowpass(600, q=.4)
        .lowpass(600, q=.4)
    )

    new_samples = fx(samples)

    # Convert back to pydub audio
    audio_data = array.array(audio.array_type, new_samples)
    new_audio = audio._spawn(audio_data)

    if background is not None:
        new_audio = new_audio.overlay(background, loop=True)

    return new_audio


print('Going to the party...')
path = sys.argv[1]
filename, ext = path.rsplit('.', 1)
song = AudioSegment.from_file(path, format=ext)

print('Going to the bathroom...')
song_but_youre_in_the_bathroom_at_a_party = go_to_bathroom(song)

# print('Exporting...')
# new_filename = filename + ' but youre in the bathroom'
# song_but_youre_in_the_bathroom_at_a_party.export(new_filename + '.mp3')

print('Playing!')
play(song_but_youre_in_the_bathroom_at_a_party)
