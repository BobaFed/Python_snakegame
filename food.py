from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.new_locatio()

    def new_locatio(self):
        randomx = random.randint(-200, 200)
        randomy = random.randint(-200, 200)
        self.goto(randomx, randomy)