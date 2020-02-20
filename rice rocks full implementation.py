# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
angle=0
ANGLE_VELOCITY=0.05
MOTION_KEYS = ["left", "right", "up", "space"]
FRICTION=0.01
THRUST=0.1
ROCK_ANGLE_VEL = 0.1
# Rock's min and max "angular velocity".
ROCK_MIN_ANGLE_VEL= -0.15
ROCK_MAX_ANGLE_VEL= 0.15
# Rock's min and max "velocity".
ROCK_MIN_VELOCITY = -1
ROCK_MAX_VELOCITY = 1
MISSILE_SPEED = 8
missile_pos=[0,0]
missile_pos=[0,0]
started=False
rock_group=set([])
missile_group=set([])
MAX_LIVES=3
MAX_ROCK=12
VELOCITY_SCALING_FACTOR = 10
SCORE_SCALING_FACTOR = 10
EXPLOSION_ANIMATIONS = 24
explosion_group=set([])
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
    
    def get_position(self):
        return self.pos
    def get_radius(self):
        return self.radius
    def draw(self,canvas):
        
        if not self.thrust:        
            canvas.draw_image(self.image,
                             (self.image_center[0], self.image_center[1]),
                             (self.image_size[0], self.image_size[1]),
                             (self.pos[0], self.pos[1]),
                             (self.image_size[0], self.image_size[1]),
                              self.angle)
        else:
            canvas.draw_image(self.image,
                             (3 * self.image_center[0], self.image_center[1]),
                             (self.image_size[0], self.image_size[1]),
                             (self.pos[0], self.pos[1]),
                             (self.image_size[0], self.image_size[1]),
                              self.angle)            
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[0]%=WIDTH
        self.pos[1]%=HEIGHT
        self.vel[0]*=(1-FRICTION)
        self.vel[1]*=(1-FRICTION)
        if self.thrust:
            forward = angle_to_vector(self.angle)
            self.vel[0] += forward[0] * THRUST
            self.vel[1] += forward[1] * THRUST                    
        
        
    def adjust_orientation(self, angle_vel):
        self.angle_vel += angle_vel
        return None
    def set_thrust(self, on_off):
        
        self.thrust = on_off  
        
        if self.thrust:                          
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()            
        else:
            
            ship_thrust_sound.pause()
        
        return None
    def shoot(self):
        global missile_pos,missile_vel,missile_group
        forward=angle_to_vector(self.angle)
        missile_pos=[self.pos[0]+forward[0]*self.radius,self.pos[1]+forward[1]*self.radius]
        missile_vel=[self.vel[0]+forward[0]*MISSILE_SPEED,self.vel[1]+forward[1]*MISSILE_SPEED]
        a_missile = Sprite(missile_pos, missile_vel, 0, 0, missile_image, missile_info, missile_sound)
        missile_group.add(a_missile)

    

def keydown(key):  
    if key == simplegui.KEY_MAP[MOTION_KEYS[0]]:
        my_ship.adjust_orientation(-ANGLE_VELOCITY)
        
    if key == simplegui.KEY_MAP[MOTION_KEYS[1]]: 
        my_ship.adjust_orientation(ANGLE_VELOCITY)
        
    if key == simplegui.KEY_MAP[MOTION_KEYS[2]]:
        my_ship.set_thrust(True)
    if key==simplegui.KEY_MAP[MOTION_KEYS[3]]:
       
        my_ship.shoot()
def keyup(key):
    
    if key == simplegui.KEY_MAP[MOTION_KEYS[0]]:
        
        my_ship.adjust_orientation(ANGLE_VELOCITY)
                
    if key == simplegui.KEY_MAP[MOTION_KEYS[1]]:
        my_ship.adjust_orientation(-ANGLE_VELOCITY)
         
    if key == simplegui.KEY_MAP[MOTION_KEYS[2]]:
        my_ship.set_thrust(False) 
        
def click(pos):

    center = [WIDTH / 2, HEIGHT / 2]

    size = splash_info.get_size()

    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)

    global started, lives, score, my_ship
    if (not started) and inwidth and inheight:
        started = True
        # Make sure lives and score are properly 
        # initialized.
        lives = MAX_LIVES
        score = 0
        # Stop playing the sound, and 
        # make it so the next "sound.play()" will 
        # start playing the background music at the 
        # beginning.                                                 
        soundtrack.rewind()
        soundtrack.play() 
        # Initialize ship.
        #my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 
        #               0, ship_image, ship_info)

    return None                   
        
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
    def get_position(self):
        return self.pos
    def get_radius(self):
        return self.radius
    def draw(self, canvas):
        if not self.animated:
            canvas.draw_image(self.image,self.image_center,self.image_size,self.pos,self.image_size,self.angle)
        else:
            image_index=(self.age % EXPLOSION_ANIMATIONS)//1
            image_center=[self.image_center[0]+(self.image_size[0]*image_index),self.image_center[1]]
            canvas.draw_image(self.image, image_center, 
                              self.image_size, self.pos, 
                              self.image_size, self.angle) 

    
    def update(self):
        self.angle+=self.angle_vel
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]
        self.pos[0]%=WIDTH
        self.pos[1]%=HEIGHT
        self.age+=1
        if self.age >=self.lifespan:
            return True
        else:
            return False
    def collide(self,other_object):
        return dist(self.pos,other_object.get_position())<(self.radius+other_object.get_radius())
    
           
def draw(canvas):
    global time,lives,score,rock_group,started
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_text("Score: "+str(score),[700,50],20,"white")
    canvas.draw_text("Lives Remaining: "+str(lives),[50,50],20,"white")
    # draw ship and sprites
    my_ship.draw(canvas)
    process_sprite_group(rock_group,canvas,"draw")
    process_sprite_group(missile_group,canvas,"draw")
    process_sprite_group(explosion_group,canvas,"draw")
    # update ship and sprites
    my_ship.update()
    process_sprite_group(rock_group,canvas,"update")
    process_sprite_group(missile_group,canvas,"update")
    process_sprite_group(explosion_group,canvas,"update")
    if group_collide(rock_group,my_ship):
        lives-=1
    score += group_group_collide(rock_group, missile_group) * SCORE_SCALING_FACTOR
    # draw splash screen if not started
    if lives==0:
        started=False
        rock_group=set([])
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
       
            
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group,score
    if not started:
        return None
    if len(rock_group) >= MAX_ROCK:
        return None
    velocity_range=ROCK_MAX_VELOCITY-ROCK_MIN_VELOCITY
    rock_vel=[random.random()*velocity_range+ROCK_MIN_VELOCITY,random.random()*velocity_range+ROCK_MIN_VELOCITY]
    if score > 0: 
        rock_vel = [rock_vel[0] * math.ceil(float(score) / (VELOCITY_SCALING_FACTOR * SCORE_SCALING_FACTOR)),
                    rock_vel[1] * math.ceil(float(score) / (VELOCITY_SCALING_FACTOR * SCORE_SCALING_FACTOR))]
    
    angle_velocity_range=ROCK_MAX_ANGLE_VEL-ROCK_MIN_ANGLE_VEL
    rock_angle_vel=random.random()*angle_velocity_range+ROCK_MIN_ANGLE_VEL
    rock_pos=[random.randrange(0,WIDTH-1),random.randrange(0,HEIGHT-1)]
    while dist(rock_pos, my_ship.pos) < ( (2 * my_ship.radius) + 30):                          
        rock_pos = [random.randrange(0, WIDTH - 1), 
                    random.randrange(0, HEIGHT - 1)]
        
    a_rock=Sprite(rock_pos, rock_vel, 
                    0, rock_angle_vel, 
                    asteroid_image, asteroid_info)  
    rock_group.add(a_rock)

def process_sprite_group(sprite_group,canvas,method):
    group_copy=set(sprite_group)
    for sprite in group_copy:
        if method=="draw":
            sprite.draw(canvas)
        else:
            remove_sprite=sprite.update()
            if remove_sprite:
                sprite_group.remove(sprite)
def group_collide(group,other_object):
    collision=False
    group_copy=set(group)
    for object in group_copy:
        if object.collide(other_object):
            collision=True
            group.remove(object)
            explosion = Sprite(object.get_position(), 
                               [0, 0], 0, 0,
                               explosion_image, 
                               explosion_info, 
                               explosion_sound) 
            explosion_group.add(explosion)
    return collision
def group_group_collide(group_1,group_2):
    number_of_collisions=0
    group1_copy=set(group_1)
    for object in group1_copy:
        collision=group_collide(group_2,object)
        if collision:
            number_of_collisions+=1
            group_1.discard(object)
    return number_of_collisions
            
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)
# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0],0, ship_image, ship_info)
#a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, ROCK_ANGLE_VEL, asteroid_image, asteroid_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()