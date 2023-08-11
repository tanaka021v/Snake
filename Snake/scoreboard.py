from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        with open('highscore.txt', "r") as file:
             self.highscore1 = file.read()
        super().__init__()
        
        self.score= 0
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.write(f'Score: {self.score} / Highscore:{self.highscore1}', align = 'right', font = ('Arial', 23, 'normal'))
        
        
        self.ht()
    def refreshscore(self):
        self.score +=1 
        self.clear()
        self.write(f'Score: {self.score} / Highscore:{self.highscore1}', align = 'right', font = ('Arial', 23, 'normal'))
        
    def reset(self):
        if self.score > int(self.highscore1):
            with open('highscore.txt', "w") as file:
                file.write(str(self.score))
            self.highscore1 = self.score
            
            
            
        self.score = 0
        self.clear()
        self.write(f'Score: {self.score} / Highscore:{self.highscore1}', align = 'right', font = ('Arial', 23, 'normal'))