n = input("Enter n: ")
n = str(n)
def find_min(n):
	char_array = []
	for i in n:
		char_array.append(i)
	char_array = sorted(char_array)
	result = "Smallest: "
	result += ''.join(char_array)
	
	return  result

def find_max(n):
	char_array = []
	for i in n:
		char_array.append(i)
	char_array = reversed(sorted(char_array))
	result = "Largest: "
	result += ''.join(char_array)

	return  result

print find_max(n)
print find_min(n)
