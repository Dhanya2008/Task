num=int(input("enter the no of series"))
a, b = 0, 1
print("Fibonacci series within the given range:") 
for i in range(num):
    print(a, end=" ") 
    a, b = b, a + b