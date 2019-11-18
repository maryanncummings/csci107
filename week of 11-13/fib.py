def fibonacci(n):
    if n == 1:
        return 1;
    elif n == 2:
        return 1;
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input("Enter n: "))
    string = ""
    for i in range(1,n+1):
        string = string + str(fibonacci(i)) + " "
    print(string)

main()
