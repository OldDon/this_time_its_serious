""" 
Small application where the computer picks a random number between 1 and 50 without revealing what the number is.
The user has a guess at what the number could be.
The computer only responds with three answers:
1. Too high
2. Too low
3. Correct
"""


import random

print('Hi there. This is a little program to pass some time in an "amusing" way (you can be the judge of that!)')
print('\n')
print('The aim of the game is this:')
print('The computer will "guess" a random number between 1 - 100')
print('Your job, should you wish to accept it Mr. Phelps, is to guess that number in the fewest number of guesses!')
print('.....don\'t worry though, the computer will give you clues as to the direction you need to be going to figure it out')
print('Enjoy :)')


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




        
    
