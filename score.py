from turtle import Turtle
class Scorebord(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.speed("fastest")
        self.new_scorebord()

    def new_scorebord(self):
        self.write(f"Omnoms:  {self.score} ", align="center", font=("Courier", 12, "normal"))

    def more_score(self):
        self.score += 1
        self.clear()
        self.new_scorebord()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"YOU DIED", align="center", font=("Courier", 12, "normal"))