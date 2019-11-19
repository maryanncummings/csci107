import math

def IsPalindrome(string):
    
    if len(string) == 0 or len(string) == 1:
        return True
    else:       
        match = string[0] == string[-1]       
        # call function recursively to check the inner digits
        return match and IsPalindrome(string[1:-1])       

def main():
    string = input("Enter string to check: ")
    print(string + " is a palindrome? " +
                    str(IsPalindrome(string)))

main()
    
    
