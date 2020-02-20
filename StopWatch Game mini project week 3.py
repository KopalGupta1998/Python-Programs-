# template for "Stopwatch: The Game"

# define global variables
import simplegui
time=0
x=0
y=0
run=False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    d=t%10
    t=t//10
    a=t//60
    b=t%60
    if(b<10):
        b="0"+str(b)
    return str(a)+":"+str(b)+"."+str(d)
  
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def reset():
    timer.stop()
    global time,x,y
    time=0
    x=0
    y=0
def start():
    timer.start()
    global run
    run=True
def stop():
    global time,x,y,run
    if(run):
        timer.stop()
        y=y+1
        if(time%10==0):
            x+=1
    run=False
        
        
# define event handler for timer with 0.1 sec interval
def time_handler():
    global time
    time+=1

# define draw handler
def draw(canvas):
    global time,x,y
    canvas.draw_text(format(time),[100,100],20,"red")
    canvas.draw_text(str(x)+"/"+str(y),[260,30],20,"red")
# create frame
frame=simplegui.create_frame("StopWatch Game",300,200)
frame.set_draw_handler(draw)
timer=simplegui.create_timer(100,time_handler)

# register event handlers
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)

# start frame
frame.start()
# Please remember to review the grading rubric
