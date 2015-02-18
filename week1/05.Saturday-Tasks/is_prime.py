n = input("Enter n: ")
n = int(n)

i = 3
is_prime = 1

while i < n:
    if n % i == 0:
        is_prime = 0
    i = i + 1
if is_prime:
    print("The number is prime.")
else:
    print("The number is NOT prime.")   
