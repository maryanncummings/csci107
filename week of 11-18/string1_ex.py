# what will this print?

def main():
    
    mystring = "MSU Bobcats"
	
    for i in range(len(mystring)):
        print("mystring[" + str(i) + "] is " + mystring[i])
		
    for i in range(1,len(mystring)+1):
        print("mystring[" + str(i*(-1)) + "] is " +
                      mystring[i*(-1)])
	
	
main()
