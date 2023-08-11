from turtle import Turtle
from random import randint
class apple(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.up()
        self.shapesize(0.5, 0.5)
        self.color('red')
        self.speed('fastest')
        self.goto(randint(-280,280), randint(-280,280))
    def updateposition(self):
        self.goto(randint(-280,280), randint(-280,280))
        
        