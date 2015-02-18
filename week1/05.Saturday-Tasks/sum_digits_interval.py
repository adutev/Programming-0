N = input("Enter number N: ")
N = int(N)
M = input("Enter number M: ")
M = int(M)
n = N
while N <= M:
    sum = 0
    while n // 10 != 0:
        sum += (n % 10)
        n = n // 10        
    sum += n
    print ("Sum of digits of %s = %s " % (N, sum))
    N = N + 1
    n = N
    
