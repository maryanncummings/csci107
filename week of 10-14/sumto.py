def sumTo(n):
    result = (n * (n+1))/2
    return result

#main
n = int(input("Enter n: "))
total = sumTo(n)
print("Sum of 1 to {} is {}".format(n, total))
    
