def member(x, xs):
	if x in xs:
		return True
	else:
		return False

print member(1, [1, 2, 3])
print member("Python", ["Django", "Rails"])