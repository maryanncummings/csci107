import random

def main():
    
    total = 0
    
    for i in range(100):
        total += random.randint(1,6)

    average = int(total/100)
    print("The avg of 100 dice rolls is " + str(average))


main()
    
