import turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270,260)
        self.score=0

        self.write(f'Level={self.score}',False,align='left', font=('Arial',15,'normal'))

    def scoreincrease(self):
        self.score+=1
        self.clear()
        self.write(f'Level={self.score}',False,align='left', font=('Arial',15,'normal'))

    def gameover(self):
        self.clear()
        self.goto(0,0)
        self.write(f'GAME OVER',False,align='center', font=('Arial',15,'normal'))
