

# find an odd number
def main():
    found_odd = False
    while not found_odd:
        num = int(input("Enter number: "))
        if num%2 != 0:
            found_odd = True
    print(str(num) + " is odd")

main()

        
