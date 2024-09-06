import numpy as np
import sounddevice as sd

def generate_sine_wave(freq, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    return np.sin(2 * np.pi * freq * t)

def play_tone(frequency, duration):
    tone = generate_sine_wave(frequency, duration)
    sd.play(tone, samplerate=44100)
    sd.wait()

def play_melody():
    melody = [
        (440, 0.5),  # A4
        (493.88, 0.5),  # B4
        (523.25, 0.5),  # C5
        (587.33, 0.5),  # D5
        (659.25, 0.5),  # E5
        (523.25, 0.5),  # C5
        (493.88, 0.5),  # B4
        (440, 1.0)  # A4 (held longer)
    ]
    
    for freq, duration in melody:
        play_tone(freq, duration)

# Example usage
if __name__ == "__main__":
    play_melody()
