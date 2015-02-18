a = input("Enter a: ")
a = int(a)

b = input("Enter b: ")
b = int(b)

if a > b:
    temp = a
    a = b
    b = temp

while a <= b:
    if a % 2 ==0:
        print(str(a) + " - even")
    else:
        print(str(a) + " - odd")
    a += 1
