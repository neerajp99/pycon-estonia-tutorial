import py5
import math

polygon = list()

def random_gauss(m, sd):
    value = 1
    while value >= 1:
        x1 = py5.random(2) - 1
        x2 = py5.random(2) - 1
        value = x1 * x1 + x2 * x2
    value = math.sqrt(-2 * math.log(value) / value)
    y1 = x1 * value
    y2 = x2 * value
    mean = m or 0
    standardDeviation = sd or 1
    return y1 * standardDeviation + mean

def setup():
    py5.size(800, 800)
    py5.background(255)
    py5.color_mode(py5.HSB, 360, 200, 150, 1)
    global polygon

    def getCenterPoint(previous, current, standardDeviation):
        sideX = random_gauss(previous["sideX"] + (current["sideX"] - previous["sideX"]) / 2, standardDeviation)
        sideY = random_gauss(previous["sideY"] + (current["sideY"] - previous["sideY"]) / 2, standardDeviation)
        return {"sideX": sideX, "sideY": sideY}
                                           
    def getMid(mean, standardDeviation):
        newVector = [mean[0]]
        for i in range(1, len(mean)):
            previousValue = mean[i - 1]
            currentValue = mean[i]
            midPoint = getCenterPoint(previousValue, currentValue, standardDeviation)
            newVector.append(previousValue)
            print("Previous", previousValue)
            newVector.append(midPoint)
            print("New", midPoint)
        newVector.append(mean[-1])
        return newVector

    
    sideAngle = 0.5
    while sideAngle < 6:
        sideX = py5.sin(sideAngle) * py5.width / 4
        sideY = py5.cos(sideAngle) * py5.width / 4
        polygon.append({"sideX": sideX, "sideY": sideY})
        sideAngle += 0.6
    
    mid = 50
    while mid > 5:
        for _ in range(3):
            polygon = getMid(polygon, mid)
        mid /= 2

def draw():
    global polygon
    for _ in range(20):
        py5.push()
        py5.no_stroke()
        py5.fill(200, 100, 80, 0.02)
        py5.begin_shape()
        py5.translate(py5.width * 0.5, py5.height * 0.5)
        for j in range(len(polygon)):
            currentVector = polygon[j]
            x = random_gauss(currentVector['sideX'], py5.random(25))
            y = random_gauss(currentVector['sideY'], py5.random(25))
            py5.vertex(x, y)
        py5.end_shape(py5.CLOSE)
        py5.pop()
    py5.no_loop()

py5.run_sketch()