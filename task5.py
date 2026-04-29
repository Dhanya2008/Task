print("Vande Bharat.")
ac_coach=500
non_ac_coach=300
coach=input("Enter your coach (ac/non ac): ")
sleeper=450
general=250
seat=input("Enter your preferred seat (general/sleeper): ")
if seat=="sleeper" and coach=="ac":
    print("The total cost will be: ",sleeper+ac_coach)
elif seat=="sleeper" and coach=="non ac":
    print("The total cost will be: ",sleeper+non_ac_coach)
elif seat=="general"and coach=="ac":
    print("The total cost will be: ",general+ac_coach)
elif seat=="general" and coach=="non ac":
    print("The total cost will be: ",general+non_ac_coach)
else:
    print("Sorry! Your choice is invalid.")
seat_no=int(input("Enter your  preferred seat no: "))
if seat_no>=10 and seat_no<=50:
    print("Your ticket is confirmed.")    
else:
    print("The is seat unavailable. Kindly choose another seat.")     
print("Thank you for choosing Vande Bharat.")
print("Have a safe and comfortable journey.")
