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

grass = Rectangle(Point(0, 0), Point(1000, 200))
grass.setFill(color_rgb(0, 55, 0))
grass.setOutline(color_rgb(0, 55, 0))
grass.draw(window)

hill = Oval(Point(100, 330), Point(900,-600))
hill.setFill(color_rgb(0,55,0))
hill.setOutline(color_rgb(0, 55, 0))
hill.draw(window)

for i in range(100):
    starX = randint(0, 1000)
    starY = randint(600, 800)
    starRadius = randint(1, 5)
    starColor = "Yellow"
    draw_stars(starX, starY, starRadius, starColor, window)

moon = Oval(Point(850, 770), Point(950,670))
moon.setFill(color_rgb(215,215,215))
moon.setOutline(color_rgb(0, 55, 0))
moon.draw(window)
