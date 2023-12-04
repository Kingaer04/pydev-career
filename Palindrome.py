def palindrome_string(word):
    l = []
    words = list(word)
    for i in words:
        if i == i[::-1]:
            l.append(i)
    return max(l)

name = ['Dan', 'Alex', 'Mic', 'mam', 'rotor', 'xyxyxyxyx ']
print(palindrome_string(name))
