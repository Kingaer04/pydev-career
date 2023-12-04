def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i -1
        while j >=0 and key <  list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
        print(list)


number = [2,9,1,-1,6,4,7,0]
print(insertion_sort(number))
