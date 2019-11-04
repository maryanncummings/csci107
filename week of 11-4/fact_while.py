def factorial(n):
    total = 1
    i = n
    while i != 1:
        total *= i
        i = i - 1
    return total

def main():
    n = int(input("Enter number: "))
    
    n_fact = factorial(n)
    print(str(n) + "! is " + str(n_fact))       

main()
