import random
from music21 import stream, note, midi

# Function to generate a random note
def generate_random_note():
    pitch = random.choice(['C', 'D', 'E', 'F', 'G', 'A', 'B'])
    octave = random.choice([4, 5])
    duration = random.choice([0.25, 0.5, 1.0])  # quarter, half, whole notes
    return note.Note(pitch + str(octave), quarterLength=duration)

# Function to generate a melody
def generate_melody(length=16):
    melody = stream.Stream()
    for _ in range(length):
        melody.append(generate_random_note())
    return melody

# Generate a melody and show it
melody = generate_melody()
melody.show('text')

# Save the melody as a MIDI file
mf = midi.translate.music21ObjectToMidiFile(melody)
mf.open('random_melody.mid', 'wb')
mf.write()
mf.close()
