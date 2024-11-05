import turtle
import time

class Line(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=2,stretch_len=1,outline=0)
        self.penup()
        self.goto(0,-400)
        self.setheading(90)
        self.hideturtle()
        self.pensize(width=2)
        
        for i in range(-200,200):
            self.penup()
            self.forward(5)
            self.pendown()
            self.forward(5)
    

