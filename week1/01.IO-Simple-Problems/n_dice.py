from random import randint

n = input("Enter sides: ")
n = int(n)

rolled = randint(1, n)
print("The dice rolled: " + str(rolled))

