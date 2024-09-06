import py5

def draw():
    # Create an ellipse
    py5.ellipse(a, b, c, d)
    # Creates an ellipse at point a,b with "c" width and "d" height

    # Create a rectangle
    py5.rect(a, b, c, d, tl, tr, br, bl)
    # Creates a rectangle at point a,b with width "c" and height "d"
    # Optional parameters tl, tr, br, bl for rounded corners

    # Create a square
    py5.square(x, y, c)

    # Using Py5Graphics object
    g = py5.create_graphics(400, 400)
    g.begin_draw()
    g.rectangle(a, b, c, d)
    g.arc(x, y, radius, start_angle, stop_angle)
    g.end_draw()
    # Creates a rectangle and an arc
    # For a full ellipse, use stop_angle as py5.TWO_PI

py5.run_sketch()