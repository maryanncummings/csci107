import turtle

def sprite(turt, legs, length):
    for i in range(legs):
        turt.forward(length)
        turt.back(length)
        turt.left(360/legs)
        turt.shape("blank")
    
def main():
    turt = turtle.Turtle()
    turt.color("green") 
    legs = int(input("Enter number of legs: "))
    len = int(input("Enter length of each leg: "))
    sprite(turt, legs, len)

main()
