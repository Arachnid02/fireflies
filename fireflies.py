from graphics import *

window = GraphWin("Starry Night", 1000, 800)
window.setCoords(0, 0, 1000, 800)
window.setBackground(color_rgb(29, 0, 51))


hill = Oval(Point(250, 250), Point(800,-600))
hill.setFill(color_rgb(0,55,0))
hill.draw(window)
