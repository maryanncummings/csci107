import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess=turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
tess.stamp()
move=30
for i in range(12):
    tess.penup()
    tess.forward(50)
    tess.pendown()
    tess.forward(25)
    tess.penup()
    tess.forward(15)
    tess.stamp()
    tess.home()
    tess.right(move)
    move += 30
