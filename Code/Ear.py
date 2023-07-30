from turtle import *


class Ear:

    def __init__(self, face, side):
        self.myFace = face
        self.side = side
        self.colour = "White"

    def setColour(self, c):
        self.colour = c

    def draw(self):
        penup()
        if self.side == "left":
            setheading(120)
            rotation = 45
        else:
            setheading(45)
            rotation = 40
        forward(self.myFace.getSize())
        right(rotation)
        pendown()

        fillcolor(self.colour)

        begin_fill()

        circle(self.myFace.getSize() / 4, 280)

        end_fill()

        self.myFace.goHome()
