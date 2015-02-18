n = input("Enter n: ")

if int(n) == int(n[::-1]):
    print("The number is palindrom.")
else:
    print("The number is not palindrom.")
