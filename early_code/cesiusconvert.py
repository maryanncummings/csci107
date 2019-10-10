# convert a temperature in celsius to a temperature in degrees
conversion = 1.8

celsius = float(input("Enter degrees in celsius: "))
fahrenheit = round(((celsius * conversion) + 32.0), 1)

print(str(celsius) + " degrees celsius is " + str(fahrenheit)
              + " degrees fahrenheit")
