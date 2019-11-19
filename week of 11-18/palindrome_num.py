import math

def IsPalindrome(num):
    if num < 10:
        return True
    else:
        # get the largest 10s place
        largest_10 = int(math.log10(num))
        # get first digit in number
        first_dig = int(num/(10**largest_10))
        # get last digit in number
        last_dig = num%10
        # does the first and last digits match?
        match = (first_dig == last_dig)
        # compute new number with first and last digits gone
        new_num = num-(first_dig *(10**largest_10))
        new_num = new_num // 10
        # call function recursively to check the inner digits
        return match and IsPalindrome(new_num)
       

def main():
    num = int(input("Enter number to check: "))
    print(str(num) + " is a palindrome? " +
                    str(IsPalindrome(num)))

main()
    
    
