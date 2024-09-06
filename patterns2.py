
import py5
import random
import noise

WIDTH = 800
HEIGHT = 1000
NUM_LAYERS = 20
NOISE_SCALE = 0.01

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
    py5.begin_shape()
    for y in range(y_start, y_end):
        # Randomize the start position more drastically
        x_start = random.randint(0, WIDTH // 2)  # More variation in the start position
        
        # Randomize density more per row
        density = random.uniform(1, 5)  # Adjusted range to ensure noticeable variation
        step_size = max(1, int(density))
        
        for x in range(x_start, WIDTH, step_size):
            n = noise.pnoise2(x * NOISE_SCALE, y * NOISE_SCALE, octaves=4, persistence=0.5, lacunarity=2.0)
            offset_x = py5.remap(n, -1, 1, -30, 30)
            offset_y = py5.remap(n, -1, 1, -15, 15)
            
            if y + offset_y < y_start or y + offset_y >= y_end:
                continue
            
            r, g, b = base_color
            color_variation = random.randint(-20, 20)
            py5.fill(r + color_variation, g + color_variation, b + color_variation, random.randint(100, 255))
            
            py5.vertex(x + offset_x, y + offset_y)
            py5.rect(x + offset_x, y + offset_y, random.uniform(0.5, 3.5), random.uniform(0.5, 3.5))  # More granular shapes
        
        if random.random() < 0.05:  # Add a random curve every so often
            py5.curve_vertex(x + offset_x, y + offset_y)
    py5.end_shape()

def key_pressed():
    if py5.key == 'r':
        py5.background(255)
        draw_layers()
    elif py5.key == 's':
        py5.save_frame("meridian_inspired_art.png")

py5.run_sketch()