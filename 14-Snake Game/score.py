import turtle
import random

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.score=0
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.write(f'Score={self.score}',False,align='center',font=('Arial',15,'normal'))


    def increasescore(self):
        self.clear()
        self.score+=1
        self.write(f'Score={self.score}',False,align='center',font=('Arial',15,'normal'))

    def gameover(self):
        self.clear()
        self.goto(0,0)
        self.write(f'Game OVER\nFinal Score={self.score}',False,align='center',font=('Arial',15,'normal'))
