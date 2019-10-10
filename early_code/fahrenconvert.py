# convert a temperature in celsius to a temperature in degrees
conversion = 5.0/9.0

fahrenheit = float(input("Enter degrees in fahrenheit: "))
celsius = round(((fahrenheit - 32.0) * conversion), 1)

print(str(fahrenheit) + " degrees fahrenheit is " + str(celsius)
              + " degrees celsius")
