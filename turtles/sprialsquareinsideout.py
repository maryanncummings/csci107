import turtle  #Inside_Out 
wn = turtle.Screen() 
wn.bgcolor("light green")
wn.title("Square Inside Out")
tess = turtle.Turtle() 
tess.color("blue") 
  
for j in {6,26,46,66,86,106,126,146}:
    for i in range(4): 
        tess.forward(j) 
        tess.left(90) 
        j = j + 5
  
