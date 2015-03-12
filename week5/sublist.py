def sublist(list1, list2):
	string1 = ''
	for i in list1:
		string1 += str(i)

	string2 = ''
	for i in list2:
		string2 += str(i)

	if string2 in string1:
		return True
	else:
		return False

list1 = [ 0, 0, 1, 2, 3, 5, 6 ]
list2 = [ 1, 2, 3 ]

print(sublist(list1, list2))

list1 = ["Python", "Django"]
list2 = ["Django", "Python"]

print(sublist(list1, list2))

list1 = [1, 0, 1, 2, 2]
list2 =  [1, 2]

print(sublist(list1, list2))
