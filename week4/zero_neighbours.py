def count_zero_neighbours(numbers):
    result = 0
    for i in range(0, len(numbers) - 1):
        if numbers[i] + numbers[i + 1] == 0:
            result += 1
    return result

numbers = [1, 2, -2, 0, 0, 5, -5]

print(count_zero_neighbours(numbers))
