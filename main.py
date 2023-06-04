from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("my Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    #detect the collision

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.clear()
        score.score()


    #detect collision with wall
    if snake.head.xcor() > 282 or snake.head.xcor() < -282 or snake.head.ycor() > 282 or snake.head.ycor() < -282:
        game_is_on = False
        score.game_over()
    #dectect collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <= 10:

            game_is_on = False
            score.game_over()


screen.exitonclick()
