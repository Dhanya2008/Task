print("Vande Bharat")
ac_coach=500
non_ac_coach=300
coach=input("Enter your coach: ")
sleeper=450
general=250
seat=input("Enter your preferred seat: ")
if seat=="sleeper" and coach=="ac coach":
    print("Your ticket has been confirmed")
    print("The total cost will be: ",sleeper+ac_coach)
if seat=="sleeper" and coach=="non ac coach":
    print("Your ticket has been confirmed")
    print("The total cost will be: ",sleeper+non_ac_coach)
if seat=="general"and coach=="ac coach":
    print("Your ticket has been confirmed")
    print("The total cost will be: ",general+ac_coach)
if seat=="general" and coach=="non ac coach":
    print("Your ticket has been confirmed")
    print("The total cost will be: ",general+non_ac_coach)
print("Thank you for choosing Vande Bharat")