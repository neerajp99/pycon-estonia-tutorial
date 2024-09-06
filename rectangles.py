import py5

def setup():
    # Set the size of the canvas to 500x700 pixels
    py5.size(500, 700)
    # Set the background color to black
    py5.background(0)

def draw():
    # Loop through the height of the canvas in steps of 10 pixels
    for y in range(0, 700, 10):
        # Generate a random x-coordinate
        x1 = py5.random(0, 500)
        # Calculate the complementary x-coordinate
        x2 = 500 - x1
        
        # Remove stroke (outline) from shapes
        py5.no_stroke()
        
        # Set fill color to a random grayscale value
        py5.fill(py5.random(255))
        # Draw the left rectangle
        py5.rect(0, y, int(x1), 15)
        
        # Set fill color to another random grayscale value
        py5.fill(py5.random(255))
        # Draw the right rectangle
        py5.rect(int(x1), y, 500, 15)
    
    # Prevent the draw function from looping
    py5.no_loop()

# Run the sketch
py5.run_sketch()