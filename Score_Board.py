from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times New Roman", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        with open("Data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.update_score_board()
        self.hideturtle()
    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score} \t High Score {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score_board()
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Data.txt", "w") as data:
                data.write(f"{self.highscore}")

        self.score = 0
        self.update_score_board()

