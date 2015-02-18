n = input("Enter n: ")
n = int(n)

divisors = []

count = 1
while count < n:
        if n % count == 0:
                divisors = divisors + [count]
        count += 1
print(divisors)
