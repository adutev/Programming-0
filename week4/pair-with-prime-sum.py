def prime_pais(numbers):
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            sum = numbers[i] + numbers[j]
            if is_prime(sum):
                return True
                break
    return False

def is_prime(n):
    if n <= 1:
        return False

    is_prime = True

    start = 2

    while start < n:
        if n % start == 0:
            is_prime = False
            break
        
        start += 1
    
    return is_prime

numbers = [2, 1, 4, 3]

print(prime_pais(numbers))
