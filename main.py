from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# initializing
screen = Screen()
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
l_score = ScoreBoard(x=-50,y=200)
r_score = ScoreBoard(x=50,y=200)
# screen props
screen.tracer(0)
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong Game')

# screen controls
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")


# game
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # must bounce
        ball.bounce_y()

    # detection collision with paddle
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 40) or (ball.xcor() < -320 and ball.distance(l_paddle) < 40):
        ball.bounce_x()

    # detecting r wall pass
    if ball.xcor() > 380:
        l_score.add_score()
        ball.reset_position()

    # detecting l wall pass
    if ball.xcor() < -380:
        r_score.add_score()
        ball.reset_position()




screen.exitonclick()
