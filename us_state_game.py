from turtle import Turtle, Screen
import pandas as pd
import time

data = pd.read_csv("50_states.csv")
state = data["state"].to_list()

screen = Screen()
tim = Turtle()
tim.penup()
image = "blank_states_img.gif"
screen.title("U.S. State Game")
screen.addshape(image)
tim.shape(image)
screen.tracer(0)

guess = []
while len(guess) < 50:
    user_guess = screen.textinput(title=f"{len(guess)}/50 State Correct.", prompt="What's the another state name?")
    answer = user_guess.title()

    if answer == "Exit":
        break

    for items in state:
        if items == answer:
            guess.append(answer)
            t = Turtle()
            t.penup()
            t.hideturtle()
            for_loc = data[data["state"] == answer]
            x_axis = for_loc["x"]
            y_axis = for_loc["y"]
            t.goto(int(x_axis), int(y_axis))
            t.write(answer)

for items in state:
    if items in guess:
        continue
    else:
        tu = Turtle()
        tu.penup()
        tu.hideturtle()
        st = data[data["state"] == items]
        x_axis = st["x"]
        y_axis = st["y"]
        tu.goto(int(x_axis), int(y_axis))
        tu.write(items)

screen.exitonclick()
