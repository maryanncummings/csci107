#sum of squares

def square(x):
    y = x * x
    return y

def sum_of_squares(x, y):
    a = square(x)
    b = square(y)
    return a + b

def main():
    m = 2
    n = 4
    print("Sum of squares of {} and {} \
is {}".format(m, n, sum_of_squares(m, n)))
    
main()
