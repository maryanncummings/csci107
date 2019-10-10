# Program to print a business card, taking in input
print("Please enter your first name > ")
first = input()
print("Please enter your last name > ")
last = input()
fullname = last + ", " + first
email = first.lower() + "@snow.com"
print("Please enter your phone number > ")
phoneno = input()
print("+------------------------------------------------+")
print("|                                                |")
print("| _[_]_                                          |")
print("| (*'*)         " + fullname.ljust(33) + "|")
print("| ( : )         Snow Flurry Developers           |")
print("| ( : )                                          |")      
print("|               4 FrostBite Plaza                |")
print("| *****            STE 1400                      |")
print("|               Bozeman, MT 59718                |")
print("|                                                |")
print("| Work: " + phoneno.ljust(14) + "  @: " +
      email.ljust(22) + "|")
print("+------------------------------------------------+")

