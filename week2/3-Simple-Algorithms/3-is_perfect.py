n = input("Enter n: ")
n = int(n)

divisors = []

count = 1
sum = 0
while count < n:
        if n % count == 0:
                sum += count
        count += 1

if sum == n:
        print(str(n) + " is a perfect number")
else:
        print(str(n) + " is not a perfect digit")
