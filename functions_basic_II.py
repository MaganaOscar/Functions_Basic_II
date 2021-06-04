def countdown(num):
    numList = []
    for x in range(num, -1, -1):
        numList.append(x)
    return numList
print(countdown(5))

def print_and_return(numList):
    print(numList[0])
    return numList[1]
print(print_and_return([1,2]))

def first_plus_length(numList):
    return len(numList) + numList[0]
print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(numList):
    greaterList = []
    if(len(numList) > 1):
        for num in numList:
            if num > numList[1]:
                greaterList.append(num)
        return greaterList
    else:
        return False
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

def length_and_value(size, value):
    sizedList = []
    for x in range(size):
        sizedList.append(value)
    return sizedList
print(length_and_value(4,7))
print(length_and_value(6,2))