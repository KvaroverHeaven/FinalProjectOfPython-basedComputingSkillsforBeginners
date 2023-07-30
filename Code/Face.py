from turtle import *
from Ear import Ear
from Eye import Eye

# A function is defined for each part, with following steps
#    1. pen up
#    2. move to correct position
#    3. pen down
#    4. draw
#    5. return home


class Face:

    def __init__(self, xpos, ypos, eyeColour):
        self.size = 50
        self.coord = (xpos, ypos)
        self.noseSize = "normal"
        self.leftEye = Eye(self, "left", eyeColour)
        self.rightEye = Eye(self, "right", eyeColour)
        self.leftEar = Ear(self, "left")
        self.rightEar = Ear(self, "right")

    def setSize(self, radius):
        self.size = radius

    def getSize(self):
        return self.size

    # Size is normal, large, small
    def setNoseSize(self, size):
        self.noseSize = size

    def setEarColour(self, c):
        self.leftEar.setColour(c)
        self.rightEar.setColour(c)

    def draw(self):
        self.goHome()
        pensize(7)
        self.drawOutline()
        self.drawMouth()
        self.drawNose()
        self.leftEye.draw()
        self.rightEye.draw()
        self.leftEar.draw()
        self.rightEar.draw()

    def goHome(self):
        penup()
        goto(self.coord)
        setheading(0)

    def drawOutline(self):
        penup()
        forward(self.size)
        left(90)
        pendown()
        circle(self.size, 180)
        penup()
        sety(self.coord[1] + 2)
        forward(7)
        left(29.5)
        pendown()
        circle(self.size * 1.16, 120.15)
        self.goHome()

    def drawMouth(self):
        penup()
        right(90)
        pendown()
        circle(self.size / 6, 135)
        self.goHome()

        penup()
        left(90)
        pendown()
        circle(self.size / 6, -135)

        self.goHome()

    def drawNose(self):
        penup()
        pendown()
        if self.noseSize == "large":
            circle(self.size / 6)
        elif self.noseSize == "small":
            circle(self.size / 10)
        else:
            circle(self.size / 8)

        self.goHome()
