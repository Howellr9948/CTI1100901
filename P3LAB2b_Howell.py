#P3LAB2b: initials
#Rheanna Howell
#20210224
#CTI - 110 - 0901
#Using turtle graphics, write a program that displays your first/last initial.
#

import turtle
wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor(128, 128, 128)
wn.title("Howells' Turtle Initials!")


turtle.colormode(255)
turtle.color(102, 2, 60)
turtle.shape("turtle")

#The code for 'R'

turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(220)
turtle.forward(150)

#The code for 'H'

turtle.penup()
turtle.left(40)
turtle.forward(50)
turtle.left(90)
turtle.pendown()
turtle.forward(200)
turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.pendown()
turtle.forward(200)
turtle.penup()
turtle.right(180)
turtle.forward(100)
turtle.pendown()
turtle.left(90)
turtle.forward(100)

wn.mainloop()
