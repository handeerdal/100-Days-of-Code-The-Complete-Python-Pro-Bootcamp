import time
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

turtle.colormode(255)

screen = turtle.Screen()
screen.bgcolor((242,224,201))
screen.setup(width=600, height=600)
screen.tracer(0)

player_turtle=Player()
screen.listen()
screen.onkey(player_turtle.move,'Up')

car=CarManager()
score=Scoreboard()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.speedcar()
    car.carmove()
    screen.update()
    #collide car
    for all_cars in car.cars:
        if player_turtle.distance(all_cars)<20:
            score.gameover()
            game_is_on=False
    #otherside
    if player_turtle.ycor()>=260:
        player_turtle.goback()
        car.firstspeed-=1
        if car.firstspeed==0:
            car.firstspeed=1
        score.scoreincrease()
        




screen.exitonclick()