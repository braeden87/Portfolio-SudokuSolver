class Sudoku:
	board_1 = [
		[0,0,0,0,2,8,0,7,0],
		[0,0,0,3,0,0,0,0,8],
		[0,0,8,0,0,1,0,0,4],
		[0,4,0,0,0,0,7,0,6],
		[0,8,0,7,5,6,0,4,0],
		[5,0,7,0,0,0,0,1,0],
		[9,0,0,8,0,0,6,0,0],
		[8,0,0,0,0,9,0,0,0],
		[0,2,0,5,4,0,0,0,0]
	]
	def __init__(self, board = board_1):
		self.board = board
		self.solved = False
	def __enter__(self):
		print('Enter:')
		return self
	def __exit__(self, exc_type, exc_value, exc_traceback):
		print('Exit:')
######################################################################
# Solve Board Method
#
# This method will solve for all of the empty spaces in the puzzle.
# it does this using the backtracking algorithm
######################################################################  
	def solve_board(self):
		empty = self.empty_cell()
		if not empty: return True
		else:
			row, column = empty
			for i in range(1, 10):
				if self.valid_number(i, [row, column]):
					self.board[row][column] = i
					if self.solve_board(): return True

					self.board[row][column] = 0

######################################################################
# Valid Number Method
#
# This method  checks to see whether a number entered into a certain 
# cell of the puzzle would work with the rules of sudoku. It checks 
# the row, column, and square to see if that number is already there
######################################################################  
	def valid_number(self, number, position):
		square_x = position[0] // 3
		square_y = position[1] // 3

		for i in range(len(self.board)):
	#Check the Row
			if self.board[i][position[1]] == number and position[0] != i:
				return False
	#Check The Column
			if self.board[position[0]][i] == number and position[1] != i:
				return False
	#Check the Square
		for i in range(square_x*3, square_x*3 + 3):
			for j in range(square_y*3, square_y*3 + 3):
				if self.board[i][j] == number and position != [i, j]:
					return False
		return True

######################################################################
# Print Board Method
#
# This method prints whatever valuse are currently inside of the board
# it can be used to print the original or completed board
######################################################################  
	def print_board(self):
		for i in range(len(self.board)):
			if i % 3 == 0 and i != 0:
				print('--- --- ---')
			for j in range(len(self.board[i])):
				print(self.board[i][j], end = '')
				if (j+1) % 3 == 0 and j != 0 and (j+1)!=9:
					print('|', end = '')
				if j == 8:
					print('')
	def empty_cell(self):
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				if self.board[i][j] == 0:
					return [i, j]
		return False