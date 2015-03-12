def str_reverse(string):
	result = ''
	for ch in reversed(string):
		result += ch

	return result

print("=== Test str_reverse function ===")
print(str_reverse("Anton"))

def join(delimiter, items):
	result = ""
	for item in items:
		result += item + delimiter

	return result
print("=== Test join function ===")
print(join(" ", ["Radoslav", "Yordanov", "Georgiev"]))
print(join("\n", ["line1", "line2"]))

def startswith(search, string):
	for i in range(0, len(search)):
		if search[i] != string[i]:
			return False
		return True

print("=== Test startswith function ===")
print(startswith("Py", "Python"))
print(startswith("py", "Python"))
print(startswith("baba", "asdbaba"))

def endswith(search, string):
	start = len(string) - len(search)
	for i in range(start, len(string)):
		if search[i - start] != string[i]:
			return False
		return True

print("=== Test endswith function ===")
print(endswith(".py", "hello.py"))
print(endswith("kapak", "babakapak"))
print(endswith(" ", "Python   "))
print(endswith("py", "python"))

def trim(string):
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

print("=== Test trim function ===")
print(trim("   asda   "))
print(trim(" spacious    "))
print(trim("no here but yes at end   "))
print(trim("                      "))
print(trim("python"))