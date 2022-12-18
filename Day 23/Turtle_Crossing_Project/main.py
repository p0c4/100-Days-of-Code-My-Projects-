import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_man = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_man.create_car()
    car_man.move_car()

    #Detect collision with car:
    for cars in car_man.car_generated:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Detect collision with finish line:
    if player.ycor() > 280:
        scoreboard.level_up()
        player.go_to_start()
        car_man.increment_move_speed()


screen.exitonclick()
