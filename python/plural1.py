import re


def plural(noun):
    if re.search('[sxz]', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeioudgkprt]h', noun):
        return re.sub('$', 'es', noun)
    #can use something like this: re.sub('[^aeiou]y', r'\1ies', noun)
    elif re.search('[^aeiou]y', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'

if __name__ == '__main__':
    while True:
        word = input('Please enter a noun:')
        if word == 'quit':
            break
        print('the plural of {0} is {1}'.format(word, plural(word)))
    else:       #here else is useless, after using break
        print('You stoped the application.')
