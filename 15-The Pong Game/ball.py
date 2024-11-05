import turtle
import time

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color((58,23,138))
        self.shape('circle')
        self.penup()
        self.setheading(0)

        self.xmove=4
        self.ymove=4

    
    def move(self):
        self.sety(self.ycor() +self.ymove)
        self.setx(self.xcor() + self.xmove)

    def bounce(self):
        self.ymove*=-1

    def paddlebounce(self):
        self.xmove*=-1

    def reset_pos(self):
        self.goto(0,0)
        self.xmove*=-1
