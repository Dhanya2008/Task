print("Vande Bharat.")
ac_coach=500
non_ac_coach=300
coach=input("Enter your coach (ac/non ac): ")
sleeper=450
general=250
seat=input("Enter your preferred seat (general/sleeper): ")
if seat=="sleeper" and coach=="ac":
    print("The ticket cost will be: ",sleeper+ac_coach)
elif seat=="sleeper" and coach=="non ac":
    print("The ticket cost will be: ",sleeper+non_ac_coach)
elif seat=="general"and coach=="ac":
    print("The ticket cost will be: ",general+ac_coach)
elif seat=="general" and coach=="non ac":
    print("The ticket cost will be: ",general+non_ac_coach)
else:
    print("Sorry! Your choice is invalid.")
seat_no=int(input("Enter your  preferred seat no: "))
if seat_no>=1 and seat_no<=50:
    print("Your ticket is confirmed.")    
else:
    print("The is seat unavailable. Kindly choose another seat.") 
meal=input("Choose your preferred meal (breakfast/lunch/dinner): ")
if meal=="breakfast" or meal=="lunch" or meal=="dinner":
    print("Your complementary meal order is confirmed.")
else:
    print("You have not chosen any meal.")        
print("Thank you for choosing Vande Bharat.")
print("Have a safe and comfortable journey.")
