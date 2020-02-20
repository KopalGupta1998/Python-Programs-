# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
# helper function to start and restart the game
number=100
number_of_guess=0
def new_game():
    global secret_number
    global number_of_guess
    global number
    secret_number=random.randrange(0,number)
    if(number==100):
        number_of_guess=7
    elif(number==1000):
        number_of_guess=10
    
    # initialize global variables used in your code here

    # remove this when you add your code    
   


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global number
    number=100
    # remove this when you add your code    
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global number
    number=1000
    new_game()
    
def input_guess(guess):
    print ""
    guess=int(guess)
    global number_of_guess
    number_of_guess=number_of_guess-1
    if(number_of_guess==0):
        print "You lost the game"
        new_game()
    else:
        print "You have "+ str(number_of_guess)+" guesses left!"
    print "Guess was "+str(guess)
    global secret_number
    if(secret_number>guess):
        print "Higher"
    elif(secret_number<guess):
        print "Lower"
    elif(secret_number==guess):
        print "Correct"
    else:
        print "Something went wrong!"
        
    
    # main game logic goes here	
    
    # remove this when you add your code
    

    
# create frame
frame=simplegui.create_frame("Guess_the_Number",200,200)
frame.add_input("Enter a Number:",input_guess,200)
frame.add_button("Range is [0,100)",range100,100)
frame.add_button("Range is [0,1000)",range1000,100)
# register event handlers for control elements and start frame



# always remember to check your completed program against the grading rubric
