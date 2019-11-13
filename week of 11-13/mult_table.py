
def PrintHeading(n):
    myst = "  *  |"
    for i in range(1, n+1):
        myst = myst + (str(i)).rjust(3)
    print(myst)
    mystlen = len(myst) - 6
    print("-----+" + ("-"*mystlen))

def PrintRow(cur_m,n):
    st = (str(cur_m)).rjust(3) + "  |"
    for i in range(1,n+1):
        num = i * cur_m
        st = st + (str(num)).rjust(3)
    print(st)
    
def main():
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
    PrintHeading(n)
    for i in range(1,m+1):
        PrintRow(i,n)
        
main()    
