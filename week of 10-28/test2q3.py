import math

def main():
    n = int(input("Enter number of items in set: "))
    r = int(input("Enter number of items in subset: "))
    p = math.factorial(n)/math.factorial(n-r)
    print("Number of permutions with {} items, {} at a time \
is {}".format(n,r,p))

main()
    
            
