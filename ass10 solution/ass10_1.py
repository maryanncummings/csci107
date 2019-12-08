def printSentences(contents):
    contents = contents.replace("\n", "")
    
    for i in range(4):
        contents = contents.replace(". ", ".")
    
    contents = contents.replace('."','.     "')
    contents = contents.replace(".",".\n")
    print(contents)

def main():
    myfile = open("tale.txt", "r")
    contents = myfile.read()
    printSentences(contents)
    myfile.close()


main()
