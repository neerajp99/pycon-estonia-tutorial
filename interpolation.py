import py5

def setup():
    py5.size(600, 600)
    py5.background(255)
    py5.color_mode(py5.HSB, 360, 100, 100)

def draw():
    initial_color = py5.color(0, 50, 100)
    final_color = py5.color(45, 80, 100)
    py5.no_stroke()
    for i in range(py5.width):
        linear_int_value = py5.remap(i, 0, py5.width, 0, 1.0)
        # Calculates a color between two colors at a specific increment.
        linear_int_color = py5.lerp_color(initial_color, final_color, linear_int_value)
        py5.fill(linear_int_color)
        py5.rect(i, 0, 1, py5.height)
    py5.no_loop()

py5.run_sketch()
