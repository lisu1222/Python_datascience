"""
Guess a number
Computer gives a random number from 1~100
Computer provides feedback on the guessed number until guessed correctly:
'bigger', 'smaller', 'correct'
"""

import random

answer = random.randint(1,100)
counter = 0
while True:
    counter += 1
    number = int(input('Please insert your guess: '))
    if number < answer:
        print('Make it bigger!')
    elif number > answer:
        print('Make it smaller!')
    else:
        print('Correct!')
        break
print("You've guessed %d times!" % counter)
if counter > 7:
      print('You are so persistent!')
