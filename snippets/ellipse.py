import py5

x, y = 250, 250

def setup():
    py5.size(500, 500)
    py5.background(0)

def draw():
    global x, y
    py5.fill(255)
    py5.ellipse(x, y, 25, 25)

py5.run_sketch()