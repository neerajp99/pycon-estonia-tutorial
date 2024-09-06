import py5
import numpy as np
import sounddevice as sd
from scipy import signal
import random
import colorsys

# Audio parameters
SAMPLE_RATE = 44100
DURATION = 0.1
BPM = 128

# Visual parameters
NUM_WAVES = 5
MAX_RADIUS = 400

# Global variables
beat_intensity = 0
hue_offset = 0
beat_counter = 0
current_palette = []
waves = []

def setup():
    global current_palette, waves
    py5.size(800, 800, py5.P3D)
    py5.color_mode(py5.HSB, 360, 100, 100)
    py5.background(0)
    py5.frame_rate(60)
    
    current_palette = generate_palette()
    waves = [Wave(i) for i in range(NUM_WAVES)]

def draw():
    global beat_intensity, hue_offset, beat_counter
    
    py5.background(0, 25)
    py5.translate(py5.width / 2, py5.height / 2)
    
    # Generate beats
    frames_per_beat = py5.get_frame_rate() * 60 / BPM
    if py5.frame_count % int(frames_per_beat) == 0:
        beat_counter = (beat_counter + 1) % 16
        trigger_beat(beat_counter)
        if beat_counter % 8 == 0:
            change_palette()
    
    # Update beat intensity
    beat_intensity *= 0.95
    
    # Draw waves
    for wave in waves:
        wave.update()
        wave.display()

def trigger_beat(beat):
    global beat_intensity
    beat_intensity = 1
    
    if beat % 4 == 0:
        sd.play(generate_kick(), SAMPLE_RATE)
        waves[0].pulse(0.5)
    if beat % 8 == 4:
        sd.play(generate_snare(), SAMPLE_RATE)
        waves[1].pulse(0.3)
    if beat % 2 == 1:
        sd.play(generate_hihat(), SAMPLE_RATE)
        waves[2].pulse(0.2)

def generate_kick():
    t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), False)
    frequency = 50 * np.exp(-t * 50)
    return np.sin(2 * np.pi * frequency * t) * np.exp(-t * 20)

def generate_snare():
    t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), False)
    return np.random.normal(0, 1, t.shape) * np.exp(-t * 40)

def generate_hihat():
    t = np.linspace(0, DURATION/2, int(SAMPLE_RATE * DURATION/2), False)
    return np.random.normal(0, 1, t.shape) * np.exp(-t * 200)

def generate_palette():
    base_hue = random.random()
    return [
        colorsys.hsv_to_rgb((base_hue + i/5) % 1, 0.7, 0.9)
        for i in range(5)
    ]

def change_palette():
    global current_palette
    current_palette = generate_palette()

def map_range(value, start1, stop1, start2, stop2):
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))

class Wave:
    def __init__(self, index):
        self.index = index
        self.radius = 0
        self.target_radius = 0
        self.thickness = random.uniform(2, 5)
        self.speed = random.uniform(0.5, 2)
        self.color = random.choice(current_palette)
        self.alpha = 255

    def update(self):
        self.radius += (self.target_radius - self.radius) * 0.1
        self.alpha = int(map_range(self.radius, 0, MAX_RADIUS, 255, 0))
        if self.radius > MAX_RADIUS:
            self.reset()

    def display(self):
        py5.stroke(*[int(c * 255) for c in self.color], self.alpha)
        py5.stroke_weight(self.thickness + beat_intensity * 2)
        py5.no_fill()
        py5.ellipse(0, 0, self.radius * 2, self.radius * 2)

    def pulse(self, intensity):
        self.target_radius += MAX_RADIUS * intensity

    def reset(self):
        self.radius = 0
        self.target_radius = 0
        self.color = random.choice(current_palette)

py5.run_sketch()