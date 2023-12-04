names = ['Dan', 'Anny', 'Dan', 'Mic', 'Alex', 'Sam', 'Mic']
name = set(names)
last = list(name)
print(last)


vowel = set('aeiou')
word = input('Input sentence: ')
found = vowel.intersection(set(word))
for i in found:
    print(i, end=',')
