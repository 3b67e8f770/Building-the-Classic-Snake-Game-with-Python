#!/usr/bin/env python3
import turtle
import secrets

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

def print_snake(mouse,snake,m_t,s):         
    m_t.clearstamps()                   # mouse printing
    m_t.goto(mouse[0],mouse[1])
    s.update
    m_t.stamp()
    for i in range(0,len(snake)):       # snake printing
        m_t.goto(snake[i][0],snake[i][1])
        s.update
        m_t.stamp()
    
def snake_coordinates(direction,snake,mouse,score,new_mause=False):   #new snake
    _x=snake[len(snake)-1][0]
    _y=snake[len(snake)-1][1]
    if direction == "up":
        new_haed=[_x,_y+20]
    elif direction == "down":
        new_haed=[_x,_y-20]
    elif direction == "left":
        new_haed=[_x-20,_y]
    else:
        new_haed=[_x+20,_y]
    if new_haed in snake:
        print(f'Game over. Yours score = {score}!')
##        turtle.bye()

    snake.append(new_haed)
    if mouse in snake:                          # if catch the mouse
        mouse=mouse_coordinates(500,500,snake)
        score+=1
        new_mause=True
    else:
        snake.pop(0)
            
    return snake,score,new_mause
    
    


direction="right"
score=0
w = 500                         # width
h = 500                         # high
s = turtle.Screen()             # s=screen
s.setup(w,h)
s.title("Snake")
s.bgcolor("Cyan")
m_t = turtle.Turtle()           #my_turtle
m_t.shape("square")
size=int(20/20)                 # 20 = pixels, 50/20 = 50 pixels
m_t.shapesize(size,size,size)
m_t.pen(pensize=size*20, speed=2*5)
m_t.color("green","Lime")
m_t.penup()                     # no paint marks when moveing
m_t.stamp()                     # 
x_max=int(w/40)*20
y_max=int(w/40)*20
snake=[[-20,0],[0,0],[20,0]]
mouse=mouse_coordinates(w,h,snake)
speed = 2

print_snake(mouse,snake,m_t,s)
s.listen()
direction =s.onkey(up, 'Up')
direction =s.onkey(down, 'Down')
direction =s.onkey(left, 'Left')
direction =s.onkey(right, 'Right')
    
ups=True    
while ups:
    # out of the screen?
    if snake[len(snake)-1][0] not in range(-x_max,x_max) or snake[len(snake)-1][1] not in range(-y_max,y_max):
        ups=False
        break
    # eat itself?
    for i in range(0,len(snake)-2):
        if snake[len(snake)-1] == snake[i]:
            ups=False
            turtle.bye()
    snake,score,new_mause=snake_coordinates(direction,snake,mouse,score)
    if new_mause:
        mouse=mouse_coordinates(w,h,snake)
    print_snake(mouse,snake,m_t,s)

        
turtle.bye()
    
print(f'Game over. Yours score = {score}!')
    


