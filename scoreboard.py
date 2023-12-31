from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_score()

    def increase_score(self) -> None:
        self.clear()
        self.score += 1
        self.update_score()

    def update_score(self) -> None:
        self.write(arg=f"Score: {self.score}", move=False,
                   align=ALIGNMENT, font=FONT)

    def game_over(self) -> None:
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER", move=False,
                   align=ALIGNMENT, font=FONT)

