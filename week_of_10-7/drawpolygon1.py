#drawpolygon.py
import turtle

def drawPolygon(turt, sides, size):
    angle = 360/sides
    for i in range(sides):
        turt.forward(size)
        turt.left(angle)

def main():
    # read in number of sides
    sides=int(input("Enter number of sides: "))
    # hardwire size of each side
    size=50

    #set up screen
    ts=turtle.Screen()
    ts.bgcolor("green")

    #set up turtle
    myturt=turtle.Turtle()
    myturt.pensize(3)
    x_pos = -100.0
    y_pos = -100.0
    
    for i in range(3):
        # move turtle to starting position
        myturt.penup()
        myturt.setpos(x_pos, y_pos)
        myturt.pendown()
        
        drawPolygon(myturt,sides,size)

        #change position variables
        x_pos = x_pos + 75
        y_pos = y_pos + 75
        
    myturt.shape("blank")

main()
          
    
    
