def sum_divisors(n):
	divisors = []

	count = 1
	sum = 0
	while count < n:
	        if n % count == 0:
	                sum += count
	        count += 1

	return sum

n = input("Enter n: ")
n = int(n)

print(sum_divisors(n))
