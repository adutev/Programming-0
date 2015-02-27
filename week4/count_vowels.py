def count_vowels_consonants(word):
    vowels = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    result = {}
    v = 0
    c = 0
    
    for i in word:
        if i in vowels:
            v += 1
        elif i in consonants:
            c += 1
    result['vowels'] = v
    result['consonants'] = c
    
    return result

print(count_vowels_consonants("aaaAcccD"))
