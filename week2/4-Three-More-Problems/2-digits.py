n = input("Enter n: ")
n = int(n)
digits = []
string_of_digits = ""

while n != 0:
    digits += [n % 10]
    n = n // 10
digits.reverse()

print("List of digits is: " + str(digits))

digits_string = ""
for i in digits:
        digits_string += str(i)
print("Number is: " + digits_string)
