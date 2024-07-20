"""
target = int(input("Enter Numbers Till Which You Want Sum Of Numbers: "))
even_sum = 0

for number in range(2,target+ 1, 2):
    even_sum += number
    
print(even_sum)

"""
target = int(input("Enter Numbers Till Which You Want Sum Of Numbers: "))
total = 0

print(f"Even numbers till {target} are:-")
for number in range(1, target+1):
    
    if number % 2 == 0:
        
        print(number)
        total += number

print(f"Sum Of All Even Numbers Is {total}")
