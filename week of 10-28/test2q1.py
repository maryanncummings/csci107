import math
import random

def ComputePrintNums():
    total = 0
    for i in range(10):
        num = random.randint(1,20)
        print((str(num)).ljust(2), int(math.pow(num,3)))
        total += num

    return total/10

def main():
    avg = ComputePrintNums()
    print("The average of the numbers is {:.2f}".format(avg))

main()
