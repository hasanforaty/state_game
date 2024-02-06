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


guss_set = set()

while game_on:
    user_input = screen.textinput(
        title=f'{len(guss_set)}/50 States Correct',
        prompt="what's another state name ?",
    )
    if user_input is None:
        continue
    if user_input.lower() == 'exit':
        game_over()
    result = states.query(f"state.str.lower() == '{user_input.lower()}'")
    if not result.empty:
        result = result.iloc[0]
        guss_set.add(user_input.lower())
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(result[X_COLUMN], result[Y_COLUMN])
        state_name.write(result[STATE_COLUMN], align='center', font=('Arial', 10, 'bold'))

full_list = states.state.to_list()

un_Answer = []
for state in full_list:
    if state.lower() not in guss_set:
        un_Answer.append(state)
un_Answer_file = pandas.Series(un_Answer)
un_Answer_file.to_csv('un_Answer.csv', index=False)
