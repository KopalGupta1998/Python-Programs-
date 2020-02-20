# implementation of card game - Memory

import simplegui
import random


num_list = range(8) + range(8)
exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
cards_flipped = 0
card1 = 0
card2 = 0
turns = 0

# helper function to initialize globals
def indexing(num, list1):
    indexes = []
    for index, value in enumerate(list1):
        if value == num:
            indexes.append(index)
    return indexes

def new_game():
    global num_list, exposed, cards_flipped, turns
    random.shuffle(num_list)  
    cards_flipped = 0
    turns = 0
    exposed = []
    for i in range(16):
        exposed.append(False)
    label.set_text("Turns = " + str(turns))
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global cards_flipped, card1, card2, turns
    bounds = 0
    counter = 0
    for i in range(16):
        if exposed[counter]:
            pass
        elif not exposed[counter]:
            if bounds <= pos[0] <= (bounds + 50):
                exposed[counter] = True
                if cards_flipped == 0:
                    cards_flipped = 1
                    card1 = (bounds / 50)
                    
                elif cards_flipped == 1:
                    cards_flipped = 2
                    card2 = (bounds / 50)
                    
                else:
                    cards_flipped = 1
                    if num_list[card1] == num_list[card2]:
                        exposed[card1] = True
                        exposed[card2] = True
                    else:
                        exposed[card1] = False
                        exposed[card2] = False
                    card1 = (bounds / 50)
                    turns += 1
                    
                    label.set_text("Turns = " + str(turns))
        counter += 1
        bounds += 50
                            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global num_list
    spacing = 12.5
    card_spacing = 0
    
    for num in num_list:
        canvas.draw_text(str(num), (spacing, 75), 60, "White")
        spacing += 50
    for card in indexing(False, exposed):
        card_spacing = card * 50
        canvas.draw_polygon([(card_spacing, 0), (card_spacing, 100), ((card_spacing + 50), 100), ((card_spacing + 50), 0)], 1, "Red", "Green")
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric