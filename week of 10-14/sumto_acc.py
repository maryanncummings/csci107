def sumTo(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result

#main
n = int(input("Enter n: "))
total = sumTo(n)
print("Sum of 1 to {} is {}".format(n, total))
    
