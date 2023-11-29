from turtle import Turtle, Screen
from player import Player
from match import Match

def make_format():
    new_turtle = Turtle()
    new_turtle.speed("fastest")
    new_turtle.hideturtle()
    new_turtle.pensize(10)
    new_turtle.right(90)
    new_turtle.penup()
    new_turtle.goto(60, 150)
    new_turtle.pendown()
    new_turtle.forward(300)
    new_turtle.penup()
    new_turtle.goto(-60, 150)
    new_turtle.pendown()
    new_turtle.forward(300)
    new_turtle.penup()

    # horzontal lines
    new_turtle.left(90)
    new_turtle.goto(-150, -60)
    new_turtle.pendown()
    new_turtle.forward(300)
    new_turtle.penup()
    new_turtle.goto(-150, 60)
    new_turtle.pendown()
    new_turtle.forward(300)
    new_turtle.penup()

def calculate_mid_point(cor1, cor2):
    x_mid = (cor1[0] + cor2[0]) / 2
    y_mid = (cor1[1] + cor2[1]) / 2
    return (x_mid, y_mid-35)

def end_game(x, y):
    if -200 < x < -170 and 170 < y < 200:
        print("Game Over!!!!")
        screen.bye()

def make_button():
    end_button = Turtle()
    end_button.hideturtle()
    end_button.speed("fastest")
    end_button.penup()
    end_button.goto(-200, 170)
    end_button.pendown()
    end_button.goto(-170, 170)
    end_button.goto(-170, 200)
    end_button.goto(-200, 200)
    end_button.goto(-200, 170)
    end_button.penup()
    mid_cor = calculate_mid_point((-200, 170), (-170, 200))
    x_cor = mid_cor[0]
    y_cor = mid_cor[1] + 27
    end_button.goto(x_cor, y_cor)
    end_button.write("❌", align="center")


make_format()
counter = 0
match = False

def on_click_game(x, y):
    global counter, match
    state_x = 0
    state_y = 0
    number_of_turns = 8     # from 0 (zero) to 8; total = 9

    # checking coordinates and making appropiate signs at appropiate signs
    if -150 < x < -60 and 60 < y < 150:     #1
        mid_coordinate = calculate_mid_point((-150, 60), (-60, 150))
        x = mid_coordinate[0]
        y = mid_coordinate[1]
        state_x = 0
        state_y = 0

    elif -60 < x < 60 and 60 < y < 150:     #2
        mid_coordinate = calculate_mid_point((-60, 60), (60, 150))
        x = mid_coordinate[0]
        y = mid_coordinate[1]
        state_x = 0
        state_y = 1

    elif 60 < x < 150 and 60 < y < 150:     #3 
        mid_coordinate = calculate_mid_point((60, 60), (150, 150))
        x = mid_coordinate[0]
        y = mid_coordinate[1]
        state_x = 0
        state_y = 2



    elif -150 < x < -60 and -60 < y < 60:   #4
        mid_coordinate = calculate_mid_point((-150, -60), (-60, 60))
        x = mid_coordinate[0]
        y = mid_coordinate[1]
        state_x = 1
        state_y = 0

    elif -60 < x < 60 and -60 < y < 60:     #5
        mid_coordinate = calculate_mid_point((-60, -60), (60, 60))
        x = mid_coordinate[0]
        y = mid_coordinate[1]
        state_x = 1
        state_y = 1

    elif 60 < x < 150 and -60 < y < 60:       #6
        mid_coordinate = calculate_mid_point((60, -60), (150, 60))
        x = mid_coordinate[0]
        y = mid_coordinate[1]
        state_x = 1
        state_y = 2



    elif -150 < x < -60 and -150 < y < -60:       #7
        mid_coordinate = calculate_mid_point((-150, -150), (-60, -60))
        x = mid_coordinate[0]
        y = mid_coordinate[1]
        state_x = 2
        state_y = 0

    elif -60 < x < 60 and -150 < y < -60:       #8
        mid_coordinate = calculate_mid_point((-60, -150), (60, -60))
        x = mid_coordinate[0]
        y = mid_coordinate[1]
        state_x = 2
        state_y = 1

    elif 60 < x < 150 and -150 < y < -60:       #9
        mid_coordinate = calculate_mid_point((60, -150), (150, -60))
        x = mid_coordinate[0]
        y = mid_coordinate[1]
        state_x = 2
        state_y = 2

    else:
        print("wrong area clicked!!!")
    

    if match == False and counter <= number_of_turns:
        Player1 = Player("Player1", "X")     # cross
        Player2 = Player("Player2", "O")   # circle

        if match1.get_state(state_x, state_y) != 0 and match1.get_state(state_x, state_y) != 1: 
            if counter % 2 == 0:
                # even number; player1 plays
                Player1.make_sign(x, y)
                match1.set_state((state_x, state_y), 0)
            else:
                # odd number; player2 plays
                Player2.make_sign(x, y)
                match1.set_state((state_x, state_y), 1)
        else:
            print("already selected")
            counter -= 1

    match = match1.check_match()    # checking if either of the players won the game...

    if match == True:
        screen.onclick(None)
        # call the method of class match to draw the appropiate line
        match1.draw_line()
        # declare the fucking winner nigga
        if match1.get_state(state_x, state_y) == 0:
            match1.declare_winner(Player1.get_name().capitalize())
        else:
            match1.declare_winner(Player2.get_name().capitalize())
        make_button()
        screen.onclick(None)
        screen.onclick(end_game, 1)

    # if the game draws and no one wins...
    if number_of_turns == counter and match == False:
        match1.draw("Draw")
        make_button()
        screen.onclick(None)
        screen.onclick(end_game, 1)


    counter += 1


screen = Screen()
screen.title("TIC-TAC-TOE")
screen.setup(height=600, width=600)
match1 = Match()
screen.onclick(on_click_game, 1)


screen.mainloop()