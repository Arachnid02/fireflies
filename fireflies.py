from graphics import *
from random import *

def draw_circle(X, Y, rad, col, window):
    circle = Circle(Point(X,Y), rad)
    circle.setFill(col)
    circle.setOutline(col)
    circle.draw(window)
    
def draw_stars(X, Y, rad, col, window):
    star = Circle(Point(X, Y), rad)
    star.setFill(col)
    star.setOutline(col)
    star.draw(window)

def draw_sunflowers(X, Y, rad, col1, col2, window):
    flower1Core = draw_circle(X, Y, rad, col1, window)
    for i in range(5):
        flower1Pedal = draw_circle(X - rad, Y - rad, rad, col2, window)

winX = 1000
winY = 800

window = GraphWin("Starry Night", winX, winY)
window.setCoords(0, 0, winX, winY)
window.setBackground(color_rgb(29, 0, 51))

grass = Rectangle(Point((winX * 0), winY * 0),
                  Point((winX / 10) * 10, (winY / 8) * 2))
grass.setFill(color_rgb(0, 55, 0))
grass.setOutline(color_rgb(0, 55, 0))
grass.draw(window)

hill = Oval(Point(winX / 10, (winY / 8) * 3.3),
            Point((winX / 10) * 9, (winY / 8) * -6))
hill.setFill(color_rgb(0,55,0))
hill.setOutline(color_rgb(0, 55, 0))
hill.draw(window)

for i in range(100):
    starRadius = randint(1, 5)
    starColor = "Yellow"
    draw_stars(randint(winX * 0, winX),
               randint((winY / 8) * 6, winY), starRadius, starColor, window)

sunflowerX = 50
sunflowerY = 200
sunflowerRadius = 10
sunflowerColor1 = (color_rgb(43, 29, 14))
sunflowerColor2 = "aquamarine"
draw_sunflowers(sunflowerX, sunflowerY, sunflowerRadius, sunflowerColor1,
                sunflowerColor2, window)

moon = Oval(Point((winX / 10) * 8.5, (winY / 8) * 7.7),
            Point((winX / 10) * 9.5, (winY / 8) * 6.7))
moon.setFill(color_rgb(215,215,215))
moon.setOutline(color_rgb(0, 55, 0))
moon.draw(window)
