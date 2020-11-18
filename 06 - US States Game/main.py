#1. Import Statements
###################################
from turtle import Turtle, Screen
import pandas as pd


#2. Initialize the turtle and the screen
###################################
sc = Screen()
t = Turtle()


#3. Make background and other settings
###################################
SHAPE = "blank_states_img.gif"
sc.bgpic(SHAPE)
sc.title('🇺🇸 Game')

t.penup()
t.hideturtle()


#4. Logistics
###################################
state_guess = []
    #Array to be populated in while loop
df = pd.read_csv('50_states.csv')
all_states = df.state.to_list()
    #Getting an array of states using the CSV file


#5. Game Start
###################################
while len(state_guess) < 50:     #While they haven't guessed all the states
    
    guess = sc.textinput(title = f"State {len(state_guess) + 1}/50", prompt = "Input your state guess, input exit to end").title() #title case
    if guess in all_states: #right guess
        state_guess.append(guess)
        row = df[df.state == guess] #getting the row where the df's state is the guess
        coor = (int(row.x), int(row.y))
        t.goto(coor) 
        t.write(guess) #go to the coordinate and write it
    elif guess == "Exit": #if the user inputs the exit keyword
        break
sc.mainloop() #to keep window open


#6. Exporting all the wrong guesses
###################################
        #List comprehension to make list with the states not guessed
wrong_states = [state for state in all_states if state not in state_guess]
need_to_learn = pd.DataFrame(wrong_states) #storing all of them into a pandas dataframe
need_to_learn.to_csv('state_edu.csv') #export




