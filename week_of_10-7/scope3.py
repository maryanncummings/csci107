# variable scope
power = 3
def powerof(x, p):
    power = p
    y = x ** power
    return y

def main():
    z = powerof(10, 2)
    print("power is " + str(power))
    print(z)

main()
