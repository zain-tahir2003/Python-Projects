height = input("Enter your height(in centimeters)")
if height > 120:
    age = int(input("Enter your age: "))
    if age <= 18:
        print("Cost of your ticket is $7")
    elif age > 18:
        print("Cost of your ticket is $12")
else:
    print("You Cannot Have This Ride! ")
