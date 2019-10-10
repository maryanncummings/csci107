# convert number of pennies to nickels and remaining pennies

print("Enter number of pennies: ")
pennies = int(input())

nickels = pennies // 5

rem_pennies = pennies % 5

print("Number of nickels: " + str(nickels))
print("Number of pennies left: " + str(rem_pennies))
