def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

theInput = int(input('Enter a number to compute the factorial: '))
print(f'The factorial is: {factorial(theInput)}')