def recursive_binary_search(list, target):
    # check if the list is not empty
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint +1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(index):
    if index == True:
        print(f'Target is at index {index}')
    else:
        print('Target not found')


number = [1,2,3,4,201,5,6,7,100,8,9,10,11,14,23,-1,16,34]
num = sorted(number)
result = recursive_binary_search(num, 1000)
verify(result)
