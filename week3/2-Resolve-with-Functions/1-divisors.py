def divisors(n):
    divisors = []
    count = 1

    while count < n:
            if n % count == 0:
                divisors.append(count)
            count += 1
    return divisors

n = input("Enter n: ")
n = int(n)

print(divisors(n))
