def print_sands_clock(n):
	middle = n//2
	result = ""
	for row in range(0, n):
		for col in range(0, n):
			if row == 0 or row == n - 1:
				result += '*'
			elif(col >= row and col < n - row and row <= middle):
				result += '*'
			elif(col >= n - row - 1 and col <= row and row > middle):
				result += '*'
			else:
				result += '.'
		result += '\n'
	return result
n = input("Enter odd number: ")
n = int(n);
if n%2 == 0:
	print("Please enter an odd number!")
else:
	print(print_sands_clock(n))