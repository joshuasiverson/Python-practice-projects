from turtle import Turtle

START_SPOTS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.python = []
        self.gomu_gomu_no_culverine()
        self.fist = self.python[0]
        self.shut_off = False

    def gomu_gomu_no_culverine(self):
        for i in START_SPOTS:
            self.stretch(i)

    def stretch(self, position):
        culverine = Turtle(shape='square')
        culverine.color('magenta')
        culverine.fillcolor('dark red')
        culverine.penup()
        culverine.goto(x=position)
        culverine.speed('fast')
        self.python.append(culverine)

    def extend(self):
        p = self.python[-1].position()
        self.stretch(p)

    def chase(self):
        for gomu in range(len(self.python) - 1, 0, -1):
            new_x = self.python[gomu - 1].xcor()
            new_y = self.python[gomu - 1].ycor()
            self.python[gomu].goto(new_x, new_y)
        self.python[0].forward(MOVE_DISTANCE)

    def new_attack(self):
        for g in self.python:
            g.goto(1000, 1000)
        self.python.clear()
        self.gomu_gomu_no_culverine()
        self.fist = self.python[0]

    def up(self):
        if self.fist.heading() != DOWN:
            self.fist.setheading(UP)

    def down(self):
        if self.fist.heading() != UP:
            self.fist.setheading(DOWN)

    def left(self):
        if self.fist.heading() != RIGHT:
            self.fist.setheading(LEFT)

    def right(self):
        if self.fist.heading() != LEFT:
            self.fist.setheading(RIGHT)

    def end_game(self):
        self.shut_off = True
