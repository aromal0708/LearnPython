print("Enter 'S' for Small Pizza 'M' for Medium Pizza and 'L' for Large Pizza")
choice = input("Enter your choice :")
bill = 0
if choice == 'S' or choice == 's' :
    bill = 200
elif choice == 'M' or choice == 'm' :
    bill = 300
elif choice == 'L' or choice == 'l' :
    bill = 400
else :
    bill = 0
    print("Invalid choice")
if bill != 0 :
    pepperoni = input("Do you want Pepperoni (Y/N):")
    if (pepperoni == 'y' or pepperoni == 'Y') and bill == 200 :
        bill +=20
    else :
        bill+=30
    extra_cheese = input("Do you want Extra cheese (Y/N):")
    if(extra_cheese == 'y' or extra_cheese == 'Y'):
        bill +=50
print(f"Your bill is :{bill}")
print("Enjoy your Pizza..")