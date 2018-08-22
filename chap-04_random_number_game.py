""" 
Small application where the computer picks a random number between 1 and 50 without revealing what the number is.
The user has a guess at what the number could be.
The computer only responds with three answers:
1. Too high
2. Too low
3. Correct
"""


import random

"""
The block of code below is simply output to the display to instruct the user...

on what is going to happen and what is needed from the user.

There are no arguments passed here it is all simply text.
"""
print('Hi there. This is a little program to pass some time in an "amusing" way (you can be the judge of that!)')
print('\n')
print('The aim of the game is this:')
print('The computer will "guess" a random number between 1 - 100')
print('Your job, should you wish to accept it Mr. Phelps, is to guess that number in the fewest number of guesses!')
print('.....don\'t worry though, the computer will give you clues as to the direction you need to be going to figure it out')
print('Enjoy :)')




def play_again_wrapper():
    """
    This function acts as a 'wrapper' around the main game function.

    It allows the main game function (random_game()) to be interogated....
    
    for user wishing to continue to play or to quit at any point
    """
    def random_game():
        """
        This function is the backbone of the application.

        It requires NO arguments but provides the user with interaction...

        calculation of their input versus the 'secret' number and ultimately....

        displaying the results to the user.
        """
        count = 0
        print('OK, welcome. Let\'s get started')
        lsl = int(input('What is the lower number you want to use in your range?' + '\n'))
        usl = int(input('What is the upper number you want to use in your range?' + '\n'))
        
        n = random.randint(lsl, usl)

        while True:
            ans = int(input('Enter your guess: '))
            count = count + 1
            if ans == 0:
                print('OK. So long. See you soon for another game.')
                break
            if ans == n:
                print('Success! You win!')
                print(f'That was pretty good. It only took you {count} estimates. Well done!')
                play_again = input('Do you want to play again? (y)es/(n)o')
                if play_again == 'y':
                    random_game()
                else:
                    break
            elif ans > n:
                print('Too high!')
            else:
                print('Too low')
    random_game()

play_again_wrapper()



        
    
