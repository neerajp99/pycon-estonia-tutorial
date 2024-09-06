import py5

def setup():
    # Set the size of the canvas to 500x500 pixels
    py5.size(500, 500)
    
    # Set the pixel density to 1 (1 pixel = 1 display pixel)
    py5.pixel_density(1)
    
    # Set the level of detail for the Perlin noise
    # Higher values create more detailed noise patterns
    py5.noise_detail(40)

def draw():
    # Initialize the x-offset for the noise function
    xoff = 0
    
    # Load the pixel array for direct manipulation
    py5.load_pixels()
    
    # Loop through each pixel in the canvas
    for x in range(py5.width):
        # Reset the y-offset for each column
        yoff = 0
        for y in range(py5.height):
            # Calculate the index in the 1D pixel array
            index = x + y * py5.width
            
            # Generate a noise value and scale it to 0-255 range
            r = py5.noise(xoff, yoff) * 255
            
            # Randomly decide whether to set the pixel color
            # This creates a sparse, grainy effect
            if py5.random(1) > 0:
                py5.pixels[index] = py5.color(r)
            
            # Increment the y-offset for the next row
            yoff += 0.02
        
        # Increment the x-offset for the next column
        xoff += 0.02
    
    # Update the display with the modified pixel array
    py5.update_pixels()
    
    # Prevent the draw function from looping
    py5.no_loop()

# Run the sketch
py5.run_sketch()