# guess number game
# comProg slide 4

import random

print("Guess my number (0 to 99)\nYou have 7 tries")

n = random.randint(0,99)
x = int(input())

for i in range(7):
    if x == n:
        print("You win!")
        break
    elif x < n:
        print("Higher")
    elif x > n:
        print("Lower")
        
    if i == 6:
        print(f'You lose... the number is {n}')
    x = int(input())
