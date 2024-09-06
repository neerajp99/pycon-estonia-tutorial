import py5
import random

# Constants
WIDTH = 800
HEIGHT = 1000
GRID_SPACING = 42
CHARACTER_SIZE = 30
NUM_CURVES_PER_CHAR = 3

def setup():
    py5.size(WIDTH, HEIGHT)
    create_parchment_background()
    draw_characters()
    add_texture()
    py5.no_loop()  # Run the draw function only once

def create_parchment_background():
    py5.background(220, 204, 177)  # Light beige color for parchment
    py5.no_stroke()
    # Add random small ellipses to create a textured look
    for _ in range(10000):
        x = py5.random(WIDTH)
        y = py5.random(HEIGHT)
        # Vary the color slightly for each ellipse
        py5.fill(py5.random(200, 230), py5.random(184, 214), py5.random(157, 197), py5.random(20, 60))
        py5.ellipse(x, y, py5.random(1, 3), py5.random(1, 3))

def draw_characters():
    # Draw characters in a grid pattern
    for i in range(GRID_SPACING, WIDTH - GRID_SPACING, GRID_SPACING):
        for j in range(GRID_SPACING, HEIGHT - GRID_SPACING, GRID_SPACING):
            draw_character(i, j)

def draw_character(x, y):
    py5.push_matrix()  # Save the current transformation state
    py5.translate(x, y)  # Move to the character's position
    py5.rotate(py5.random(-0.1, 0.1))  # Slight random rotation for each character
    
    # 'Ink' color with slight variations
    py5.stroke(py5.random(20, 40), py5.random(10, 30), 0, py5.random(200, 255))
    py5.stroke_weight(py5.random(1, 2))
    py5.no_fill()
    
    # Draw multiple curves to form each character
    for _ in range(NUM_CURVES_PER_CHAR):
        py5.begin_shape()
        for _ in range(4):  # 4 control points for each curve
            py5.curve_vertex(py5.random(-CHARACTER_SIZE/2, CHARACTER_SIZE/2),
                             py5.random(-CHARACTER_SIZE/2, CHARACTER_SIZE/2))
        py5.end_shape()
    
    py5.pop_matrix()  # Restore the previous transformation state

def add_texture():
    py5.blend_mode(py5.MULTIPLY)  # Set blend mode to multiply for darker texture
    # Add random points to create a grainy texture
    for _ in range(20000):
        x = py5.random(WIDTH)
        y = py5.random(HEIGHT)
        py5.stroke(0, py5.random(5, 20))  # Black color with random opacity
        py5.point(x, y)
    py5.blend_mode(py5.BLEND)  # Reset blend mode

def key_pressed():
    if py5.key == 's':
        py5.save_frame("manuscript_characters.png")  # Save the sketch as an image
    elif py5.key == 'r':
        py5.random_seed(int(py5.random(10000)))  # Set a new random seed
        py5.redraw()  # Redraw the sketch with the new seed

py5.run_sketch()