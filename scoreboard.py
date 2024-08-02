from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align="center",
                   font=("Courier", 12, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("data.txt", mode="w") as data:
            self.high_score = str(self.high_score)
            data.write(self.high_score)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 12, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
