n = input("Enter number n: ")
m = input("Enter number m: ")

n = int(n)
m = int(m)

last_digit_n = n % 10
last_digit_m = m % 10

last_digit_n = int(last_digit_n)
last_digit_m = int(last_digit_m)

if last_digit_n > last_digit_m:
    print (n)
elif last_digit_m > last_digit_n:
    print (m)
else:
    if n > m:
        print (n)
    else:
        print (m)
