n = input("Enter number n: ")
n = int(n)

while n // 10 != 0:
    print(n % 10)
    n = n // 10
print(n)
