def board_to_string(board):
	result = ""
	for row in board:
		row = " | ".join(row)
		result += "| " + row + ' |\n'

	return result

board = [["X", "O", "#"],["X", "X", "X"],["#", "#", "#"]]

result = board_to_string(board)

print(result)