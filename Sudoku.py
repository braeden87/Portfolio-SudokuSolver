class Sudoku:
	def __init__(self, board):
		self.board = board
		self.solved = False
	def __enter__(self):
		print('Enter:')
		return self
	def exit_(self, exc_type, exc_value, exc_traceback):
		print('Exit:')
		if self.solved:
			self.quit()
	#def solve_board(self):

	#def valid_number(self, position):

	def print_board(self):
		for i in range(len(self.board)):
			if i % 3 == 0 and i != 0:
				print('--- --- ---')
			for j in range(len(self.board[i])):
				print(self.board[i][j], end = '')
				if j % 3 == 0 and j != 0 and j != 9:
					print('|', end = '')
				if j == 9:
					print()
	def empty_cell(self):
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				if self.board[i][j] == 0:
					return self.board[i][j]
		return None