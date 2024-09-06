import py5
import numpy as np
import pyaudio
import colorsys

# Audio parameters
CHUNK = 1024  # Number of audio samples per frame
FORMAT = pyaudio.paFloat32  # Audio format (32-bit float)
CHANNELS = 1  # Mono audio
RATE = 44100  # Sample rate (Hz)

# Visual parameters
NUM_BANDS = 64  # Number of frequency bands for visualization
SMOOTHING = 0.2  # Smoothing factor for the visualization

# Global variables
fft_data = None  # Will store the FFT data
smoothed_data = np.zeros(NUM_BANDS)  # Smoothed FFT data

def setup():
    global p, stream
    py5.size(1000, 800)  # Set canvas size
    py5.color_mode(py5.RGB, 255)  # Set color mode to RGB
    py5.background(10, 10, 30)  # Set initial background color

    # Initialize PyAudio
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

def draw():
    global fft_data, smoothed_data
    py5.background(10, 10, 30, 20)  # Slight fade effect for motion blur

    # Read and process audio data, breaks down the audio into different frequency bands.
    data = np.frombuffer(stream.read(CHUNK, exception_on_overflow=False), dtype=np.float32)
    fft_data = np.abs(np.fft.fft(data)[:NUM_BANDS])  # Compute FFT and take magnitude

    # Smooth the FFT data
    smoothed_data = SMOOTHING * fft_data + (1 - SMOOTHING) * smoothed_data

    # Draw visualizations
    draw_circular_equalizer()
    draw_linear_equalizer()
    draw_title()

def draw_circular_equalizer():
    center_x, center_y = py5.width // 2, py5.height // 2 - 100
    max_radius = 200
    bar_width = py5.TWO_PI / NUM_BANDS

    for i in range(NUM_BANDS):
        angle = i * bar_width
        r = py5.remap(smoothed_data[i], 0, np.max(smoothed_data), 50, max_radius)
        
        # Calculate start and end points of each line
        x1 = center_x + np.cos(angle) * 50
        y1 = center_y + np.sin(angle) * 50
        x2 = center_x + np.cos(angle) * r
        y2 = center_y + np.sin(angle) * r

        # Create gradient color (purple to blue range)
        hue = py5.remap(i, 0, NUM_BANDS, 0.7, 1.0)
        rgb = colorsys.hsv_to_rgb(hue, 1, 1)
        color = py5.color(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))

        py5.stroke(color)
        py5.stroke_weight(3)
        py5.line(x1, y1, x2, y2)

def draw_linear_equalizer():
    bar_width = py5.width / NUM_BANDS
    for i in range(NUM_BANDS):
        x = i * bar_width
        y = py5.height
        h = py5.remap(smoothed_data[i], 0, np.max(smoothed_data), 0, 300)

        # Create rainbow gradient
        hue = i / NUM_BANDS
        rgb = colorsys.hsv_to_rgb(hue, 1, 1)
        color = py5.color(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))

        py5.no_stroke()
        py5.fill(color)
        py5.rect(x, y, bar_width, -h)  # Draw bar

        # Draw reflection
        py5.fill(color, 100)  # Semi-transparent for reflection effect
        py5.rect(x, y, bar_width, h * 0.3)

def draw_title():
    py5.fill(255)  # White color for text
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text_size(40)
    py5.text("PYCON ESTONIA", py5.width // 2, py5.height // 2 - 100)
    py5.text_size(20)
    py5.text("creative session", py5.width // 2, py5.height // 2 - 50)

def exit():
    # Clean up audio stream when exiting
    stream.stop_stream()
    stream.close()
    p.terminate()

py5.run_sketch()