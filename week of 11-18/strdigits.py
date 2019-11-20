
def main():
    string = input("Enter string with numbers: ")

    count = 0
    for c in string:
        if c.isdigit():
            count += 1

    print("Number of digits in " + string + " is "
                   + str(count))
        
main()
