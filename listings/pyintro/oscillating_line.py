import turtle
import time

turtle = turtle.Turtle()

turtle.speed(0)
turtle.pensize(10)
turtle.left(90)
turtle.speed(1)

def oscillate():
    for x in range(4):
        turtle.pencolor("green")
        turtle.forward(43)
        # time.sleep()
    for x in range(4):
        turtle.pencolor("blue")
        turtle.backward(43)
        # time.sleep()

oscillate()