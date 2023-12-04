def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while(first <= last):
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print(f'The target is at index {index}')
    else:
        print('Target not found')


number = [1,2,3,4,201,5,6,7,100,8,9,10,11,14,23,-1,16,34]
num = sorted(number)
result = binary_search(number, 100)
verify(result)
