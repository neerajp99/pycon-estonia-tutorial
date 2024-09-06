import py5

def setup():
    py5.size(500, 700)
    py5.background(0)

def draw_noise(x, y, size):
    py5.push()
    py5.translate(x, y)
    
    for i in range(500):
        x = py5.random(0, size)
        y = py5.random(0, size)
        w = py5.random(1, 3)
        h = py5.random(1, 3)
        py5.no_stroke()
        py5.fill(py5.random(250))
        if py5.random(0, 1) > 0.7:
            py5.ellipse(x, y, w, h)
    print('hello')
    py5.pop()
    
def draw():
    for y in range(0, 700, 10):
        x1 = py5.random(0, 500)
        x2 = 500 - x1
        print(x1, x2)
        
        py5.no_stroke()
        py5.fill(py5.random(255))
        py5.rect(0, y, int(x1), 15)
        py5.fill(py5.random(255))
        py5.rect(int(x1), y, 500 - int(x1), 15)
    py5.no_loop()

py5.run_sketch()
