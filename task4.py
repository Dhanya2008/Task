blue=100 #assignment operator
green=100
white=blue+green #arithmetic operator
ball=input("Give the colour of the ball:")
if ball=="blue" or ball=="green": #logical operator
    print("You have won: ",blue)
else:
    print("You have won: ",white)
print("The lcm of green and white: ",green & white) #bitwise operator