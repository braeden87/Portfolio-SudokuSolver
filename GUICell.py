import pygame
import constants as const

#Initialize
pygame.font.init()


class Cell:
    ###############################################################################
    #Creates a Cell object that is used inside the table 
    ###############################################################################
    def __init__(self, value, row, column, width, height):
        self.value = value
        self.row = row
        self.column = column
        self.width = width
        self.height = height
        self.focused = False
        self.temp_val = 0

    ###############################################################################
    #Inserting a number into the Cell
    ###############################################################################
    def insert_number(self, screen):
        #Initializing All Variables that will be used
        x = self.column * const.CELL_WIDTH
        y = self.row * const.CELL_HEIGHT
        value = None
        color = const.BACKGROUND_COLOR

        #Decides whether the value is Temporary or Permenant
        if self.temp_val !=0 and self.value == 0:
            color = const.SECONDARY_TEXT_COLOR
            value = (str(self.temp_val))
        elif self.value != 0:
            color = const.TEXT_COLOR
            value = (str(self.value))
        text = const.FONT.render(value, True, color)
        screen.blit(text, (x + (const.CELL_WIDTH / 2 - text.get_width() / 2), y + (const.CELL_HEIGHT / 2 - text.get_height() / 2)))

        if self.focused:
            pygame.draw.rect(screen, const.FOCUS_COLOR, (x, y, const.CELL_WIDTH, const.CELL_WIDTH), 3)
    
    ###############################################################################
    #This Method is utilized by the Solve_puzzle_GUI method in the GUITable class 
    #to display the number that is currently being tried for every cell. 
    ###############################################################################
    def try_number(self, screen, color=True):
        x = self.column * const.CELL_WIDTH
        y = self.row * const.CELL_WIDTH
        #Creates a new rectangle to go over the previous one (this way answers don't stack)
        pygame.draw.rect(screen, const.BACKGROUND_COLOR, (x, y, const.CELL_WIDTH, const.CELL_HEIGHT), 0)

        text = const.FONT.render(str(self.value), True, const.TEXT_COLOR)
        screen.blit(text, (x + (const.CELL_WIDTH / 2 - text.get_width() / 2), y + (const.CELL_HEIGHT / 2 - text.get_height() / 2)))
        if color:
            pygame.draw.rect(screen, const.CORRECT_COLOR, (x, y, const.CELL_WIDTH, const.CELL_HEIGHT), 3)
        else:
            pygame.draw.rect(screen, const.INCORRECT_COLOR, (x, y, const.CELL_WIDTH, const.CELL_HEIGHT), 3)
    ###############################################################################
    #Setters
    ###############################################################################
    def set_value(self, value):
        self.value = value
    def set_temp_val(self, temp_val):
        self.temp_val = temp_val
        
