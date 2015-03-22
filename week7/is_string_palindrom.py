import re

def is_string_palindrom(string):
	string = string.lower()
	string = re.sub(r'[^\w]','', string)

	if string == string[::-1]:
		return True
	else:
		return False

print(is_string_palindrom("Az obi4am ma4 i boza"))
print(is_string_palindrom("A Toyota!"))
print(is_string_palindrom("bozaaa"))
print(is_string_palindrom(" kapak! "))