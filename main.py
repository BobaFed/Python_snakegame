# First game  | BobaFed
# Made with the help of Python bootcamp 2022

from turtle import Screen
from snake import Snake
import time
from score import Scorebord
from food import Food

screen = Screen()
screen.setup(width=600, height=600) # setting up the canvas
screen.bgcolor("black")
screen.title("SnakeEater")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scorebord()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1) # with this we make it smoother to look at
    snake.move()

    #collisio with food
    if snake.head.distance(food) < 15:
        food.new_locatio()
        snake.bodybuild()
        score.more_score()

    # collisio with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_on = False

    # collisio with tail
    for part in snake.whole_snake[1:]:
        if snake.head.distance(part) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()