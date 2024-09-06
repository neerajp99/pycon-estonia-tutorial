import py5
import random
import numpy as np
import sounddevice as sd
from threading import Thread
import time

# Global variables
frequencies = [random.randint(200, 1000) for _ in range(8)]
audio_thread = None

def setup():
    global audio_thread
    py5.size(400, 400)
    py5.background(220)
    audio_thread = Thread(target=audio_loop)
    audio_thread.start()

def draw():
    py5.background(220)
    for i in range(8):
        x = py5.width * i / 8
        h = py5.height * frequencies[i] / 1000
        py5.fill(0)
        py5.rect(x, py5.height - h, py5.width/8, h)

def mouse_pressed():
    trigger_sound()

def audio_loop():
    while True:
        time.sleep(0.1)

def trigger_sound():
    freq = random.choice(frequencies)
    sd.play(generate_sine_wave(freq, 0.5), samplerate=44100)

def generate_sine_wave(freq, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    return np.sin(2 * np.pi * freq * t)

py5.run_sketch()