def count_zero_pairs(numbers):
    result = 0
    pairs = {}
    
    for i in numbers:
        for j in numbers:
            if i + j == 0:
                result += 1
                numbers.remove(j)
    return result

numbers = [0, 2, -2, 5, 10]

print(count_zero_pairs(numbers))
