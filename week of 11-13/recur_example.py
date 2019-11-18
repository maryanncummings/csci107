def NumBackwards(numstr):
    if len(numstr) == 1:
        return numstr
    else:
        return NumBackwards(numstr[1:]) + numstr[0]
#    str = ""
#    for i in numstr:
#        str = i + str
#    return str

def main():
    # print number backwards
    numstr = input("Enter number: ")
    print(NumBackwards(numstr))

main()
