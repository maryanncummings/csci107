import turtle  #Outside In 
wn = turtle.Screen() 
wn.bgcolor("light green")
wn.title("Square Outside In")
tess = turtle.Turtle() 
tess.color("blue") 
  
for j in {146, 126, 106, 86, 66, 46, 26}:
    for i in range(4): 
        tess.forward(j) 
        tess.left(90) 
        j = j - 5
  
