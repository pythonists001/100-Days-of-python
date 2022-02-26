from hashlib import new
import turtle
import pandas as pd
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "Day 25 - Working with CSV Data and the Pandas Library/blank_states_img.gif"
states_csv = "Day 25 - Working with CSV Data and the Pandas Library/50_states.csv"

screen.addshape(image)

turtle.shape(image)
data = pd.read_csv(states_csv)
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        
        new_data.to_csv("Day 25 - Working with CSV Data and the Pandas Library/states_to_learn.csv")
        break
    # print(answer_state)
    if answer_state in all_states and (answer_state not in guessed_states):
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state) #state_data.state.item()

# turtle.mainloop()
## States to learn.csv
