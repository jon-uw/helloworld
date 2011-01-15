# implement fibonacci function using python generator

def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    for n in fib(1000):
        print(n, end=' ')
print('')
#using list will iterate through the generator like for loop:next(generator)
print(list(fib(10000)))     
