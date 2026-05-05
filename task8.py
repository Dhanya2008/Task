print("| Dhanya Supermarket |")
Shampoos=["Meera","Pilgrim","Himalayas","Sunsilk"]
Meera=12
Pilgrim=10
Himalayas=20
Sunsilk=15
price_meera=100
price_pilgrim=200
price_himalayas=150
price_sunsilk=120
choose_shampoo=input("What shampoo do you need ? ")
if choose_shampoo=="Meera":
    print("The total no of Meera shampoo is: ",Meera)
    no_of_meera_shampoo=int(input("How many shampoos do you need ? "))
    if no_of_meera_shampoo>0 and no_of_meera_shampoo<=12:
        print("The no of shampoos bought: ",no_of_meera_shampoo)
        print("The remaining no of shampoos: ",Meera-no_of_meera_shampoo)
    else:
        print("No of shampoos unavailable")   
elif choose_shampoo=="Pilgrim":
    print("The total no of Pilgrim shampoo is: ",Pilgrim)
    no_of_pilgrim_shampoo=int(input("How many shampoos do you need ? "))
    if no_of_pilgrim_shampoo>0 and no_of_pilgrim_shampoo<=10:
        print("The no of shampoos bought: ",no_of_pilgrim_shampoo)
        print("The remaining no of shampoos: ",Pilgrim-no_of_pilgrim_shampoo)
    else:
        print("No of shampoos unavailable")
elif choose_shampoo=="Himalayas":
    print("The total no of Himalayas shampoo is: ",Himalayas)
    no_of_hima_shampoo=int(input("How many shampoos do you need ? "))
    if no_of_hima_shampoo>0 and no_of_hima_shampoo<=20:
        print("The no of shampoos bought: ",no_of_hima_shampoo)
        print("The remaining no of shampoos: ",Himalayas-no_of_hima_shampoo)
    else:
        print("No of shampoos unavailable")
elif choose_shampoo=="Sunsilk":
    print("The total no of Sunsilk shampoo is: ",Sunsilk)
    no_of_sunsilk_shampoo=int(input("How many shampoos do you need ? "))
    if no_of_sunsilk_shampoo>0 and no_of_sunsilk_shampoo<=10:
        print("The no of shampoos bought: ",no_of_sunsilk_shampoo)
        print("The remaining no of shampoos: ",Sunsilk-no_of_sunsilk_shampoo)
    else:
        print("No of shampoos unavailable")
else:
    print("The shampoo is not available.")
if choose_shampoo=="Meera":
    print("Manufacturing date: 02/04/25")
    print("Expiry Date: 02/04/27")
    print("Price of meera shampoo: ",price_meera)
    discount=10
    disc_price=(no_of_meera_shampoo*price_meera)*10/100
    print("Total price: ",no_of_meera_shampoo*price_meera)
    print("Congrats! you have won a discount of 10%, and a free milkbikis biscuit pack of rupees:5")
    print("Final price (Discounted):",(no_of_meera_shampoo*price_meera)-disc_price)
elif choose_shampoo=="Pilgrim":
    print("Manufacturing date: 03/05/25")
    print("Expiry Date: 03/05/27")
    print("Price of pilgrim shampoo: ",price_pilgrim)
    discount=10
    disc_price=(no_of_pilgrim_shampoo*price_pilgrim)*10/100
    print("Total price: ",no_of_pilgrim_shampoo*price_pilgrim)
    print("Congrats! you have won a discount of 10%, and a free mariegold biscuit pack of rupees:5")
    print("Final price (Discounted):",(no_of_pilgrim_shampoo*price_pilgrim)-disc_price)
elif choose_shampoo=="Himalayas":
    print("Manufacturing date: 04/06/25")
    print("Expiry Date: 04/06/27")
    print("Price of himalayas shampoo: ",price_himalayas)
    discount=10
    disc_price=(no_of_hima_shampoo*price_himalayas)*10/100
    print("Total price: ",no_of_hima_shampoo*price_himalayas)
    print("Congrats! you have won a discount of 10%, and a free goodday biscuit pack of rupees:5")
    print("Final price (Discounted):",(no_of_hima_shampoo*price_himalayas)-disc_price)
elif choose_shampoo=="Sunsilk":
    print("Manufacturing date: 05/07/25")
    print("Expiry Date: 05/07/27")
    print("Price of sunsilk shampoo: ",price_sunsilk)
    discount=10
    disc_price=(no_of_sunsilk_shampoo*price_sunsilk)*10/100
    print("Total price: ",no_of_sunsilk_shampoo*price_sunsilk)
    print("Congrats! you have won a discount of 10%, and a free oreo biscuit pack of rupees:5")
    print("Final price (Discounted):",(no_of_sunsilk_shampoo*price_sunsilk)-disc_price)
else:
    print("Try these shampoos (Meera/Pilgrim/Himalayas/Sunsilk): ")
print("Thank you for shopping with us..")
print("Please give us your feedback in our website (www.dhanyasupermarket.com)")
    

