import turtle
import pandas

screen = turtle.Screen()
game_on = True
states = pandas.read_csv('50_states.csv')
STATE_COLUMN = 'state'
X_COLUMN = 'x'
Y_COLUMN = 'y'

screen.title('US State Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)


def game_over():
    global game_on
    game_on = False


screen.listen()
screen.onkey(key='q', fun=game_over)

correct_answers = 0
while game_on:
    user_input = screen.textinput(
        title=f'{correct_answers}/50 States Correct',
        prompt="what's another state name ?",
    )
    if user_input is None:
        continue
    result = states.query(f"state.str.lower() == '{user_input.lower()}'")
    if not result.empty:
        result = result.iloc[0]
        correct_answers += 1
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        print(result)
        state_name.goto(result[X_COLUMN], result[Y_COLUMN])
        state_name.write(result[STATE_COLUMN], align='center', font=('Arial', 10, 'bold'))

screen.exitonclick()
