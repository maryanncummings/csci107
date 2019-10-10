#drawpolygon.py
import turtle

def drawPolygon(turt, sides, size):
    angle = 360/sides
    for i in range(sides):
        turt.forward(size)
        turt.left(angle)

sides=int(input("Enter number of sides: "))
size=int(input("Enter size of each side: "))
ts=turtle.Screen()
ts.bgcolor("green")

myturt=turtle.Turtle()
myturt.pensize(3)
drawPolygon(myturt,sides,size)
myturt.shape("blank")
          
    
    
