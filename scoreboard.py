from turtle import Turtle

alignment = 'center'
font = ('Courier', 18, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.score = 0
        self.color('medium violet red')
        self.goto(0, 270)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", move=False, align=alignment, font=font)

    def add_point(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", move=False, align=alignment, font=font)

#   def punch_wall(self):
#       self.goto(0, 0)
#       self.write("GAME OVER", align=alignment, font=font)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data2:
                data2.write(f"{self.high_score}")
        self.score = 0
        self.add_point()
