logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
# The alphabet is repeated to handle shifting beyond 'z' easily
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""  # Initialize an empty string to store the final result
    if cipher_direction == "decode":
        shift_amount *= -1  # Reverse the shift for decoding

    # Process each character in the input text
    for char in start_text:
        if char in alphabet:
            # Find the position of the character in the alphabet
            position = alphabet.index(char)
            # Calculate the new position with the shift amount
            new_position = position + shift_amount
            # Append the shifted character to the result
            end_text += alphabet[new_position]
        else:
            # If the character is not in the alphabet (e.g., space or punctuation), add it unchanged
            end_text += char

    # Print the final encoded or decoded result
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Flag to control the while loop
should_end = False
while not should_end:
    # Get user input for direction, message, and shift amount
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Ensure the shift amount is within the range of the alphabet length
    shift = shift % 26

    # Call the caesar function with the user inputs
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Ask the user if they want to restart the program
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True  # Set the flag to True to exit the loop
        print("Goodbye")  # Print a goodbye message
