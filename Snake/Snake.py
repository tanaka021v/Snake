from turtle import Turtle
from time import sleep
starting_position = [(0,0),(-20,0), (-40,0)]
MOVE_DISTANCE = 20
connected = False
class snake():
    def __init__(self):
        
        self.snake_list = []
        self.create_snake()
        
    def create_snake(self):
        for i in starting_position:

            t1 = Turtle()
            t1.speed('fastest')
            t1.shape('square')
            t1.color('white')
            t1.up()
            t1.goto(i)
            self.snake_list.append(t1)
       
    def up(self):
        if self.snake_list[0].heading() != 270:
            self.snake_list[0].setheading(90.0)
        
    def down(self):
        if self.snake_list[0].heading() != 90:
            self.snake_list[0].setheading(270)
        
    def right(self):
        if self.snake_list[0].heading() != 180:
          self.snake_list[0].setheading(0)
        
        
    def left(self):
        if self.snake_list[0].heading() != 0:
          self.snake_list[0].setheading(180)
    
    def add_snake(self):
        t1 = Turtle()
        t1.speed('fastest')
        t1.shape('square')
        t1.color('white')
        t1.up()
        t1.goto(self.snake_list[-1].xcor(), self.snake_list[-1].ycor())
        self.snake_list.append(t1)
    
    def reset(self):
        for seg in self.snake_list:
            seg.goto(700,700)
        self.snake_list.clear()
        self.snake_list = []
        self.create_snake()
    def move(self):
        
 
            for i in range(len(self.snake_list) -1, 0, -1):
                x = self.snake_list[i-1].xcor()
                y = self.snake_list[i-1].ycor()
                self.snake_list[i].goto(x,y)
            self.snake_list[0].forward(MOVE_DISTANCE)
            sleep(0.1)



                
                
            
            


