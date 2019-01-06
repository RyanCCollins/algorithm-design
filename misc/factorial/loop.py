from functools import reduce

def factorial(n):
    nums = map(lambda x: x + 1, list(range(n)))
    return reduce(lambda x, y: x * y, nums)