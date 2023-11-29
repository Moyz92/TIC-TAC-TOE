from turtle import Turtle
FONT = ("Courier", 45, "bold")


class Player:
    def __init__(self, name: str, sign: str):
        self.name = name
        self.player_sign = sign

    def make_sign(self, x: float, y: float):
        sign = Turtle()
        sign.hideturtle()
        sign.speed("fastest")
        sign.penup()
        sign.goto(x, y)
        sign.write(self.player_sign, align="center", font=FONT)

    def get_name(self):
        return self.name