words = ["words", "are", "meaningful", "words", "words", "are"]

def count_words(words):
    result = {}

    for word in words:
        count = 0
        for i in words:
            if word == i:
                count += 1
        result[word] = count
        count = 0
    return result

print(count_words(words))
