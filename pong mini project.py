# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[0,0]
score1=0
score2=0
paddle1_pos=HEIGHT/2
paddle2_pos=HEIGHT/2
paddle1_vel=0
paddle2_vel=0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    ball_vel[1] = -random.randrange(60, 180)/60
    if direction == True:
        ball_vel[0] = random.randrange(120, 240)/60
    else:
        ball_vel[0] = -random.randrange(120, 240)/60
    pass
        
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2 # these are ints
    score1=0
    score2=0
    paddle1_vel=0
    paddle2_vel=0
    paddle1_pos=HEIGHT/2
    paddle2_pos=HEIGHT/2
    spawn_ball(LEFT)

def draw(c):
    global score1, score2, paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos < (HALF_PAD_HEIGHT) and paddle1_vel < 0:
        paddle1_vel = 0
    if paddle2_pos < (HALF_PAD_HEIGHT) and paddle2_vel < 0:
        paddle2_vel = 0
    if paddle1_pos > (HEIGHT - (HALF_PAD_HEIGHT)) and paddle1_vel > 0:
        paddle1_vel = 0
    if paddle2_pos > (HEIGHT - (HALF_PAD_HEIGHT)) and paddle2_vel > 0:
        paddle2_vel = 0
