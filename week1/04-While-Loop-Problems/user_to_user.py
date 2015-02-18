a = input("Enter a: ")
a = int(a)

b = input("Enter b: ")
b = int(b)

if a > b:
    temp = a
    a = b
    b = temp

while a <= b:
    print (a)
    a += 1
