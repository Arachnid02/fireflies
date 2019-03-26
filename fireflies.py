from graphics import *
from random import *

def draw_stars(X, Y, rad, col, window):
    star = Circle(Point(X, Y), rad)
    star.setFill(col)
    star.setOutline(col)
    star.draw(window)

window = GraphWin("Starry Night", 1000, 800)
window.setCoords(0, 0, 1000, 800)
window.setBackground(color_rgb(29, 0, 51))

hill = Oval(Point(250, 250), Point(800,-600))
hill.setFill(color_rgb(0,55,0))
hill.draw(window)

for i in range(100):
    starX = randint(0, 1000)
    starY = randint(600, 800)
    starRadius = randint(1, 5)
    starColor = "Yellow"
    draw_stars(starX, starY, starRadius, starColor, window)
