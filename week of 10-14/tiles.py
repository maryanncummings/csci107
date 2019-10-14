#draw a tile

import turtle

def draw_tile(turt, width, height):
    turt.pendown()
    turt.color("black", "blue")
    turt.begin_fill()
    
    for i in range(2):
        turt.forward(width)
        turt.left(90)
        turt.forward(height)
        turt.left(90)

    turt.end_fill()

    turt.penup()

def main():
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    win = turtle.Screen()
    turt = turtle.Turtle()
    turt.speed(0)
    turt.penup()

    for row in range(rows):
        for column in range(columns):
            turt.goto((column*10)-(columns*10),
                      (row*10)-(rows*10))
            draw_tile(turt, 10, 10)

    turt.shape("blank")
    win.exitonclick()

main()
            
        
    
