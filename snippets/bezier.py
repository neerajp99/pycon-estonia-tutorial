
    # 2D Bezier curve
    py5.bezier(x1, y1, x2, y2, x3, y3, x4, y4)

    # 3D Bezier curve
    py5.bezier(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4)

    # Using Py5Graphics object
    g = py5.create_graphics(400, 400)
    g.begin_draw()
    g.move_to(ax, ay)
    g.curve_to(bx, by, cx, cy, dx, dy)
    g.end_draw()
