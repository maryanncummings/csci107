import turtle
import random

def apple(t):
    t.pensize(1)
    t.color("red")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.color("brown")
def tree(branchLen,t):
    if branchLen > 5:
        if branchLen > 50:
            t.pensize(random.randint(10,12))
            t.color("saddlebrown")
        elif branchLen > 15:
            t.pensize(random.randint(7,10))
            t.color("sienna")
        else:
            t.pensize(random.randint(40,50))
            x = random.randint(0,2)
            if x == 1 or x == 0:
                t.color("green")
                t.pensize(random.randint(50,60))
            else:
                apple(t)
        t.down()
        t.forward(branchLen)
        f= float((random.randint(15,20)))
        t.right(f)
        tree(branchLen-random.randint(5,15),t)
        t.left(2 * f)
        tree(branchLen-random.randint(5,15),t)
        t.right(f)
        t.up()
        t.backward(branchLen)

def tree_close(branchLen,t):
    if branchLen > 5:
        if branchLen > 50:
            t.pensize(random.randint(12,14))
            t.color("saddlebrown")
        elif branchLen > 15:
            t.pensize(random.randint(9,12))
            t.color("saddlebrown")
        else:
            t.pensize(random.randint(22,27))
            t.color("darkgreen")
        t.down()
        t.forward(branchLen)
        f= float((random.randint(15,20)))
        t.right(f)
        tree(branchLen-random.randint(5,15),t)
        t.left(2 * f)
        tree(branchLen-random.randint(5,15),t)
        t.right(f)
        t.up()
        t.backward(branchLen)
        

def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("black")
    t.shape("blank")
    t.left(90)
    t.up()
    t.backward(100)
    t.pensize(10)
    t.color("yellow")
    t.right(90)
    t.forward(100)
    t.down()
    t.begin_fill()
    t.circle(200)
    t.end_fill()
    t.up()
    t.left(90)
    tree(75,t)
    t.color("green")
    t.left(90)
    t.forward(10)
    t.down()
    t.begin_fill()
    t.circle(500)
    t.end_fill()
    t.up()
    t.forward(400)
    t.down()
    t.color("darkgreen")
    t.begin_fill()
    t.circle(400)
    t.end_fill()
    t.up()
    t.right(90)
    wn.exitonclick()

main()
