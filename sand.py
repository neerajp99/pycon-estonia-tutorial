import py5
import random
import noise

WIDTH = 800
HEIGHT = 1000
NUM_LAYERS = 20
NOISE_SCALE = 0.005

colors = [
    (255, 166, 43),   # Orange
    (6, 69, 173),     # Blue
    (248, 243, 212),  # Cream
    (61, 153, 112),   # Green
    (218, 65, 103),   # Pink
    (183, 183, 164),  # Light Gray
    (42, 46, 75)      # Dark Blue
]

def setup():
    py5.size(WIDTH, HEIGHT)
    py5.background(255)
    py5.no_stroke()
    
    draw_layers()
    
    py5.no_loop()

def draw_layers():
    for i in range(NUM_LAYERS):
        layer_color = random.choice(colors)
        y_start = int(py5.remap(i, 0, NUM_LAYERS, 0, HEIGHT))
        y_end = int(py5.remap(i+1, 0, NUM_LAYERS, 0, HEIGHT))
        draw_layer(y_start, y_end, layer_color)

def draw_layer(y_start, y_end, base_color):
    for y in range(y_start, y_end):
        for x in range(WIDTH):
            n = noise.pnoise2(x * NOISE_SCALE, y * NOISE_SCALE, octaves=4, persistence=0.5, lacunarity=2.0)
            offset = py5.remap(n, -1, 1, -30, 30)
            
            if y + offset < y_start or y + offset >= y_end:
                continue
            
            r, g, b = base_color
            color_variation = random.randint(-20, 20)
            py5.fill(r + color_variation, g + color_variation, b + color_variation, random.randint(100, 255))
            
            py5.rect(x, y + offset, 1, 1)

def key_pressed():
    if py5.key == 'r':
        py5.background(255)
        draw_layers()
    elif py5.key == 's':
        py5.save_frame("sand.png")

py5.run_sketch()


