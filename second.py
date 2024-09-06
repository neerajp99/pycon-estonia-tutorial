import py5
import random
import numpy as np
import sounddevice as sd
from threading import Thread
import time

# Global variables
frequencies = [random.randint(200, 1000) for _ in range(8)]  # Generate 8 random frequencies
audio_thread = None
particles = []
current_freq = 0

def setup():
    global audio_thread
    py5.size(800, 600)
    py5.background(0)
    audio_thread = Thread(target=audio_loop)
    audio_thread.start()
    py5.color_mode(py5.HSB, 360, 100, 100)

def draw():
    global particles, current_freq
    py5.background(0, 25)  # Slight fade effect for motion blur

    # Update and draw particles
    for particle in particles[:]:
        particle.update()
        particle.display()
        if particle.is_dead():
            particles.remove(particle)

    # Create new particles based on audio
    if current_freq > 0:
        hue = py5.remap(current_freq, 200, 1000, 0, 360)
        for _ in range(5):
            particles.append(Particle(py5.random(py5.width), py5.height, hue))

    # Draw frequency bars
    for i, freq in enumerate(frequencies):
        x = py5.width * i / len(frequencies)
        h = py5.remap(freq, 200, 1000, 0, py5.height)
        py5.no_stroke()
        py5.fill(py5.remap(freq, 200, 1000, 0, 360), 80, 80, 100)
        py5.rect(x, py5.height - h, py5.width/len(frequencies), h)

def mouse_pressed():
    trigger_sound()

def audio_loop():
    while True:
        time.sleep(0.1)

def trigger_sound():
    global current_freq
    current_freq = random.choice(frequencies)
    sd.play(generate_sine_wave(current_freq, 0.5), samplerate=44100)

def generate_sine_wave(freq, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    return np.sin(2 * np.pi * freq * t)

class Particle:
    def __init__(self, x, y, hue):
        self.x = x
        self.y = y
        self.hue = hue
        self.size = random.randint(5, 20)
        self.speed = random.uniform(1, 5)
        self.life = 255

    def update(self):
        self.y -= self.speed
        self.life -= 2

    def display(self):
        py5.no_stroke()
        py5.fill(self.hue, 80, 80, self.life)
        py5.ellipse(self.x, self.y, self.size, self.size)

    def is_dead(self):
        return self.life <= 0

py5.run_sketch()