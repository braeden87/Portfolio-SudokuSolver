import pygame
#Initialize
pygame.font.init()

###############################################################################
#This class is going to hold all of the constant values that will be utilized 
#inside of this project
###############################################################################

#All 
FONT = pygame.font.SysFont('arial', 45)
BACKGROUND_COLOR = (25, 25, 25)
TEXT_COLOR = (255, 255, 255)
SECONDARY_TEXT_COLOR = (128, 128, 128)
CORRECT_COLOR = (0, 255, 0)
INCORRECT_COLOR = (255, 0, 0)
FOCUS_COLOR = (0, 0, 255)


#Table
BOARD_HARD = [
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
BOARD_INTERMEDIATE = [
[0,4,0,0,0,2,0,1,9],
[0,0,0,3,5,1,0,8,6],
[3,1,0,0,9,4,7,0,0],
[0,9,4,0,0,0,0,0,7],
[0,0,0,0,0,0,0,0,0],
[2,0,0,0,0,0,8,9,0],
[0,0,9,5,2,0,0,4,1],
[4,2,0,1,6,9,0,0,0],
[1,6,0,8,0,0,0,7,0]
]
BOARD_EASY = [
[0,0,0,0,8,0,2,7,0],
[0,0,0,6,0,3,9,0,5],
[0,4,0,0,0,0,0,3,0],
[0,0,2,0,7,0,5,0,0],
[1,0,0,0,0,9,3,6,0],
[3,7,4,5,0,1,8,0,9],
[2,1,8,7,0,0,6,9,3],
[0,0,6,0,3,0,0,5,0],
[7,5,0,0,0,0,4,8,2]
]



#Main Class
SCREEN_WIDTH = 540
SCREEN_HEIGHT = 600
BOARD_WIDTH = 540
BOARD_HEIGHT = 540
ROWS = 9
COLUMNS = 9


#Cell Class
CELL_WIDTH = BOARD_WIDTH / 9
CELL_HEIGHT = BOARD_HEIGHT / 9
