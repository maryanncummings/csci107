#towers of hanoi

def printMove(fr, to):
    print("move from " + str(fr) + " to " + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

def main():
    n = 1
    while n != 0:
        Towers(n, "f", "t", "s")
        n = int(input("Enter n: "))

main()
