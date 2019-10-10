# practice 1-2
import turtle
wn = turtle.Screen()
tess=turtle.Turtle()
tess.color("green")

num = int(input("Enter number of legs: "))

turn = angle = 360/num

for i in range(1,num+1):
    tess.forward(20)
    tess.home()
    tess.right(turn)
    turn += angle
tess.hideturtle()

