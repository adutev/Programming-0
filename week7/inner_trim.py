def inner_trim(string):
	result = ""
	inline = False
	if string[0] != " ":
		inline = True

	for ch in range(0, len(string) - 1):
		if inline:
			if string[ch] != " ":
				result += string[ch]
			elif string[ch] == " " and string[ch + 1] != " ":
				result += string[ch]
		else:
			if string[ch] != " ":
				result += string[ch]
				inline = True
	if string[len(string) - 1] != " ":
		result += string[len(string) - 1]
	return result

print(inner_trim("Python    Django"))
print(inner_trim("  Python     Django   "))
