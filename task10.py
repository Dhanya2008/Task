num=int(input("Enter a number to find its factorial: "))
f=1
for i in range(1,num+1):
    f=f*i
print("The factorial of the given number: ",f)