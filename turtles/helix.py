# Python program to draw  
# Spiral  Helix Pattern 
# using Turtle Programming 
  
import turtle 
wn = turtle.Screen() 
turtle.speed(100) 
  
for i in range(100): 
    turtle.circle(5*i) 
    turtle.circle(-5*i) 
    turtle.left(i) 
  
turtle.exitonclick() 
