import turtle as Turtle 
import pandas as pd
screen=Turtle.Screen()
screen.title("US State Game Quiz")
image="blank_states_img.gif"
screen.addshape(image)
Turtle.shape(image)
data=pd.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]
while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="Whats the State's name?").title()
    if answer_state=="Exit":
        missing_states=[]
        for states in all_states:
            if states not in guessed_states:
                missing_states.append(states)
        dataframe=pd.DataFrame(missing_states)
        dataframe.to_csv("Remaining States.csv")        
        
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=Turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state) 
    
