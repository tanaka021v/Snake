from turtle import Turtle, Screen, write
from Snake import snake
from Apple import apple
from scoreboard import scoreboard

import time
screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake1 = snake()
apple1 = apple()
scoreboard1 = scoreboard()

screen.listen()
screen.onkey(snake1.up, 'w')
screen.onkey(snake1.down, 's')
screen.onkey(snake1.left, 'a')
screen.onkey(snake1.right, 'd')



game_on = True
while game_on:
    screen.update()
    snake1.move()
    time.sleep(0.1)
    
    if snake1.snake_list[0].distance(apple1) < 15:
        apple1.updateposition()
        snake1.add_snake()
        scoreboard1.refreshscore()
    if snake1.snake_list[0].xcor() > 300 or snake1.snake_list[0].xcor() < -300 or snake1.snake_list[0].ycor() > 300  or snake1.snake_list[0].ycor() < -300 :
        snake1.reset()
        scoreboard1.reset()
        print('You Lost')
        time.sleep(1)
        
    for i in range(1, len(snake1.snake_list)-1):
        if snake1.snake_list[0].xcor() == snake1.snake_list[i].xcor() and  snake1.snake_list[0].ycor() == snake1.snake_list[i].ycor():
            snake1.reset()
            scoreboard1.reset()
            print('You Lost')
            time.sleep(1)
            break
            
        
   

screen.exitonclick()