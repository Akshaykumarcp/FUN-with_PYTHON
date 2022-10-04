import turtle as t
from turtle import Screen, Turtle
import random

tim = Turtle()
t.colormode(255)
directions = [0,90,180,270]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

tim.pensize(15)
tim.speed("fast")

for _ in range(200):
    tim.color(random_color())
    tim.forward(40)
    tim.setheading(random.choice(directions))

# stay window and exit when only we want to exit
screen = Screen()
screen.exitonclick()