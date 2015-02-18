n = input("Enter n: ")
n = int(n)

divisors = []

count = 1
sum = 0
while count < n:
        if n % count == 0:
                sum += count
        count += 1

print(sum)
