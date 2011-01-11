# see how to use if statement

number = 23
guess = int(input('Enter an integer:' ))

if guess == number:
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
elif guess < number:
    print('No, It is a little higher than that')
else:
    print('No, It is a little lower than that')

print('Done')
