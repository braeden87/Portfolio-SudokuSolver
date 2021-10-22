import Sudoku
import constants as const

with Sudoku(const.BOARD_1) as game:
	game.print_board()