import py5

def setup():
    # Set the size of the canvas to 600x600 pixels
    py5.size(600, 600)
    
    # Set the background color to white
    py5.background(255)
    
    # Set the color mode to HSB (Hue, Saturation, Brightness)
    # with ranges: Hue (0-360), Saturation (0-100), Brightness (0-100)
    py5.color_mode(py5.HSB, 360, 100, 100)

def draw():
    # Define the starting color (red)
    # Hue: 0 (red), Saturation: 50%, Brightness: 100%
    initial_color = py5.color(0, 50, 100)
    
    # Define the ending color (orange)
    # Hue: 45 (orange), Saturation: 80%, Brightness: 100%
    final_color = py5.color(45, 80, 100)
    
    # Remove outline from shapes
    py5.no_stroke()
    
    # Loop through each pixel width of the canvas
    for i in range(py5.width):
        # Calculate the interpolation value (0.0 to 1.0)
        # based on the current position in the loop
        linear_int_value = py5.remap(i, 0, py5.width, 0, 1.0)
        
        # Interpolate between the initial and final colors
        # based on the calculated interpolation value
        linear_int_color = py5.lerp_color(initial_color, final_color, linear_int_value)
        
        # Set the fill color to the interpolated color
        py5.fill(linear_int_color)
        
        # Draw a rectangle at the current x-position
        # Width of 25 pixels, full height of the canvas
        py5.rect(i, 0, 25, py5.height)
    
    # Prevent the draw function from looping
    py5.no_loop()

# Run the sketch
py5.run_sketch()