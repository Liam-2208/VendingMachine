import random  
import time

def guess() :
    num = input('Please enter your guess')
    return num

print('Welcome to the number guessing game')
print()
print('The objective is to guess the number im thinking of.')
print()
print('I will give you clues after your first guess')
print()
time.sleep(5)

secretnumber = random.randint(1,100)
print('I have thought of a number from 1-100')
numGuessed = int(input('What is the number you guess?'))

if numGuessed < secretnumber:
    print('Guess is too low, guess higher!')
elif numGuessed == secretnumber:
    print('Wow! You got it exactly right!!!')
else:
    print('Guess is to high, please guess lower')