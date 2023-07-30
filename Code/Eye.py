from turtle import *


class Eye:

    def __init__(self, face, side, colour):
        self.myFace = face
        self.side = side
        self.colour = colour

    def setColour(self, c):
        self.colour = c

    def draw(self):
        if self.side == "left":
            setheading(110)
            rotation = 70
        else:
            setheading(45)
            rotation = 90
        penup()
        forward(self.myFace.getSize() / 1.65)

        pendown()
        circle(self.myFace.getSize() / 6)
        """
        penup()
        right(rotation)
        forward(self.myFace.getSize() / 6)
        pendown()
        right(30)
        """
        penup()
        left(rotation)
        if(self.side == "left"):
            forward(self.myFace.getSize() / 9)
        else:
            forward(self.myFace.getSize() / 4.5)
        pendown()
        dot(self.myFace.getSize() / 10, self.colour)

        self.myFace.goHome()
