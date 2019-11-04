# -----------------------------------------+
# Your name                                |
# CSCI 107, Assignment 8                   |
# Last Updated:                            |
# -----------------------------------------|
# Simulate the game Manufactoria by        |
# testing various input strings for        |
# criteria defined by functions.           |
# -----------------------------------------+


# --------------------------------------------------+
# manufactoria: The main function for Assignment 7. |
# --------------------------------------------------+


# -----------------------------------------------------------+
# test: Determine whether a given function accepts a string. |
# -----------------------------------------------------------|
# fn: The function to use, e.g. four_or_more_reds            |
# string: The string to test, e.g. "rrrbbb"                  |
# -----------------------------------------------------------+
    
def test(fn, string):

    if fn(string):
        result = "YES!"
    else:
        result = "no"

    #print('The string "' + string + '" is ' + result)
    print("Testing string", string, "...", result)

# -----------------------------------------------------------+


def main():
    # test strings to see if they contain three blues
    print()
    print("Testing three blues")
    print("---------------------------")
    # these tests should accept
    test(three_blues, "bbb")
    test(three_blues, "rbbb")
    test(three_blues, "rrbrrrrbbrrr")
    test(three_blues, "bbrbrrr")
    # these tests should not accept
    test(three_blues, "bbbbbbbbbbb")
    test(three_blues, "brrrr")
    test(three_blues, "rb")
    test(three_blues, "bbr")  
    test(three_blues, "")

    # test strings to see if they contain same amount of both.
    print()
    print("Testing same of both")
    print("---------------------------")
    # these tests should accept
    test(same_amount_of_both, "")
    test(same_amount_of_both, "rrbb")
    test(same_amount_of_both, "bbbbrrrr")
    test(same_amount_of_both, "brbr")
    test(same_amount_of_both, "rbrbrbrrbb")
    test(same_amount_of_both, "rbbrbbrr") 
    # these tests should not accept
    test(same_amount_of_both, "rbbbbbrbbbbbrbbbb")
    test(same_amount_of_both, "bbbbrbbbb")
    test(same_amount_of_both, "rbbrbbrrb")  
    test(same_amount_of_both, "rrrrr")
    test(same_amount_of_both, "brrbrr")

    # test strings to see if they contain all one color
    print()
    print("Testing all one color")
    print("---------------------------")
    # these tests should accept
    test(all_one_color, "")
    test(all_one_color, "r")
    test(all_one_color, "b")
    test(all_one_color, "rrrr")
    test(all_one_color, "bbbbbbbbbbb")
    # these tests should not accept
    test(all_one_color, "brrrr")
    test(all_one_color, "rb")
    test(all_one_color, "rbb")  
    test(all_one_color, "br")

main()  

