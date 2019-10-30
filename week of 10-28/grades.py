def what_grade(g):
    if g >= 90:
        str = "A"
    elif 80 <= g and g < 90:
        str = "B"
    elif 70 <= g and g < 80:
        str = "C"
    elif 60 <= g and g < 70:
        str = "D"
    else:
        str = "F"
    return str
    
def main():
    grade = int(input("Enter grade: "))
    letter = what_grade(grade)
    print("Letter grade is " + letter)
    
main()
            
