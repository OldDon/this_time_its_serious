""" 
Small application where the computer picks a random number between 1 and 50 without revealing what the number is.
The user has a guess at what the number could be.
The computer only responds with three answers:
1. Too high
2. Too low
3. Correct
"""

import random


n = random.randint(1, 100)
while True:
    ans = int(input('Enter your guess: '))
    if ans == n:
        print('Success! You win!')
        break
    elif ans > n:
        print('Too high!')
    else:
        print('Too low')




        
    
