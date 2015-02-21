def fact(n):
	result = 1
	for i in range (2,n + 1):
		result = result * i
	return result

print fact(5)
print fact(0)
print fact(6)
print fact(2)
print fact(1)

