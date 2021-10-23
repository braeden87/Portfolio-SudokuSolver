from Sudoku import Sudoku
import constants as const

with Sudoku() as game:
	game.print_board()
	game.solve_board()
	print('- - - - - - - - - - - - - -')
	game.print_board()