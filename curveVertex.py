import py5

def setup():
    # Set the size of the canvas to 700x700 pixels
    py5.size(700, 700)
    # Set the background color to a dark teal (#013840)
    py5.background("#013840")

def draw():
    # Nested loops to create a grid of shapes
    # Outer loop: horizontal spacing (every 40 pixels)
    for i in range(40, py5.width - 30, 40):
        # Inner loop: vertical spacing (every 40 pixels)
        for j in range(40, py5.height - 30, 40):
            # Set the stroke weight (line thickness) to 1.3
            py5.stroke_weight(1.3)
            # Set the stroke color to white
            py5.stroke(255)
            # Don't fill the shapes
            py5.no_fill()
            
            # Start drawing a shape
            py5.begin_shape()
            
            # Create 6 curve vertices for each shape
            for _ in range(6):
                # Each vertex is slightly offset from the grid position
                # Random offset between -10 and 10 pixels in both x and y directions
                py5.curve_vertex(i + py5.random(-10, 10), j + py5.random(-10, 10))
            
            # Finish drawing the shape
            py5.end_shape()

    # Prevent the draw function from looping
    py5.no_loop()

def key_pressed():
    if py5.key == "s":
        # Save a screenshot of the canvas
        py5.save_frame("curve_vertex.png")  

# Run the sketch
py5.run_sketch()