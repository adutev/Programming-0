n = input("Enter number: ")
n = int(n)

i = 1
sum = 0
while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
print ("The sum of the even numbers between 1 and %s is: %s " % (n, sum))
