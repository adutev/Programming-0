n = input("Enter n: ")
n = int(n)

if n == 0:
    print ("0! is 1")
else:
    i = 1
    factorial = 1
    while i < n:
        factorial *= (i + 1)
        i += 1
    print (factorial)
        
