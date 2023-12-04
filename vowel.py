# from collections import Counter
    

# vowels = ['a', 'e', 'i', 'o', 'u']
# word = input('Input word: ').lower()
# found = []
# for i in word:
#     if i in vowels:
#         if i not in found:
#             found.append(i)

# print(Counter(found))



# word = input('Input sentence: ').lower()
# found = {'a':0, 'e':0, 'i':0, 'o': 0, 'u':0}
# for letter in word:
#     if letter in found:
#         found[letter] += 1
# print(found)
# for m,n in sorted(found.items()):
#     print(f'{m}:{n}')


vowel = ['a', 'e', 'i', 'o', 'u']
word = input('Input sentence: ').lower()
found = {}
for letter in word:
    if letter in vowel:
        found.setdefault(letter,0)
        found[letter] += 1
print(found)
