def linear_search(list, target):
    '''Returns the position of the target value'''
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print(f'Target value at index {index}')
    else:
        print('Target value not found')


number = [1,2,3,4,5,6,7,8,9,10,11,14,23,16,34]
result = linear_search(number, 100)
verify(result)
