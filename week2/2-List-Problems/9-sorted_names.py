n = input("Enter n: ")
n = int(n)

count = 1
names = []
while count <= n:
    name = input("Enter name: ")
    names = names + [name]
    count += 1

print("Sorted names are:")
for name in sorted(names):
        print(name)

