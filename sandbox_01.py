"""
Test file. Acts like a sandbox. Get ideas out of the head and in to a file.
"""
import random

polarity_check = True
while polarity_check:
    lsl = int(input('What is the lower number you want to use in your range?' + '\n'))
    usl = int(input('What is the upper number you want to use in your range?' + '\n'))
    if usl <= lsl:
        print('The RHS of the equation must be bigger than the LHS')
        print('Please re enter the values using that convention.')
    rand_num = random.randint(lsl, usl)
    overall_range = usl - lsl
    print(rand_num, overall_range)