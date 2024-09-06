import py5
from random import randint, choice

def setup():
    # Set up the canvas size to A4 dimensions (595x842 pixels)
    py5.size(595, 842)
    # Set the background color
    py5.background("#04383f")
    # Disable continuous drawing - we'll draw just once
    py5.no_loop()

def draw():
    # Define sketch parameters
    margin = 40  # Margin around the edge of the canvas
    column_number = 65  # Number of columns to draw
    column_width = 3  # Width of each column
    spacing = 5  # Spacing between rectangles in a column

    # Define color palettes
    palettes = [
        ["#69d2e7", "#a7dbd8", "#e0e4cc", "#f38630", "#fa6900"],
        ["#fe4365", "#fc9d9a", "#f9cdad", "#c8c8a9", "#83af9b"],
        ["#ecd078", "#d95b43", "#c02942", "#542437", "#53777a"],
        ["#556270", "#4ecdc4", "#c7f464", "#ff6b6b", "#c44d58"],
        ["#774f38", "#e08e79", "#f1d4af", "#ece5ce", "#c5e0dc"]
    ]

    # Loop through each column
    for i in range(column_number):
        # Calculate the x-position of the current column
        x = margin + i * (column_width + spacing)
        # Start drawing from the top margin
        y = margin

        # Continue drawing rectangles in the column until we reach the bottom margin
        while y < py5.height - margin:
            # Generate a random height for the rectangle
            rect_height = randint(5, 25)

            # Adjust the height if it would exceed the bottom margin
            if y + rect_height > py5.height - margin:
                rect_height = py5.height - margin - y

            # Choose a random color from a random palette
            py5.fill(choice(choice(palettes)))

            # Draw the rectangle
            py5.rect(x, y, column_width, rect_height)

            # Move the y-position down for the next rectangle
            y += rect_height + spacing


# Run the sketch
py5.run_sketch()