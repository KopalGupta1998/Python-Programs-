# implementation of card game - Memory

import simplegui
import random
exposed=["F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F"]
cards=[0,1,2,3,4,5,6,7]
cards2=[0,1,2,3,4,5,6,7]
cards.extend(cards2)
card_index=0
state=0
index1=0
index2=0
counter=0
# helper function to initialize globals
def new_game():
    global card_index,exposed,cards,counter
    counter=0
    label.set_text("Turn = "+str(counter))
    card_index=0
    exposed=["F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F"]
    random.shuffle(cards)

     
# define event handlers
def mouseclick(pos):
    global cards,card_index,exposed,state,index1,index2,counter
    
    card_index=pos[0]//50
    if exposed[card_index]=="F":
        counter+=1
    label.set_text("Turn = "+str(counter))
    if exposed[card_index]=="F":
        exposed[card_index]="T"
        if state == 0:
            state = 1
            index1=card_index
        elif state == 1:
            state = 2
            index2=card_index 
            if cards[index1]==cards[index2]:
                exposed[index1]=True
                exposed[index2]=True
        else:
            state = 1
            index1=card_index
            if cards[index1]==cards[index2]:
                exposed[index1]=True
                exposed[index2]=True
            else:
                for i in range(len(exposed)):
                        if exposed[i]=="T":
                               exposed[i]="F"
                exposed[index1]="T"
    #print exposed
        
    
        
   
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards,exposed
    
    for i in range(len(cards)):
        if exposed[i]=="F":
            canvas.draw_polygon([(i*50,0),((i+1)*50,0),((i+1)*50,100),(i*50,100)],5,"black","green")
        elif exposed[i]=="T" or exposed[i]==True:
            canvas.draw_text(str(cards[i]),[20+2*i*25,50],25,"white")
        


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