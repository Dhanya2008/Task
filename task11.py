seat=2
while seat<=16:
    amount=int(input("Enter the amount: "))
    if amount>=200:
        print("Seat Booked at seat no:",seat)
        seat+=2
    else:
        print("Seat cannot be booked")