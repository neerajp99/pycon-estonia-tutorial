import py5

def setup():
    py5.size(700, 700)
    py5.background(0)
    py5.stroke(255)
    py5.stroke_weight(0.5)
    py5.no_fill()
    global offset
    offset = py5.random(100)

def draw():
    global offset
    x, y = [], []
    m, n = 20, 70
    
    if py5.frame_count <= 600:
        for i in range(4):
            x.append(py5.width * py5.noise(offset + m))
            y.append(py5.height * py5.noise(offset + n))
            m += 10
            n += 10
        
        py5.bezier(x[0], y[0], x[1], y[1], x[2], y[2], x[3], y[3])
        offset += 0.005

py5.run_sketch()