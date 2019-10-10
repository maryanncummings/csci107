# practicum 1 - problem 2

name = input("Enter your name: ")
width = int(input("Enter the field width: "))

box_line = "+"
for i in range(width-2):
    box_line = box_line + "-"
box_line = box_line + "+"

print(box_line)
print("| " + name.rjust(width-4) + " |")
print(box_line)

            
