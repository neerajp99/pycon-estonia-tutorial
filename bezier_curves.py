import py5
import random

palettes = [
    ["#69d2e7", "#a7dbd8", "#e0e4cc", "#f38630", "#fa6900"],
    ["#fe4365", "#fc9d9a", "#f9cdad", "#c8c8a9", "#83af9b"],
    ["#ecd078", "#d95b43", "#c02942", "#542437", "#53777a"],
    ["#556270", "#4ecdc4", "#c7f464", "#ff6b6b", "#c44d58"],
    ["#774f38", "#e08e79", "#f1d4af", "#ece5ce", "#c5e0dc"]
]

def bezier_curve(points, x=0.5, y=0.8):
    py5.begin_shape()
    initial_point = points[0]
    py5.vertex(initial_point['x'], initial_point['y'])
    
    curve_point_x, curve_point_y = 0, 0
    
    for i in range(len(points)):
        current_point = points[i]
        if i + 1 < len(points):
            next_point = points[i + 1]
            slope = (next_point['y'] - initial_point['y']) / (next_point['x'] - initial_point['x'])
            curve_point_x2 = (next_point['x'] - current_point['x']) * -x
            curve_point_y2 = curve_point_x2 * slope * y
        else:
            curve_point_x2, curve_point_y2 = 0, 0
        
        py5.bezier_vertex(
            initial_point['x'] - curve_point_x, initial_point['y'] - curve_point_y,
            current_point['x'] + curve_point_x2, current_point['y'] + curve_point_y2,
            current_point['x'], current_point['y']
        )
        
        curve_point_x, curve_point_y = curve_point_x2, curve_point_y2
        initial_point = current_point
    
    py5.end_shape()

def generate_lines():
    final_lines = []
    for j in range(0, 1200, 25):
        line = []
        x = 50
        width_x = 20
        for _ in range(100):
            if x < 570:
                y = j + random.randint(25, 44)
                point = {'x': x, 'y': y}
                line.append(point)
            x += width_x
        final_lines.append(line)
    return final_lines

def setup():
    py5.size(595, 842)  # A4 size in pixels
    py5.background("#04383f")
    
    global final_lines, palette
    final_lines = generate_lines()
    palette = random.choice(palettes)
    
    py5.no_loop()

def draw():
    py5.stroke_weight(1)
    
    for i in range(32):
        py5.stroke(random.choice(palette))
        bezier_curve(final_lines[i], 0.3, 1)

py5.run_sketch()