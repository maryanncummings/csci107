def NumBackwards(numstr):

    str = ""
    for i in numstr:
        str = i + str
    return str

def main():
    # print number backwards
    numstr = input("Enter number: ")
    print(NumBackwards(numstr))

main()
