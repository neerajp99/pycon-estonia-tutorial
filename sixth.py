import py5
import numpy as np
import pyaudio
import struct

# Audio parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Wave parameters
NUM_WAVES = 5
MAX_AMPLITUDE = 100
DAMPING = 0.05

# Global variables
audio_data = np.zeros(CHUNK)
volume = 0
wave_amplitudes = [0] * NUM_WAVES

def setup():
    global p, stream
    
    py5.size(800, 800)
    py5.background(0)
    
    p = pyaudio.PyAudio()
    try:
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        py5.println("Audio stream opened successfully")
    except Exception as e:
        py5.println(f"Error opening audio stream: {str(e)}")

def draw():
    global audio_data, volume, wave_amplitudes
    
    py5.background(0, 25)  # Slight fade effect
    
    try:
        # Read audio data
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.int16)
        
        # Calculate volume (RMS)
        volume = np.sqrt(np.mean(audio_data**2))
        
        # Update wave amplitudes
        target_amplitude = py5.remap(volume, 0, 5000, 0, MAX_AMPLITUDE)
        for i in range(NUM_WAVES):
            wave_amplitudes[i] += (target_amplitude - wave_amplitudes[i]) * DAMPING
        
        # Draw circular waves
        py5.translate(py5.width / 2, py5.height / 2)
        for i in range(NUM_WAVES):
            draw_circular_wave(i)
        
        # Display debug information
        py5.fill(255)
        py5.text_size(14)
        py5.text(f"Volume: {volume:.2f}", -py5.width/2 + 10, -py5.height/2 + 20)
        
    except Exception as e:
        py5.fill(255, 0, 0)
        py5.text(f"Error during audio processing: {str(e)}", -py5.width/2 + 10, py5.height/2 - 20)

def draw_circular_wave(wave_index):
    radius = 100 + wave_index * 50
    frequency = 6 + wave_index * 2
    amplitude = wave_amplitudes[wave_index]
    
    py5.stroke(py5.remap(wave_index, 0, NUM_WAVES-1, 0, 255), 200, 255)
    py5.stroke_weight(2)
    py5.no_fill()
    
    py5.begin_shape()
    for angle in range(0, 361):
        r = radius + py5.sin(py5.radians(angle * frequency)) * amplitude
        x = r * py5.cos(py5.radians(angle))
        y = r * py5.sin(py5.radians(angle))
        py5.vertex(x, y)
    py5.end_shape(py5.CLOSE)

def exit():
    try:
        stream.stop_stream()
        stream.close()
        p.terminate()
    except Exception as e:
        py5.println(f"Error during cleanup: {str(e)}")

py5.run_sketch()