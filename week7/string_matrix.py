def string_matrix(matrix_width, strings):

	result = ""
	index = 0
	for row in range(0, matrix_width):
		new_row = []
		if len(strings[row]) >= matrix_width:
			for col in range(0, matrix_width):
				new_row.append(strings[row][col])
		else:
			for col in range(0, len(strings[row])):
				new_row.append(strings[row][col])
			for col in range(len(strings[row]), matrix_width):
				new_row.append('X')
		result += "| " + " | ". join(new_row) + " |\n"
	return result

result = string_matrix(6,["python","gogo","perl","java","haskell","ruby0nRails"])
print(result)