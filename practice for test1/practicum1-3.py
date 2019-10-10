# practicum 1 - question 3
import turtle

ts=turtle.Screen()
ts.bgcolor("black")

turt=turtle.Turtle()

#set up our graphic to draw
turt.color("white", "green")


#drawing
turt.begin_fill()
turt.left(45)
for i in range(4):    
    turt.forward(50)
    turt.left(90)

turt.end_fill()
turt.shape("blank") # remove the arrowhead

