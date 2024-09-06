
    # Create a point
    py5.point(x, y)
    py5.point(x, y, z)  # 3D point

    # Calculate distance between two points
    distance = py5.dist(x1, y1, x2, y2)

    # Create a line
    py5.line(x1, y1, x2, y2)

    # Set stroke color
    py5.stroke(color)

    # Set stroke weight
    py5.stroke_weight(x)

    # Alternative way using Py5Graphics object
    g = py5.create_graphics(400, 400)
    g.begin_draw()
    g.stroke_weight(0.02)
    g.move_to(x, y)
    g.line_to(x1, y1)
    g.stroke()
    g.end_draw()
