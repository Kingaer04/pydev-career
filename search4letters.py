def search4words(words:str, vowel:str=set('aeiou')) ->str:
    found = vowel.intersection(set(words))
    return found


#print(str(search4words("am king", set("ia"))))