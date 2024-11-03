import turtle
import time
import score

XPOS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20

class Snake:


    def __init__(self):
        self.squares=[]
        self.createsnake()
        self.head= self.squares[0]
    
    
    def createsnake(self):
        
        for i in XPOS:
            self.add(i)
            # newsquare=turtle.Turtle('square')
            # newsquare.color('white')
            # newsquare.penup()
            # newsquare.goto(i)
            # self.squares.append(newsquare)

    def movesnake(self):
            for i in range(len(self.squares)-1,0,-1):
                x=self.squares[i-1].xcor()
                y=self.squares[i-1].ycor()
                self.squares[i].goto(x,y)
            self.squares[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading()!=0:
         self.head.setheading(180)

    def add(self,position):
            newsquare=turtle.Turtle('square')
            newsquare.color('white')
            newsquare.penup()
            newsquare.goto(position)
            self.squares.append(newsquare)
 
    def extendsnake(self):
        self.add(self.squares[-1].position())

    def tailcollision(self,score):
        gameison=True
        for i in self.squares:
            if i == self.head:
                pass
            elif self.head.distance(i)<15:
                score.gameover()
                gameison=False
        return gameison
                
            

