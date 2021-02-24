#P3LAB2a: Shapes
#Rheanna Howell
#20210222
#CTI - 110 - 0901
#Using tutle graphics, and either a while or for loop,
#write a program that draws both a square and a traingle.


import turtle
wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor(230, 251, 255)
wn.title("Howells' Square and Rectangle")


turtle.colormode(255)
turtle.color(138, 154, 91)
turtle.shape("turtle")

#The code for the Square goes here

turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)


#The code for the Rectangle goes here
#We'll change the color for the turtle here

turtle.color(0, 102, 85)
    
turtle.forward(300)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(150)
turtle.left(90)

wn.mainloop()
