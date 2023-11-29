from turtle import Turtle
FONT = ("Courier", 30, "normal")

# global framework for 2d array to store a boolean which will show state of the game
STATE = [[False, False, False],
         [False, False, False],
         [False, False, False]]

# class starts from here
class Match:
    def __init__(self):
        self.STATE = [[-1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]    # can not initialize with any one thing because matches will be triggered!
        self.rows = 3
        self.column = 3
        self.match_coordinates = [[0, 0], [0, 0]]
    
    def set_state(self, coordinate, item: int):
        self.STATE[coordinate[0]][coordinate[1]] = item

    def get_state(self, row:int, column:int):
        return self.STATE[row][column]


    def check_match(self):
        # 3 horizontal matches 
        if self.STATE[0][0] == self.STATE[0][1] and self.STATE[0][1] == self.STATE[0][2]:
            self.match_coordinates[0] = [-105, 110]
            self.match_coordinates[1] = [105, 110]
            return True
        elif self.STATE[1][0] == self.STATE[1][1] and self.STATE[1][1] == self.STATE[1][2]:
            self.match_coordinates[0] = [-105, 0]
            self.match_coordinates[1] = [105, 0]
            return True
        elif self.STATE[2][0] == self.STATE[2][1] and self.STATE[2][1] == self.STATE[2][2]:
            self.match_coordinates[0] = [-105, -110]
            self.match_coordinates[1] = [105, -110]
            return True

        # 3 vertical matches
        if self.STATE[0][0] == self.STATE[1][0] and self.STATE[1][0] == self.STATE[2][0]:
            self.match_coordinates[0] = [-105, 130]
            self.match_coordinates[1] = [-105, -130]
            return True
        elif self.STATE[0][1] == self.STATE[1][1] and self.STATE[1][1] == self.STATE[2][1]:
            self.match_coordinates[0] = [0, 130]
            self.match_coordinates[1] = [0, -130]
            return True
        elif self.STATE[0][2] == self.STATE[1][2] and self.STATE[1][2] == self.STATE[2][2]:
            self.match_coordinates[0] = [105, 130]
            self.match_coordinates[1] = [105, -130]
            return True
        
        # 2 diagonal matches
        if self.STATE[0][0] == self.STATE[1][1] and self.STATE[1][1] == self.STATE[2][2]:
            self.match_coordinates[0] = [-105, 100]
            self.match_coordinates[1] = [105, -100]
            return True
        elif self.STATE[0][2] == self.STATE[1][1] and self.STATE[1][1] == self.STATE[2][0]:
            self.match_coordinates[0] = [105, 100]
            self.match_coordinates[1] = [-105, -100]
            return True
        return False
    

    def draw_line(self):
        line = Turtle()
        line.hideturtle()
        line.speed("slowest")
        line.pensize(15)
        line.pencolor("red")
        line.penup()
        line.goto(self.match_coordinates[0][0], self.match_coordinates[0][1])
        line.pendown()
        line.goto(self.match_coordinates[1][0], self.match_coordinates[1][1])

    def declare_winner(self, winner:str):
        win = Turtle()
        win.hideturtle()
        win.speed("fastest")
        win.penup()
        win.goto(150, 200)
        win.write(winner + " Won!!", align="center", font=FONT)

    def draw(self, draw_game:str):
        draw = Turtle()
        draw.hideturtle()
        draw.speed("fastest")
        draw.penup()
        draw.goto(150, 200)
        draw.write(draw_game, align="center", font=FONT)