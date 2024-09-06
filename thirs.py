import py5
import numpy as np
import sounddevice as sd
from scipy import signal
import random

# Audio parameters
SAMPLE_RATE = 44100  # Samples per second
DURATION = 0.1  # Duration of each beat sound in seconds

# Visual parameters
NUM_RINGS = 5  # Number of concentric rings in the mandala
SEGMENTS_PER_RING = 16  # Number of segments in each ring
MAX_RADIUS = 350  # Maximum radius of the outermost ring

# Global variables
rotation = 0  # Current rotation angle of the mandala
beat_intensity = 0  # Intensity of the current beat (affects visual elements)
hue_offset = 0  # Offset for color cycling

def setup():
    py5.size(800, 800)  # Set canvas size
    py5.color_mode(py5.HSB, 360, 100, 100)  # Use HSB color mode
    py5.background(0)  # Set initial background to black

def draw():
    global rotation, beat_intensity, hue_offset
    py5.background(0, 25)  # Fade effect for smooth animation
    py5.translate(py5.width / 2, py5.height / 2)  # Move origin to center

    # Generate beat every half second (30 frames at 60 fps)
    if py5.frame_count % 30 == 0:
        trigger_beat()
        hue_offset = (hue_offset + 20) % 360  # Shift hue for color cycling

    # Update rotation and decay beat intensity
    rotation += 0.005
    beat_intensity *= 0.95

    # Draw the mandala
    draw_mandala()

def trigger_beat():
    global beat_intensity
    beat_intensity = 1  # Set beat intensity to maximum
    frequency = random.choice([220, 330, 440, 550])  # Choose a random frequency
    audio_data = generate_beat(frequency)
    sd.play(audio_data, SAMPLE_RATE)  # Play the generated audio

def generate_beat(frequency):
    t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), False)
    tone = 0.5 * signal.square(2 * np.pi * frequency * t)  # Generate square wave
    envelope = np.exp(-t * 20)  # Create a fast decay envelope
    return tone * envelope  # Apply envelope to tone

def draw_mandala():
    for ring in range(NUM_RINGS):
        radius = MAX_RADIUS * (ring + 1) / NUM_RINGS
        segment_angle = 360 / SEGMENTS_PER_RING

        for segment in range(SEGMENTS_PER_RING):
            angle = segment * segment_angle + rotation * (ring + 1) * 20

            # Calculate segment start and end points
            x1 = py5.cos(py5.radians(angle)) * radius
            y1 = py5.sin(py5.radians(angle)) * radius
            x2 = py5.cos(py5.radians(angle + segment_angle)) * radius
            y2 = py5.sin(py5.radians(angle + segment_angle)) * radius

            # Determine segment color based on position and beat
            hue = (angle + hue_offset) % 360
            saturation = 80 + beat_intensity * 20
            brightness = 50 + beat_intensity * 50

            py5.stroke(hue, saturation, brightness)
            py5.stroke_weight(2 + beat_intensity * 3)

            # Draw segment
            py5.line(x1, y1, x2, y2)

            # Occasionally draw arcs for variation
            if random.random() < 0.3:
                py5.no_fill()
                py5.arc(0, 0, radius * 2, radius * 2,
                        py5.radians(angle), py5.radians(angle + segment_angle))

    # Draw central circle
    py5.fill(hue_offset, 80, 100)
    py5.no_stroke()
    central_radius = MAX_RADIUS / NUM_RINGS * beat_intensity
    py5.circle(0, 0, central_radius * 2)

py5.run_sketch()