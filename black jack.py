# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand=[]
            # create Hand object

    def __str__(self):
        s=""
        for c in self.hand:
            s=s+"The card is a "+str(c.get_rank())+"of "+str(c.get_suit())# return a string representation of a hand
        return s

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        value=0
        n=0
        check=0
        for h in self.hand:
            value=value+VALUES[h.get_rank()]
            if h.get_rank()=='A':
                n+=1
        if n>=1:
            check=value+10
            if check <=21:
                value+=10
        return value
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
            # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        
        for i in range(len(self.hand)):
            pos[0]=pos[0]+i*72
            self.hand[i].draw(canvas,pos)
    def overlap(self, canvas, pos):
        for i in range(len(self.hand)):
            self.hand[i].draw(canvas,pos)# draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck= [] # create a Deck object
        
        for S in SUITS:
            for R in RANKS:
                card= Card(S,R)
                self.deck.append(card)
                

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)   # use random.shuffle()

    def deal_card(self):
        card=self.deck[-1]
        self.deck.remove(card)
        return card	# deal a card object from the deck
    
    def __str__(self):
        s=""
        for c in self.deck:
            s=s+ str(c.get_suit())+str(c.get_rank())+" "
            
        return "Deck contains "+s	# return a string representing the deck


#define event handlers for buttons

def deal():
    global outcome, in_play,deck,player,dealer,score
    if in_play:
        outcome="Player lost!"
        score-=1
    deck=Deck()
    deck.shuffle()
    player=Hand()
    dealer=Hand()
    card1=deck.deal_card()
    card2=deck.deal_card()
    card3=deck.deal_card()
    card4=deck.deal_card()
    player.add_card(card1)
    player.add_card(card2)
    dealer.add_card(card3)
    dealer.add_card(card4)
    

    # your code goes here
    
    in_play = True

def hit():
    global outcome, in_play,deck,player,dealer,score
    if in_play:
        c=deck.deal_card()
        player.add_card(c)
        value=player.get_value()
        if(value>21):
            outcome = "You have busted! and lost the game"
            in_play=False
            score=score-1
           
def stand():
    global outcome, in_play,deck,player,dealer,score
    value=player.get_value()
    vdeal=0
    if value>21:
        print outcome
        in_play=False
        score-=1
    else:
        while vdeal>=17:
            dealer.add_card(deck.deal_card())
            vdeal=dealer.get_value()
        if vdeal>21:
            print "The dealer busts"
            outcome="The player wins"
            in_play=False
            score+=1
            
        elif vdeal<=21:
            if vdeal>=value:
                outcome="The dealer wins"
                in_play=False
                score-=1
            else:
                outcome="The player wins"
                in_play=False
                score+=1             

# draw handler    
def draw(canvas):
    global outcome
    
    # test to make sure that card.draw works, replace with your code below
    player.draw(canvas,[200,300])
    if in_play:
        canvas.draw_image(card_back,CARD_CENTER,CARD_SIZE,[236,148],CARD_SIZE)
        dealer.overlap(canvas,[272,100])
    else:
        dealer.draw(canvas,[200,100])
    canvas.draw_text("BlackJack",[220,40],30,"black")
    canvas.draw_text("Hit or Stand?",[220,248],30,"black")
    canvas.draw_text(outcome,[200,500],30,"black")
    canvas.draw_text("Score: "+str(score),[480,40],30,"black")
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric