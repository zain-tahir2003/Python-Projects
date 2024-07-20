def calculate_bmi():
    while True:
        try:
            # Get user input
            height = input("Enter Your Height (In Meters): ")
            weight = input("Enter Your Weight (In KG): ")

            # Convert input to appropriate types
            height_as_float = float(height)
            weight_as_float = float(weight)

            # Check for negative values
            if height_as_float <= 0 or weight_as_float <= 0:
                raise ValueError("Height and weight must be positive numbers.")

            break

        except ValueError as ve:
            print(f"Invalid input: {ve}. Please enter numeric values greater than zero.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

    # Calculate BMI
    bmi = weight_as_float / (height_as_float ** 2)

    # Print BMI
    print(f"Your BMI is {bmi:.2f}")

    # Determine weight category
    if bmi < 18.5:
        print("You are underweight")
    elif 18.5 <= bmi < 25:
        print("You are normal weight")
    elif 25 <= bmi < 30:
        print("You are overweight")
    else:
        print("You are obese")

# Run the BMI calculator
print("******************************************************** BMI CALCULATOR ********************************************************\n")
calculate_bmi()
print("********************************************************************************************************************************\n")
