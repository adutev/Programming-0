n = input("Enter n: ")
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
        print("Да")
else:
    print("Не")
