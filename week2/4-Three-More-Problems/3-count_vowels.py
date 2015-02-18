n = input("Enter a string to compare: ")

count_vowels = 0

vowels = "aeiouyAEIOUY"

for v in vowels:
        count_vowels += n.count(v)
print(count_vowels)
