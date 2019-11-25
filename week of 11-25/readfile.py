
def main():
    myfile = open("tale.txt", "r")

    # read entire contents of file into a huge string
    contents = myfile.read()
    print("Printing all contents with one print")
    print(contents)

    # go back to top of file
    myfile.seek(0)

    # read all lines into an array of strings
    lines = myfile.readlines()

    print("Printing each line of the file")
    for one_line in lines:
        #get rid of the newline so that you don't have a
        # blank line between each line printed
        one_line = one_line.replace("\n", "")
        print(one_line)

    # go back to top of file
    myfile.seek(0)

    print("reading and printing one line at a time")
    #read one line
    line = myfile.readline()
    #make sure you are not at the end of file
    while line:
        # get rid of the newline so that you don't have a
        # blank line between each line printed
        line = line.replace("\n", "")
        print(line)
        line = myfile.readline()

    # close file    
    myfile.close()

main()
