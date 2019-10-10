#funcexample.py
def avgFunction(num1, num2):
    answer = (num1 + num2) / 2
    return answer

def printAverage(avg):
    print("Average is " + str(avg))

#main    
avg = avgFunction(20, 30)
printAverage(avg)

printAverage(avgFunction(50, 100))


