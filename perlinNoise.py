import py5

# Initialize a global list to store points
points = []

def setup():
    global points
    py5.size(700, 700)  # Set canvas size to 700x700 pixels
    py5.background(255)  # Set background to white
    points = []  # Initialize empty list for points
    
    # Create 2000 random points
    for _ in range(2000):
        # Create a new vector with random x and y coordinates
        # x can be outside the canvas width by up to 100 pixels
        newVector = py5.Py5Vector(py5.random(py5.width + 100), py5.random(py5.height))
        points.append(newVector)  # Add the new vector to the points list

def draw():
    global points
    
    for vectorObject in points:
        py5.no_fill()  # Set shapes to have no fill
        py5.noise_seed(2)  # Set a fixed seed for the noise function
        py5.stroke("#333")  # Set stroke color to dark gray
        py5.stroke_weight(0.3)  # Set stroke weight to 0.3
        
        py5.begin_shape()  # Start drawing a shape
        for _ in range(20):  # Create 20 segments for each point
            # Generate a noise value based on the point's position
            # and map it to an angle between 0 and 2π
            noiseValue = py5.remap(py5.noise(vectorObject.x / 500, vectorObject.y / 500), 0, 1, 0, 2*py5.PI)
            
            # Store current position
            x1 = vectorObject.x
            y1 = vectorObject.y
            
            # Calculate new position based on the noise angle
            x2 = x1 + py5.cos(noiseValue)
            y2 = y1 + py5.sin(noiseValue)
            
            py5.vertex(x1, y1)  # Add current position as a vertex
            
            # Update the vector's position
            vectorObject.x = x2
            vectorObject.y = y2
        
        py5.end_shape(py5.OPEN)  # End the shape without closing it

py5.run_sketch()  # Run the sketch