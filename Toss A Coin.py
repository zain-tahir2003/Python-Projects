import random
import time

print("Tossing...")

time.sleep(3)

random_side = random.randint(0, 1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")
