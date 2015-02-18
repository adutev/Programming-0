from random import randint

n = input("Enter sides: ")
n = int(n)

sum = 0

rolled = randint(1, n)
print("First roll: " + str(rolled))
sum += rolled

rolled = randint(1, n)
print("Second roll: " + str(rolled))
sum += rolled

rolled = randint(1, n)
print("Third roll: " + str(rolled))
sum += rolled

print("Sum is: " + str(sum))

