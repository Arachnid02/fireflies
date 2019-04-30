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
<<<<<<< HEAD
    for i in range(5):
        flower1Pedal = draw_circle(X - rad, Y - rad, rad, col2, window)

winX = 1000
winY = 800

window = GraphWin("Starry Night", winX, winY)
window.setCoords(0, 0, winX, winY)
window.setBackground(color_rgb(29, 0, 51))

grass = Rectangle(Point((winX * 0), winY * 0),
                  Point((winX / 10) * 10, (winY / 8) * 2))
=======
    for i in range(7):
        flower1Pedal = draw_circle(X - rad / 1.5, Y - rad, rad / 2.3, col2, window) #bottom left
        flower2Pedal = draw_circle(X + rad, Y + rad, rad / 2.3, col2, window) #upper right
        flower3Pedal = draw_circle(X + rad / 1.5, Y - rad, rad / 2.3, col2, window) # bottom right
        flower4Pedal = draw_circle(X - rad, Y + rad, rad / 2.3, col2, window) #upper left
        flower5Pedal = draw_circle(X + rad / 15, Y + rad, rad/ 2.3, col2, window) #top
        flower6Pedal = draw_circle(X + rad, Y + rad / 15, rad / 2.3, col2, window) #left
        flower7Pedal = draw_circle(X - rad, Y + rad / 15, rad / 2.3, col2, window) #right
        
window = GraphWin("Starry Night", 1000, 800)
window.setCoords(0, 0, 1000, 800)
window.setBackground(color_rgb(29, 0, 51))

#grass
grass = Rectangle(Point(0, 0), Point(1000, 200))
>>>>>>> 7c9997527760b78cb2eefad7f1961c2bb8a9228c
grass.setFill(color_rgb(0, 55, 0))
grass.setOutline(color_rgb(0, 55, 0))
grass.draw(window)

<<<<<<< HEAD
hill = Oval(Point(winX / 10, (winY / 8) * 3.3),
            Point((winX / 10) * 9, (winY / 8) * -6))
=======
#hill
hill = Oval(Point(100, 330), Point(900,-600))
>>>>>>> 7c9997527760b78cb2eefad7f1961c2bb8a9228c
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

<<<<<<< HEAD
moon = Oval(Point((winX / 10) * 8.5, (winY / 8) * 7.7),
            Point((winX / 10) * 9.5, (winY / 8) * 6.7))
=======
#sunflower
    
stem = Rectangle(Point(50, 195), Point(52, 170))
stem.setFill(color_rgb(152,251,152))
stem.setOutline(color_rgb(152,251,152))
stem.draw(window)

sunflowerX = 50
sunflowerY = 200
sunflowerRadius = 10
sunflowerColor1 = (color_rgb(43, 29, 14))
sunflowerColor2 = "orange"
draw_sunflowers(sunflowerX, sunflowerY, sunflowerRadius, sunflowerColor1,
                sunflowerColor2, window)


#moon
moon = Oval(Point(850, 770), Point(950,670))
>>>>>>> 7c9997527760b78cb2eefad7f1961c2bb8a9228c
moon.setFill(color_rgb(215,215,215))
moon.setOutline(color_rgb(0, 55, 0))
moon.draw(window)
