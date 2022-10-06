from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.whole_snake = []
        self.createsnake()
        self.head = self.whole_snake[0]

    def createsnake(self):
        """ makes the starting body for snake"""
        for x in START_POSITIONS:
           self.partofsnake(x)

    def partofsnake(self, x):
        """creates one part of snakes body"""
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(x)
        self.whole_snake.append(snake_body)

    def bodybuild(self):
        """ Extends the length of the snake """
        self.partofsnake(self.whole_snake[-1].position())

    def move(self):
        """ makes snakes head move and rest of the body to follow """
        for piece in range(len(self.whole_snake) - 1, 0, -1):  # this is how we got rest of the snakes body to follow the heads movement
            newx = self.whole_snake[piece - 1].xcor()
            newy = self.whole_snake[piece - 1].ycor()
            self.whole_snake[piece].goto(newx, newy)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
