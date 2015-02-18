a = input("Enter a : ")
a = int(a)

b = input("Enter b : ")
b = int(b)

operation = input("enter operation: ")

result = 0

if operation == "+":
    result = a + b
    print("Result is: " + str(result))
elif operation == "-":
    result = a - b
    print("Result is: " + str(result))
elif operation == "*":
    result = a * b
    print("Result is: " + str(result))
elif operation == "/":
    result = a / b
    print("Result is: " + str(result))
else:
    print("We do not support that operation.")

