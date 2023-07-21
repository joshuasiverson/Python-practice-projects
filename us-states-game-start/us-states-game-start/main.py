import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
states = pandas.read_csv("50_states.csv")
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"Guess the State {correct_guesses}/50",
                                    prompt="What's another state name?").title()
    print(answer_state)
    counter = 0

    if answer_state == 'Exit':
        break
        missed_states = []
        for state in states.state:
            if state not in correct_guesses:
                missed_states.append(state)

        states_to_learn = pandas.DataFrame(missed_states)
        states_to_learn.to_csv("states to learn.csv")

    for state in states.state:
        if answer_state == state:
            writer.goto(states.x[counter], states.y[counter])
            writer.write(answer_state)
            correct_guesses.append(answer_state)
        counter += 1


