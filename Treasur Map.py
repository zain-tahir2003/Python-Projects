line1 = ["⬜️", "⬜️", "⬜️"]
line2 = ["⬜️", "⬜️", "⬜️"]
line3 = ["⬜️", "⬜️", "⬜️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

position = input("Where do you want to put the treasure? (e.g., a1, b2, c3) ")

# Validate input
if len(position) != 2 or position[0].lower() not in "abc" or not position[1].isdigit():
    print("Invalid input. Please enter a position in the format 'a1', 'b2', etc.")
else:
    # Write your code below this row 👇
    letter = position[0].lower()
    abc = ["a", "b", "c"]
    letter_index = abc.index(letter)
    number_index = int(position[1]) - 1

    if number_index < 0 or number_index > 2:
        print("Invalid input. Row number must be 1, 2, or 3.")
    else:
        map[number_index][letter_index] = 'X'

        # Write your code above this row 👆
        print(f"{line1}\n{line2}\n{line3}")
