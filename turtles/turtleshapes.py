import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("aliceblue")


tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.shape("circle")
tess.shapesize(1, 1)
tess.penup()
tess.setpos(0,0)


alex = turtle.Turtle()           # create alex and set some attributes
alex.color("red")
alex.shape("square")
alex.shapesize(3, 3)
alex.penup()
alex.setpos(100, 100)


john = turtle.Turtle()           # create john and set some attributes
john.color("green")
john.shape("triangle")
john.shapesize(5, 5)
john.penup()
john.setpos(-100,0)



wn.exitonclick()
