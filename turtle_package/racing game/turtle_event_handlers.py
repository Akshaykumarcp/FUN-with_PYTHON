from shutil import move
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen() # control window

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    temp_heading = tim.heading() + 10
    tim.setheading(temp_heading)

def turn_right():
    temp_heading = tim.heading() - 10
    tim.setheading(temp_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen() # start listening
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()

