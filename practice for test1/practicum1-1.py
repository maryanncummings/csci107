

bike = int(input("How much is the bike in dollars? "))
money = int(input("How many dollars do you have now? "))

monthly_save = (bike-money)/12                      

print("You must save ${0:.2f} a month to buy the bike in a year".format(monthly_save))

                      
