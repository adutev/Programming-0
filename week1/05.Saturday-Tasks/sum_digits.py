n = input("Enter number n: ")
n = int(n)

sum = 0
while n // 10 != 0:
    sum += (n % 10)
    n = n // 10
sum += n
print (sum)
