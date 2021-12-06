usernameInput = input("Username: ")
passwordInput = input("Password: ")
if usernameInput == "Tualek" and passwordInput == "1997":
    print("Done !")
    print("----Welcome to Green Shop----")
    print("1.Rubber Plant *1  THB 250" )
    print("2.Lucky Bamboo *1  THB 150")
    print("3.Golden Pothos *1  THB 100")
    print("4.Arrowhead Vine *1  THB 120")

    userSelected = int(input("Enter the item number you want : "))
    if userSelected == 1:
        Rubber_Plant_Quantity = int(input("Please fill in the product quantity : "))
        result = (Rubber_Plant_Quantity * 250)
        print("Total")
        print(result)
    elif userSelected == 2:
        Lucky_Bamboo_Quantity = int(input("Please fill in the product quantity : "))
        result = (Lucky_Bamboo_Quantity * 150)
        print("Total")
        print(result)
    elif userSelected == 3:
        Golden_Pothos_Quantity = int(input("Please fill in the product quantity : "))
        result = Golden_Pothos_Quantity * 100
        print("Total")
        print(result)
    elif userSelected == 4:
        Arrowhead_Vine_Quantity = int(input("Please fill in the product quantity : "))
        result = Arrowhead_Vine_Quantity * 120
        print("Total")
        print(result)
print("Thank you so much !")















