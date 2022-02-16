import turtle

#Screen
wn = turtle.Screen()
wn.bgcolor("lightblue")

#Turtle Player
spaceship = turtle.Turtle()
spaceship.color("red")
spaceship.penup()

#Constant
speed = 1

def up():
    global x
    spaceship.setheading(90)
    x="up"
    print(x)
    return x

def down():
    global x
    spaceship.setheading(270)
    x='down'
    print(x)
    
    
def left():
    global x
    x='left'
    spaceship.setheading(180)
    print(x)

def right():
    global x
    spaceship.setheading(0)
    x='right'
    print(x)

wn.listen()
wn.onkey(up, 'Up')
print(x)
x=wn.onkey(down, 'Down')
print(x)
x=wn.onkey(left, 'Left')
print(x)
x=wn.onkey(right, 'Right')
print(x)
while True:
    spaceship.forward(speed)
    print(x)
