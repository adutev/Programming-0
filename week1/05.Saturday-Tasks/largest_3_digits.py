a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

a = int(a)
b = int(b)
c = int(c)

max_digit = a;
mid_digit = b;
min_digit = c;

if b > a:
    if b > c:
        max_digit = b
        if a > c:
            mid_digit = a
        else:
            mid_digit = c
            min_digit = a
    else:
        max_digit = c
        mid_digit = b
        min_digit = a

elif c >= a:
    max_digit = c
    if a >= b:
        mid_digit = a
        min_digit = b
    
print ("Max digit is: %s " % (max_digit))
print ("Mid digit is: %s " % (mid_digit))
print ("Min digit is: %s " % (min_digit))

min_3_digit_number = str(min_digit) + str(mid_digit) + str(max_digit)
max_3_digit_number = str(max_digit) + str(mid_digit) + str(min_digit)

print("Min 3 digit number is: ",  (min_3_digit_number))
print("Max 3 digit number is: ", (max_3_digit_number))
