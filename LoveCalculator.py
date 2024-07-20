print("Love Calculator Is Calculating Your Score....")
name1 = input("Enter Your Name: ")
name2 = input("Enter Your Love Name: ")
combine_names = name1 + name2
lower_names = combine_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))  # Convert score to an integer

if score < 10 or score > 90:
    print(f"Your Score Is {score}. You go together like mentos and coke")
elif 40 <= score <= 50:
    print(f"Your Score Is {score}. You are good to go together")
else:
    print(f"Your Score Is {score}")
