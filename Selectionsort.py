def selection_sort(list):
    for i in range(len(list)-1):
        minpoint = i
        for j in range(i, len(list)):
            if list[j] < list[minpoint]:
                minpoint = j

        list[i], list[minpoint] = list[minpoint], list[i]

    return list


number = [2,9,1,-1,6,4,7,0]
print(selection_sort(number))
