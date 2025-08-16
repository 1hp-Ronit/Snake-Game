from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times New Roman", 20, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.highscore = 0
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
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score_board()
