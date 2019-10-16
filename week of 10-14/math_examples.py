#using math functions
import math

def main():
    #using math.pi to calculate the area of a circle
    radius = float(input("Enter radius: "))
    circle_area = radius * math.pi
    print("Area of circle with radius {} is {:.2f}".format(radius, circle_area))

    #taking the square root of a number
    num = int(input("Enter a number: "))
    print("square root of {} is {:.2f}".format(num, math.sqrt(num)))

main()
                
