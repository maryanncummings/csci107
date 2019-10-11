#drawpolygon.py
import turtle

def drawPolygon(turt, sides, size):
    angle = 360/sides
    for i in range(sides):
        turt.forward(size)
        turt.left(angle)

sides=int(input("Enter number of sides: "))
size=50
ts=turtle.Screen()
ts.bgcolor("green")

myturt=turtle.Turtle()
myturt.pensize(3)
x_pos = -100.0
y_pos = -100.0
for i in range(3):
    myturt.penup()
    myturt.setpos(x_pos, y_pos)
    myturt.pendown()
    drawPolygon(myturt,sides,size)
    x_pos = x_pos + 75
    y_pos = y_pos + 75
myturt.shape("blank")
          
    
    
