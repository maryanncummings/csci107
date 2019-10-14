# variable scope
power = 2

def badsquare(x):
    y = x ** power
    return y

def main():
    z = badsquare(10)
    print(z)

main()
