import py5

# Initialize global variables
r, g, b = 175, 130, 215  # Initial RGB color values
opacity = 255  # Initial opacity value
zoff = 0  # Z-offset for 3D noise
rad = 2  # Initial radius

def setup():
    global rad
    py5.size(800, 800)  # Set canvas size
    py5.background(0)  # Set background to black
    py5.frame_rate(30)  # Set frame rate to 30 fps
    rad = 2  # Initialize radius (redundant, as it's already set globally)

def draw():
    global rad, r, g, b, translateX, translateY, opacity, zoff
    
    py5.no_fill()  # Set shapes to have no fill
    py5.stroke(r, g, b, opacity)  # Set stroke color with current RGB and opacity values
    
    py5.begin_shape()  # Start drawing a shape
    a = 0
    while a < py5.TWO_PI:  # Loop through a full circle
        # Generate x and y offsets for noise based on current angle
        xoff = py5.remap(py5.cos(a), -1, 1, 0, 10)
        yoff = py5.remap(py5.sin(a), -1, 1, 0, 10)
        
        # Generate noise factor and map it to a range
        noiseFactor = py5.remap(py5.noise(xoff, yoff, zoff), 0, 1, 100, 150)
        
        # Calculate x and y coordinates for the current point
        x = py5.width / 2 + rad * noiseFactor * py5.cos(a)
        y = py5.height / 2 + rad * noiseFactor * py5.sin(a)
        
        py5.curve_vertex(x, y)  # Add a curve vertex at the calculated point
        a += 0.1  # Increment angle
    
    py5.end_shape(py5.CLOSE)  # End and close the shape
    
    zoff += 0.1  # Increment z-offset for next frame
    rad -= 0.02  # Decrease radius for next frame
    
    # Reset color values if they exceed 255
    if r > 255:
        r = 0
    if g > 255:
        g = 0
    if b > 255:
        b = 0
    
    # Reset opacity if it reaches 0
    if opacity == 0:
        opacity = 255
    
    # Update color and opacity values
    opacity -= 1
    r += 1
    g += 1
    b += 1

py5.run_sketch()  # Run the sketch