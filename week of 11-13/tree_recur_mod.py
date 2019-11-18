import turtle

def tree(branchLen,t):
    print("branchLen is " + str(branchLen))
    if branchLen > 5:
        
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        print("backward, branchLen is " + str(branchLen))
        if branchLen == 15:
            t.color("green")
            print("green")
        t.backward(branchLen)
        t.color("brown")

def main():
    t = turtle.Turtle()
    ts = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    t.pensize(4)
    tree(75,t)
    ts.exitonclick()

main()
