import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

t = turtle.Turtle()
t.penup()
t.hideturtle()

data = pandas.read_csv("50_states.csv")
dict_data = data.state.to_list()
named_states = []


while len(named_states) <= len(dict_data):
    if len(named_states) == 0:
        change_title = "Guess the State"
    else:
        change_title = f"{len(named_states)}/{len(dict_data)} is correct"

    answer_state = screen.textinput(title=change_title, prompt="What's another state's name?").title()

    if answer_state in dict_data and answer_state not in named_states:

        named_states.append(answer_state)
        input_state = data[data.state == answer_state]
        coord_x = int(input_state.x.to_string(index = False))
        coord_y = int(input_state.y.to_string(index = False))

        t.goto(coord_x, coord_y)
        t.write(answer_state)

    elif answer_state == "Exit":
        break
    elif answer_state in dict_data and answer_state in named_states:
        print(f"The state {answer_state} is in list already")
    else:
        print("There is no such state in America")


# turtle.exitonclick()    we have a break - line 40



