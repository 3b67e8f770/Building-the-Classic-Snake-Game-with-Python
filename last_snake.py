#!/usr/bin/env python3
import turtle
import secrets
import time

def up():
    global direction
    if direction!='down':
        direction="up"
    return direction

def down():
    global direction
    if direction!='up':
        direction='down'
    return direction
    
    
def left():
    global direction
    if direction!='right':
        direction='left'
    return direction

def right():
    global direction
    if direction!='left':
        direction='right'
    return direction

def mouse_coordinates(w,h,snake):
    _w=int(w/40)
    _h=int(h/40)      
    mouse=snake[0]
    while mouse in snake:
        _x=secrets.choice(range(-_w,_w))*20
        _y=secrets.choice(range(-_h,_h))*20
        mouse=[_x,_y]
    return mouse

def snake_coordinates(direction, snake):   #new snake
    _x=snake[-1][0]
    _y=snake[-1][1]
    if direction == "up":
        new_haed=[_x,_y+20]
    elif direction == "down":
        new_haed=[_x,_y-20]
    elif direction == "left":
        new_haed=[_x-20,_y]
    else:
        new_haed=[_x+20,_y]
        
    return new_haed

direction="right"
score=0
w = 500                         # width
h = 500                         # high

# s=screen
s = turtle.Screen()            
s.setup(w,h)
s.title("Snake")
s.bgcolor("Cyan")

# snake
m_t = turtle.Turtle()           #my_turtle
m_t.shape("square")
size=int(20/20)                 # 20 = pixels, 50/20 = 50 pixels
m_t.shapesize(size,size,size)
m_t.pen(pensize=size*20, speed=2*500)
m_t.color("green","Lime")
m_t.penup()                     # no paint marks when moveing

x_max=int(w/40)*20
y_max=int(w/40)*20
snake=[[-20,0],[0,0],[20,0]]
snake_stamps=[]

for i in snake:
    m_t.goto(i)
    snake_stamps.append(m_t.stamp())

# mouse
m_m = turtle.Turtle()
m_m.shape("circle")
m_m.shapesize(size/2,size/2,size/2)
m_m.color("Red")
m_m.pen(speed=1000)
m_m.penup()                      # no paint marks when moveing
mouse=mouse_coordinates(w,h,snake)
m_m.goto(mouse)
m_m_stamp=m_m.stamp()

# keys
s.listen()
direction =s.onkey(up, 'Up')
direction =s.onkey(down, 'Down')
direction =s.onkey(left, 'Left')
direction =s.onkey(right, 'Right')
new_head=[100,100]

while True:
    time.sleep(0.05)
    new_head = snake_coordinates(direction, snake)
    if new_head[0] not in range(-x_max,x_max) or new_head[1] not in range(-y_max,y_max) or new_head in snake :
        print(f'Game over. Yours score = {score}!')
        turtle.bye()
        break
    else:
        snake.append(new_head)
        m_t.goto(new_head)
        snake_stamps.append(m_t.stamp())
        if mouse != new_head:
            m_t.clearstamp(snake_stamps[0])
            snake_stamps.pop(0)
            snake.pop(0)
        else:
            score += 1
            m_m.clearstamp(m_m_stamp)
            mouse=mouse_coordinates(w,h,snake)
            m_m.goto(mouse)
        







