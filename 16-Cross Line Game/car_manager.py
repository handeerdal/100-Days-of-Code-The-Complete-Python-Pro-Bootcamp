import turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.cars=[]
        self.hideturtle()
        self.firstspeed=7



    def speedcar(self):
        randomnum=random.randint(1,self.firstspeed)
        if randomnum==1:
             self.createcar()

    def createcar(self):
                newcar=turtle.Turtle()
                newcar.shape('square')
                newcar.penup()
                newcar.setheading(270)
                newcar.shapesize(stretch_wid=2,stretch_len=1)
                new_y= random.randint(-250,200)
                newcar.color(random.choice(COLORS))
                newcar.goto(-300, new_y)
                self.cars.append(newcar)
    
    def carmove(self):
        for i in self.cars:
            i.setx(i.xcor() + MOVE_INCREMENT)
             



