import turtle
import random

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('purple')
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) #divided half
        self.speed('fastest')
        self.goto(x=random.randint(-270,270),y=random.randint(-270,270))
        
    def changepos(self):
        self.goto(x=random.randint(-270,270),y=random.randint(-270,270))

