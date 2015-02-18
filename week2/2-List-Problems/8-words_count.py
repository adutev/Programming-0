word = input("Enter word:")

n = input("Enter n: ")
n = int(n)

count = 1
words = []
while count <= n:
    inserted_word = input("Enter word: ")


    words = words + [inserted_word]

    count += 1
occurence = words.count(word)
print(word + " is found " + str(occurence) + " times.")

