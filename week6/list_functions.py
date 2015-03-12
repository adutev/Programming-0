def head(list):
	return list[0]

def last(list):
	return list[len(list) - 1]

def tail(list):
	del list[0]

	return list

print(tail(["Python"]))
print(tail([1, 2, 3]))

def equal_lists(list1, list2):
	if len(list1) != len(list2):
		return False

	else:
		for i in range(0, len(list1)):
			if list1[i] != list2[i]:
				return False

	return True

print(equal_lists([1, 2], [1, 2]))
print(equal_lists([2, 1], [1, 2]))
print(equal_lists([], []))

def count_item(item, list):
	count = 0
	for i in list:
		if i == item:
			count += 1
	return count

print(count_item(5, [1, 2, 3, 4, 5]))
print(count_item("winter", ["winter", "winter"]))
print(count_item(False, [True, True]))

def take(number, list):
	result = []
	for i in range(0, number):
		if i < len(list):
			result.append(list[i])

	return result

print(take(2, [1, 2, 3, 4, 5]))
print(take(3, [3, 4, 5, 6, 7, 8]))
print(take(10, [1]))

def drop(n, list):
	result = list
	for i in range(0, n):
		if i < len(list):
			del result[i]

	return result

print(drop(1, [1, 2, 3]))
print(drop(2, ["Python", "Ruby", "Django", "Rails"]))
print(drop(10, [1]))

def reverse(list):
	result = []
	for i in reversed(list):
		result.append(i)
	return result

print(reverse(["Speak", "in", "reverse", "you", "must!"]))
print(reverse([1, 2, 3]))
print(reverse([]))