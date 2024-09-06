import py5
import numpy as np

# Function mappings
functions = {
    'sin': np.sin, 'sinh': np.sinh, 'cos': np.cos, 'sqrt': np.sqrt,
    'cbrt': np.cbrt, 'tan': np.tan, 'tanh': np.tanh, 'atan': np.arctan,
    'acos': np.arccos, 'ceil': np.ceil, 'floor': np.floor, 'exp': np.exp,
    'log': np.log, 'round': np.round, 'trunc': np.trunc,
}

u_mul1 = np.sin
u_mul2 = np.cosh
v_mul1 = np.cos
v_mul2 = np.sinh
avr_ = np.sqrt
r_ = np.sin
reset_on_change = True

# Global variables
yy = 0
a = 1
b = 0.2
maxx = maxy = 0

def setup():
    global maxx, maxy, yy
    
    # Increase the size for higher resolution
    py5.size(900, 700, py5.P2D)
    
    avr = avr_(py5.width * py5.height)
    maxx = (avr / py5.height) * py5.PI
    maxy = (avr / py5.width) * py5.PI
    yy = 0
    py5.background(0)
    
    # Set the color mode to RGB with a higher range for smoother gradients
    py5.color_mode(py5.RGB, 1000)

def draw():
    global yy
    if yy < py5.height:
        draw_layer()
    else:
        py5.no_loop()

def draw_layer():
    global yy
    y = py5.remap(yy, 0, py5.height, -maxy, maxy)
    for xx in range(py5.width):
        x = py5.remap(xx, 0, py5.width, -maxx, maxx)
        iter = julia(x, y)
        
        # Use smoother color calculations
        r = int((r_(iter / 12)**2) * 1000)
        g = int((15000 / (iter + 1)) % 1000)
        b = int((25000 / np.log(iter + 2)) % 1000)
        
        py5.stroke(r, g, b)
        py5.point(xx, yy)
    yy += 1

def julia(x, y):
    for iter in range(1000):  # Increase iteration count for more detail
        u = u_mul1(x) * u_mul2(x)
        v = v_mul1(x) * v_mul2(y) 
        x = a * u - b * v
        y = b * u + a * v
        if abs(y) > 50:
            return iter
    return 0

def key_pressed():
    if py5.key == 'r':
        timestamp = f"{py5.month():02d}-{py5.day():02d}_{py5.hour():02d}-{py5.minute():02d}-{py5.second():02d}"
        # Save as a high-quality PNG instead of JPG
        py5.save_frame(f"high_quality_julia_{timestamp}.png")
    elif py5.key == 's':
        global yy
        yy = 0
        py5.background(0)
        py5.loop()

py5.run_sketch()