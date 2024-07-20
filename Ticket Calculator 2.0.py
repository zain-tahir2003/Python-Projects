height = int(input("Enter your height: "))
if height < 120:
    print("You cannot ride the roller coaster!")
else:
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print(f"Your Total Bill Is: ${bill}")
    elif 12 <= age < 18:
        bill = 7
        print(f"Your Total Bill Is: ${bill}")
    elif age >= 18:
        bill = 12
        print(f"Your Total Bill Is: ${bill}")
    want_photo = input("Do you want photo(Y/N)? ")
    if want_photo == "Y" or want_photo == "y":
        bill = bill + 3
        print(f"Your Total Bill Is: ${bill}")
    else:
        print(f"Your Total Bill Is: ${bill}")