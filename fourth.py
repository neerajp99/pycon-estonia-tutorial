import py5
import numpy as np
import sounddevice as sd
from scipy import signal
import random

# Audio parameters
SAMPLE_RATE = 44100
DURATION = 0.1  # Duration of each sound
BPM = 130  # Beats per minute
TARGET_FRAME_RATE = 60  # Set a target frame rate

# Visual parameters
NUM_RINGS = 6
SEGMENTS_PER_RING = 32
MAX_RADIUS = 350

# Global variables
rotation = 0
beat_intensity = 0
hue_offset = 0
beat_counter = 0

def setup():
    py5.size(800, 800)
    py5.color_mode(py5.HSB, 360, 100, 100)
    py5.background(0)
    py5.frame_rate(TARGET_FRAME_RATE)  # Set the target frame rate

def draw():
    global rotation, beat_intensity, hue_offset, beat_counter
    
    py5.background(0, 25)  # Fade effect
    py5.translate(py5.width / 2, py5.height / 2)
    
    # Generate beats
    frames_per_beat = TARGET_FRAME_RATE * 60 / BPM
    if py5.frame_count % int(frames_per_beat) == 0:
        beat_counter = (beat_counter + 1) % 16
        trigger_beat(beat_counter)
        hue_offset = (hue_offset + 10) % 360  # Shift hue
    
    # Update rotation and beat intensity
    rotation += 0.002
    beat_intensity *= 0.9  # Decay
    
    # Draw evolving mandala
    draw_mandala()
    
    # Draw additional shapes
    draw_additional_shapes()

def trigger_beat(beat):
    global beat_intensity
    beat_intensity = 1
    
    # Kick drum on every beat
    if beat % 4 == 0:
        audio_data = generate_kick()
        sd.play(audio_data, SAMPLE_RATE)
    
    # Snare on every other beat
    if beat % 8 == 4:
        audio_data = generate_snare()
        sd.play(audio_data, SAMPLE_RATE)
    
    # Hi-hat on off-beats
    if beat % 2 == 1:
        audio_data = generate_hihat()
        sd.play(audio_data, SAMPLE_RATE)
    
    # Synth note every 4 beats
    if beat % 4 == 0:
        frequency = random.choice([220, 330, 440, 550])
        audio_data = generate_synth(frequency)
        sd.play(audio_data, SAMPLE_RATE)

def generate_kick():
    t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), False)
    frequency = 50 * np.exp(-t * 50)
    kick = np.sin(2 * np.pi * frequency * t)
    envelope = np.exp(-t * 20)
    return kick * envelope

def generate_snare():
    t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), False)
    noise = np.random.normal(0, 1, t.shape)
    envelope = np.exp(-t * 40)
    return noise * envelope

def generate_hihat():
    t = np.linspace(0, DURATION/2, int(SAMPLE_RATE * DURATION/2), False)
    noise = np.random.normal(0, 1, t.shape)
    envelope = np.exp(-t * 200)
    return noise * envelope

def generate_synth(frequency):
    t = np.linspace(0, DURATION*2, int(SAMPLE_RATE * DURATION*2), False)
    tone = 0.3 * signal.square(2 * np.pi * frequency * t)
    envelope = np.exp(-t * 5)
    return tone * envelope

def draw_mandala():
    for ring in range(NUM_RINGS):
        radius = MAX_RADIUS * (ring + 1) / NUM_RINGS
        segment_angle = 360 / SEGMENTS_PER_RING
        for segment in range(SEGMENTS_PER_RING):
            angle = segment * segment_angle + rotation * (ring + 1) * 20
            
            x1 = py5.cos(py5.radians(angle)) * radius
            y1 = py5.sin(py5.radians(angle)) * radius
            x2 = py5.cos(py5.radians(angle + segment_angle)) * radius
            y2 = py5.sin(py5.radians(angle + segment_angle)) * radius
            
            hue = (angle + hue_offset) % 360
            saturation = 80 + beat_intensity * 20
            brightness = 50 + beat_intensity * 50
            
            py5.stroke(hue, saturation, brightness)
            py5.stroke_weight(2 + beat_intensity * 3)
            
            py5.line(x1, y1, x2, y2)
            
            if random.random() < 0.2:
                py5.no_fill()
                py5.arc(0, 0, radius * 2, radius * 2, 
                        py5.radians(angle), py5.radians(angle + segment_angle))

    # Draw central circle
    py5.fill(hue_offset, 80, 100)
    py5.no_stroke()
    central_radius = MAX_RADIUS / NUM_RINGS * beat_intensity
    py5.circle(0, 0, central_radius * 2)

def draw_additional_shapes():
    # Draw rotating triangles
    py5.push_matrix()
    py5.rotate(rotation * 2)
    for i in range(3):
        angle = i * 120 + py5.frame_count
        x = py5.cos(py5.radians(angle)) * MAX_RADIUS * 0.7
        y = py5.sin(py5.radians(angle)) * MAX_RADIUS * 0.7
        py5.fill((hue_offset + 120) % 360, 80, 80, 150)
        py5.triangle(x, y, x+20, y+20, x-20, y+20)
    py5.pop_matrix()
    
    # Draw pulsing squares
    py5.push_matrix()
    py5.rotate(-rotation)
    for i in range(4):
        angle = i * 90 + py5.frame_count * 2
        x = py5.cos(py5.radians(angle)) * MAX_RADIUS * 0.5
        y = py5.sin(py5.radians(angle)) * MAX_RADIUS * 0.5
        size = 30 + beat_intensity * 10
        py5.fill((hue_offset + 240) % 360, 80, 80, 150)
        py5.rect(x-size/2, y-size/2, size, size)
    py5.pop_matrix()

py5.run_sketch()