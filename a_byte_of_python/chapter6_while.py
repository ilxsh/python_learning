#1/usr/bin/env python3
# -*- coding: utf-8 -*-


number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))
    if guess == number :
        print('Congratulations, you guessed it.')
        running = False #thie causes the while loop to stop
    elif guess > number:
        print('No, it is little higher than that')# Anather block
    else:
        print('No, it is a little lower than that')
else:
    print('The while loop is over.')
    # Do anything else you want to do here
print('Done')
