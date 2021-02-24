#P3LAB2c: snowflakes
#Rheanna Howell
#20210224
#CTI - 110 - 0901
#Using turtle graphics and the range() function to draw multi-sided snowflakes
#

import turtle
import random

wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor(128, 128, 128)
wn.title("Howells' Turtle Snowflake")

turtle.colormode(255)
turtle.color(160, 227, 246)
turtle.shape("turtle")

turtle.speed(15)

#snowflake design

sfcolor = ["white", "blue", "purple", "grey", "magenta"]


def snowflake(size):
    turtle.penup()
    turtle.forward(20*size)
    turtle.left(100)
    turtle.pendown()
    turtle.color(random.choice(sfcolor))
    for i in range(16):
        branch(size)
        turtle.left(100)

def branch(size):
    for i in range(5):
        for i in range(5):
            turtle.forward(20*size/5)
            turtle.back(20*size/5)
            turtle.right(100)
        turtle.left(160)
        turtle.backward(20*size/5)
        turtle.left(160)
    turtle.right(160)
    turtle.forward(20*size/5)

for i in range(40):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    sf_size = random.randint(2, 8)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    snowflake(sf_size)

wn.exitonclick()

