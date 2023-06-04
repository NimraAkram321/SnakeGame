from turtle import Turtle

class Scoreboard(Turtle):
    score_num = 0
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.score()



    def score(self):

        self.write(f"Score : {self.score_num}", False, align = "center" , font=('courier', 18 , 'normal'))
        self.score_num = self.score_num + 1

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align = "center" , font=('courier', 18 , 'normal'))
