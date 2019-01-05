import math

def binarySearch(aList, value):
    start = 0
    stop = len(aList)
    def getMiddle():
        return math.floor((start + stop) / 2)
    middle = getMiddle()

    while aList[middle] != value and start < stop:
        if value < aList[middle]:
            stop = middle - 1
        else:
            start = middle + 1
        middle = getMiddle()
    return -1 if aList[middle] != value else middle

def binarySearchRecursive(aList, value, count = 0):
    middle = math.floor(len(aList) / 2)
    if value < aList[middle]:
        newList = aList[0:middle]
        return binarySearchRecursive(newList, value, count + 0)
    elif value > aList[middle]:
        newList = aList[middle:]
        nextCount = len(aList) - len(newList)
        return binarySearchRecursive(newList, value, count + nextCount)
    elif aList[middle] == value:
        return middle + count
    else:
        return -1

listInput = input('Enter a list like: 1,2,3: ')
theList = list(map(int, listInput.split(',')))
item = int(input('Enter a value to search for: '))
result = binarySearchRecursive(theList, item)
print(f'The result is {result}')