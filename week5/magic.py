def sum_row(matrix, index):
	sum = 0
	for col in matrix[index]:
		sum += col
	return sum

def sum_col(matrix, index):
	sum = 0
	for row in matrix:
		sum += row[index]
	return sum

def sum_first_diagonal(matrix):
	sum = 0

	for i in range(0, len(matrix)):
		sum += matrix[i][i]

	return sum

def sum_second_diagonal(matrix):
	sum = 0

	for i in reversed(range(0, len(matrix))):
		sum += matrix[i][i]

	return sum

def magic_square(matrix):
	sum = sum_first_diagonal(matrix)

	if sum_second_diagonal(matrix) != sum:
		return False

	for i in range(0, len(matrix)):
		if sum != sum_col(matrix, i):
			return False

	for i in range(0, len(matrix)):
		if sum != sum_row(matrix, i):
			return False

	return True

matrix = [
			[23, 28, 21],
			[22, 24, 26],
			[27, 20, 25]
		]

print(magic_square(matrix))

matrix = [
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]
		]

print(magic_square(matrix))