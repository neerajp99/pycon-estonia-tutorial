import py5

def setup():
    py5.size(800, 600)
    py5.background(0, 30, 30)  # Dark teal background
    py5.stroke(200, 255, 255, 50)  # Light cyan color with transparency
    py5.stroke_weight(1)
    
    noise_scale = 0.01
    num_lines = 100
    
    for y in range(num_lines):
        py5.begin_shape()
        for x in range(py5.width):
            noise_val = py5.noise(x * noise_scale, y * noise_scale)
            py5.vertex(x, y * (py5.height / num_lines) + noise_val * 50)
        py5.end_shape()

py5.run_sketch()