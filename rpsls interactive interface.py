# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Functions that compute RPSLS
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if(name=="rock"):
        return 0
    elif(name =="Spock"):
        return 1
    elif(name=="paper"):
        return 2
    elif(name=="lizard"):
        return 3
    elif(name=="scissors"):
        return 4
    else:
        print "Error: Invalid Name!"

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if(number==0):
        return "rock"
    elif(number==1):
        return "Spock"
    elif(number==2):
        return "paper"
    elif(number==3):
        return "lizard"
    elif(number==4):
        return "scissors"
    else:
        print "Error: Invalid Input"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    print ""
    
    # print a blank line to separate consecutive games
    print "Player chooses "+ player_choice
    # print out the message for the player's choice
    player_number=name_to_number(player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    comp_number=random.randrange(0,5)
    # compute random guess for comp_number using random.randrange()
    comp_choice=number_to_name(comp_number)
    # convert comp_number to comp_choice using the function number_to_name()
    print "Computer chooses "+comp_choice
    # print out the message for computer's choice
    difference= (comp_number-player_number)%5
    # compute difference of comp_number and player_number modulo five
    if(difference==1 or difference==2):
        print "Computer wins!"
    # use if/elif/else to determine winner, print winner message
    elif(difference==3 or difference==4):
        print "Player wins!"
    else:
        print "Player and computer tie!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



     
    
# Handler for input field
def get_guess(guess):
    if not(guess=="rock" or guess=="paper" or guess=="scissors" or guess=="Spock" or guess=="lizard"):
        print ("Error: Bad Input to RPSLS")
    else:
        rpsls(guess)
    


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
