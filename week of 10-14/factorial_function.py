def factorial(n):
    total = 1
    for num in range(1, n+1):
        total *= num
    return total

#main
#help with my math factorial questions
for n in range(1,10):
    n_fact = factorial(n)
    print(str(n) + "! is " + str(n_fact))       
