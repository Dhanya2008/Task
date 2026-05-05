def Banking():
    print("HDFC BANK")
    print("Welcome to the ATM")
    acc_no=input("Enter your account no: ")
    password=input("Enter your password: ")
    if acc_no=="1234hdfc" and password=="567b":
        print("Your account is verified")
        print("Username: Dhanya shri")
        print("Account number: 123hdfc ")
        current_amt=int(input("Enter your initial amount: "))
        withdraw_amt=int(input("Enter the amount to withdraw: "))
        if current_amt>withdraw_amt:
            print("The amount you have withdrawn: ",withdraw_amt)
            remaining_balance=current_amt-withdraw_amt
            print("The remaining balance is:",remaining_balance)
        else:
            print("Your initial amount is less than your withdrawal amount")
        add=input("Do you want to deposit any amount?(Yes/No): ")
        if add=="Yes":
            deposit_amt=int(input("Enter the amt to be deposited: "))
            if deposit_amt<0:
                print("You cannot deposit this amount")
            else:
                print("The amount you have deposited: ",deposit_amt)
                final_balance=remaining_balance+deposit_amt
                print("The final balance in your account: ",final_balance)
                print("Thank You")
        else:
            print("The final balance is: ",remaining_balance)
            print("Thank You")
    else:
        print("The account is not available")
Banking()