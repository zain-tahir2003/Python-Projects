print("Welcome to python pizza")
size = input("Enter size of your pizza(Small(S), Medium(M), Large(L))")
add_pepperoni = input("Do You Want Pepperoni On Your Pizza(Y/N) ")
extra_cheese = input("Do You Want Extra Cheese?(Y/N) ")
if size == "S":
    cost = 15
    if add_pepperoni == "Y":
        cost = cost + 2
    
        print(f"Your Cost with pepperoni is ${cost}")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            cost = cost + 1
            print(f"Your Cost is ${cost}")
        elif extra_cheese == "N":
            print(f"Your Cost is ${cost}")
    if extra_cheese == "Y":
        cost = cost + 1
        print(f"Your Cost is ${cost}")
    elif extra_cheese == "N":
            print(f"Your Cost is ${cost}")


elif size == "M":
    cost = 20
    if add_pepperoni == "Y":
        cost = cost + 3
        print(f"Your Cost is ${cost}")
    elif add_pepperoni == "N":
        print(f"Your Cost is ${cost}")
    else:
        print(f"Your Cost is{cost}")
    if extra_cheese == "Y":
        cost = cost + 2
        print(f"Your Cost is ${cost}")
    elif extra_cheese == "N":
        print(f"Your Cost is ${cost}")
    else:
        print(f"Your Cost is{cost}")

elif size == "L":
    cost = 25
    if add_pepperoni == "Y":
        cost = cost + 4
        print(f"Your Cost is ${cost}")
    elif add_pepperoni == "N":
        print(f"Your Cost is ${cost}")
    else:
        print(f"Your Cost is{cost}")
    if extra_cheese == "Y":
        cost = cost + 3
        print(f"Your Cost is ${cost}")
    elif extra_cheese == "N":
        print(f"Your Cost is ${cost}")
    else:
        print(f"Your Cost is{cost}")
else:
    print("Invalid Size! ")