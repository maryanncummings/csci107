import math

def ComputeCircum(r):
    return math.pi * 2 * r

def ComputeArea(r):
    return math.pi * math.pow(r,2)

def main():
    radius = float(input("Enter radius: "))
    circum = ComputeCircum(radius)
    area = ComputeArea(radius)
    print("The circumference is {:.2f}, the area is {:.2f}".format(circum,area))

main()
