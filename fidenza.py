import py5
import random
import math

# Global variables
trails = []
current_path = []
x, y, breadth = 0, 0, 0
colors = ["#f4f1de", "#e07a5f", "#3d405b", "#81b29a", "#f2cc8f", "#f4f1de", "#e07a5f", "#3d405b", "#81b29a", "#f2cc8f"]

def setup():
    py5.size(500, 800)
    py5.background(255)
    py5.ellipse_mode(py5.CENTER)
    py5.frame_rate(15)
    init_path()

def draw():
    for _ in range(50):
        update_path()

def init_path():
    global x, y, breadth, current_path, trails
    if len(current_path) > 0:
        trails.extend(current_path)
    x = random.uniform(0, py5.width)
    y = random.uniform(0, py5.height)
    breadth = random.uniform(5, 50)

    py5.fill(py5.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    py5.fill(py5.color(random.choice(colors)))
    current_path = []

def update_path():
    global x, y, breadth, current_path

    n = py5.noise(x / py5.width, y / py5.height)
    angle = n * py5.TWO_PI * 2
    x += math.cos(angle) * math.sin(n) * 2
    y += math.sin(angle) * math.cos(n) * 2

    if x < 0 or y < 0 or x > py5.width or y > py5.height:
        init_path()
        return

    collide = any((t['x'] - x) ** 2 + (t['y'] - y) ** 2 < (t['breadth'] / 2 + breadth / 2) ** 2 for t in trails)
    if collide:
        init_path()
        return

    current_path.append({
        'x': x,
        'y': y,
        'breadth': breadth,
    })

    py5.push()
    py5.translate(x, y)
    py5.rotate(angle)
    py5.no_stroke()
    py5.ellipse(0, 0, breadth * 0.5, breadth * 0.5)
    py5.pop()

py5.run_sketch()
