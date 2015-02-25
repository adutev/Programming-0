def is_perfect(n):
    divisors = []

    count = 1
    sum = 0
    while count < n:
        if n % count == 0:
            sum += count
        count += 1

    if sum == n:
        return str(n) + " is a perfect number"
    else:
        return str(n) + " is not a perfect digit"

n = input("Enter n: ")
n = int(n)

print (is_perfect(n))
