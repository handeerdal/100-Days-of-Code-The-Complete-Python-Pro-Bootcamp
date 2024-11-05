import turtle
import time

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        self.hideturtle()

    
    def createscore(self):
        self.write(f'S={self.score}',False,align='center',font=('Courier',49,'normal'))
        
