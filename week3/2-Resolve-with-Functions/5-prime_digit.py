def prime_digit(n):
    has_prime = False

    for i in n:
        i = int(i)
        for j in range(2, i + 1):
            if i % j == 0:
                if j == i:
                    has_prime = True
                else:
                    has_prime = False
                    break
    if has_prime:
        return "Да"
    else:
        return "Не"

n = input("Enter n: ")

print(prime_digit(n))
