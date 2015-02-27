def calculate_coins(sum):
    sum = sum * 100
    coins = [100, 50, 20, 10, 5, 2, 1]
    result = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    for c in coins:
        if sum % c == sum:
            print(int(c))
        else:
            result[c] += int(sum // c)
            sum = sum % c
            
    return result

print(calculate_coins(0.53))
print(calculate_coins(9.84))
