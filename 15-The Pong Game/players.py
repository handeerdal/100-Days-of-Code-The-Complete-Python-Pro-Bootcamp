import turtle
import time

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color((11,44,74))
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.setheading(180)
        self.speed('fastest')
        self.is_moving_up = False
        self.is_moving_down = False

 
    def up(self):
        self.is_moving_up = True

    def down(self):
            self.is_moving_down = True

    def stop_up(self):
            self.is_moving_up = False

    def stop_down(self):
        self.is_moving_down = False

    def move(self):
        if self.is_moving_up:
            if self.ycor() >= 350:
                pass
            else:
                self.sety(self.ycor() + 10)

        if self.is_moving_down:
            if self.ycor() <= -350:
                pass
            else:
                self.sety(self.ycor() - 10)