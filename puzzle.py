import py5
import random
import noise

THE_SEED = 12396
count = 0

def settings():
    py5.size(550, 700)

def setup():
    global puzz
    py5.random_seed(THE_SEED)
    py5.noise_seed(THE_SEED)
    py5.background("#eec9c3")
    py5.no_stroke()
    
    puzz = Puzzle()
    puzz.inner_shape()
    puzz.inner_grid1(250, 320)
    puzz.inner_chessboard()
    puzz.inner_contour()
    puzz.add_decorative_elements()

def draw():
    # We don't need anything in the draw function
    # as we're generating the puzzle in setup
    pass

def key_pressed():
    if py5.key == 'p':
        py5.save(f"sophisticated_puzzle_{THE_SEED}.png")

class Puzzle:
    def __init__(self):
        self.inner_fill_shape = py5.create_graphics(py5.width, py5.height)
        self.inner_fill_shape.begin_draw()
        self.inner_fill_shape.background("#eabbca")
        self.inner_fill_shape.no_stroke()
        self.inner_fill_shape.end_draw()

        self.final_shape = py5.create_graphics(py5.width, py5.height)
        self.final_shape.begin_draw()
        self.final_shape.background("#eabbca")
        self.final_shape.no_stroke()
        self.final_shape.end_draw()

        self.dx = py5.width
        self.dy = 0
        self.random_factor_left = py5.random(200, 500)
        self.random_factor_right = py5.random(500, 700)
        self.mult_factor = 1 / py5.random(400, 500)
        self.colors = [
            "#e3ecf5", "#e3ecf5", "#3c73a8", "#538bc1", "#FFFFFF",
            "#eabbca", "#eec9c3", "#e3ecf5", "#77a4ce", "#eec9c3",
            "#9bbcdb", "#e3ecf5", "#e3ecf5", "#eec9c3", "#3c73a8",
        ]

    def inner_grid1(self, min_val, max_val):
        rand_increment = py5.random(8, 15)
        rand_size = py5.random(min_val, max_val)
        py5.stroke("#2a5278")
        py5.stroke_weight(1)
        py5.fill(255, 0)
        for i in range(20, int(rand_size), int(rand_increment)):
            for j in range(20, int(rand_size), int(rand_increment)):
                if py5.random(1) > 0.5:
                    py5.square(j, i, 10)
                else:
                    py5.square(j, i, rand_increment)

    def inner_grid2(self):
        py5.random_seed(THE_SEED)
        py5.stroke("#2a5278")
        py5.stroke_weight(1)
        py5.fill(255, 0)
        for i in range(20, py5.height - 20, 10):
            for j in range(20, py5.width - 20, 10):
                py5.square(j, i, 10)

        count = 0
        while count < 300:
            turtle = int(py5.random(26))
            snail = int(py5.random(33))
            monkey = 20 + turtle * 20
            bird = 20 + snail * 20
            py5.fill("#2a5278")
            py5.square(monkey, bird, 10)
            count += 1

    def inner_chessboard(self):
        for i in range(20, py5.width - 20, 10):
            for j in range(20, py5.height - 20, 10):
                noise_factor = int(noise.pnoise2(i * self.mult_factor, j * self.mult_factor) * 80)
                color = self.colors[noise_factor % len(self.colors)]
                py5.fill(color)
                py5.square(i % py5.width, j, 10)

    def inner_shape(self):
        py5.begin_shape()
        py5.fill("#eabbca")
        py5.rect(20, 20, py5.width - 40, py5.height - 40)
        py5.end_shape(py5.CLOSE)

    def inner_contour(self):
        for i in range(20, py5.width - 20, 1):
            self.inner_contour_columns(i, self.final_shape)

        self.inner_contour_columns(self.dx, self.inner_fill_shape)
        py5.image(self.final_shape, -self.dx % py5.width, self.dy)
        py5.image(self.inner_fill_shape, py5.width - (self.dx % py5.width), self.dy)
        self.dx += 0.5
        if self.dx % py5.width == 0:
            self.final_shape.image(self.inner_fill_shape, 0, 0)

    def inner_contour_columns(self, i, img):
        py5.noise_seed(THE_SEED)
        img.begin_draw()
        for j in range(20, py5.height - 20, 1):
            noise_factor = int(noise.pnoise2(i * self.mult_factor, j * self.mult_factor) * 80)
            color = self.colors[noise_factor % len(self.colors)]
            img.fill(color)
            img.square(i % py5.width, j, 1)
        img.end_draw()

    def add_decorative_elements(self):
        # Add circular patterns
        for _ in range(5):
            x = py5.random(50, py5.width - 50)
            y = py5.random(50, py5.height - 50)
            size = py5.random(30, 80)
            self.draw_circular_pattern(x, y, size)

        # Add flowing lines
        py5.stroke("#3c73a8")
        py5.stroke_weight(2)
        py5.no_fill()
        for _ in range(3):
            self.draw_flowing_line()

    def draw_circular_pattern(self, x, y, size):
        py5.push_matrix()
        py5.translate(x, y)
        py5.no_fill()
        py5.stroke("#538bc1")
        py5.stroke_weight(1)
        for i in range(12):
            py5.rotate(py5.TWO_PI / 12)
            py5.begin_shape()
            for j in range(0, 360, 10):
                r = size + py5.sin(j * py5.PI / 180) * 10
                px = r * py5.cos(j * py5.PI / 180)
                py = r * py5.sin(j * py5.PI / 180)
                py5.curve_vertex(px, py)
            py5.end_shape(py5.CLOSE)
        py5.pop_matrix()

    def draw_flowing_line(self):
        py5.begin_shape()
        x = 0
        while x < py5.width:
            y = py5.height / 2 + py5.sin(x * 0.02) * 100 + py5.random(-20, 20)
            py5.curve_vertex(x, y)
            x += 10
        py5.end_shape()

py5.run_sketch()