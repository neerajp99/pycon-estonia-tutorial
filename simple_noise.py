import py5

noise_scale = 0.02

def setup():
    py5.size(800, 600)
    py5.stroke_weight(1)

def draw():
    py5.background(0)
    
    for x in range(py5.width):
        noise_val = py5.noise((py5.mouse_x + x) * noise_scale, py5.mouse_y * noise_scale)
        py5.stroke(noise_val * 255)
        py5.line(x, py5.mouse_y + noise_val * 30, x, py5.height)

py5.run_sketch()