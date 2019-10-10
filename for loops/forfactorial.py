strn = input("Enter factorial number: ")
n = int(strn)
fac = 1
for i in range(1,n):
    fac *= i

print(str(n) + " factorial is " + str(fac))
    
