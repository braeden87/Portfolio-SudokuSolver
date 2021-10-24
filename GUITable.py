import pygame
from GUICell import Cell
import constants as const
pygame.font.init()


class Table:
    ###############################################################################
    #Creates a Table Object
    ###############################################################################
    def __init__(self, rows, columns, width, height, screen):
        self.rows = rows
        self.columns = columns
        self.cells = [[Cell(const.BOARD_INTERMEDIATE[i][j], i, j, width, height) for j in range(columns)] for i in range(rows)]
        self.width = width
        self.height = height
        self.focused = None
        self.table = None
        self.update_table()
        self.screen = screen

    ###############################################################################
    #This mehtod is used to add the lines and cells to the screen 
    #Therefore, creating the visualization of the table
    ###############################################################################
    def create_table(self):
        #Draw Lines
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 5
            else: thick = 1
            #Horizontal
            pygame.draw.line(self.screen, const.TEXT_COLOR, (0, i * const.CELL_HEIGHT), (self.width, i * const.CELL_HEIGHT), thick)
            #Vertical
            pygame.draw.line(self.screen, const.TEXT_COLOR, (i * const.CELL_WIDTH, 0), (i * const.CELL_WIDTH, self.width), thick)
        #Insert Number into Cells
        for i in range(self.rows):
            for j in range(self.columns):
                self.cells[i][j].insert_number(self.screen)
    
    ###############################################################################    
    #This method keeps updates the self.table variable with the current values
    #of the table
    ###############################################################################
    def update_table(self):
        self.table = [[self.cells[i][j].value for j in range(self.columns)] for i in range(self.rows)]
    
    ###############################################################################
    #Insert Values Method
    #This method inserts the value into the table, then it checks to see if the 
    #Number is valid and if it is the correct number by solving the new table 
    #With the number included. If this works then the value is kept, if not then
    #it is set back to 0
    ###############################################################################
    def insert_values(self, value):
        row, column = self.focused
        if self.cells[row][column].value == 0:
            self.cells[row][column].set_value(value)
            self.update_table()
            if Table.valid_number(self.table, value, [row, column]) and self.solve_puzzle():
                return True
            else:
                self.cells[row][column].set_value(0)
                self.cells[row][column].set_temp_val(0)
                self.update_table()
                return False

    ###############################################################################
    #Insert Temporary Value into the focused cell
    ###############################################################################
    def insert_temp_value(self, value):
        row, column = self.focused
        self.cells[row][column].set_temp_val(value)
    
    ###############################################################################
    #Focus Method
    #This method sets the focus value to the cell location of whatever cell the 
    #user is currently in / focused on
    ###############################################################################
    def focus(self, row, column):
        #Reset All Values
        for i in range(self.rows):
            for j in range(self.columns):
                self.cells[i][j].focused = False
        #Set Focus to Correct Cell
        print(2, row, column)
        self.cells[row][column].focused = True
        self.focused = [row, column]
    ###############################################################################
    #Clear Temporary Value method
    #this sets the temporary value in question back to 0
    ###############################################################################
    def clear_temp_val(self):
        row, column = self.focused
        if self.cells[row][column].value == 0:
            self.cells[row][column].set_temp_val(0)

    ###############################################################################
    #Click Method
    #This method takes the coordinates returned by the mouse  click event and 
    #returns what cell the click took place in.
    ###############################################################################
    def click(self, position):
        if position[0] < self.width and position[1] < self.height:
            x = position[0] // const.CELL_WIDTH
            y = position[1] // const.CELL_HEIGHT
            print(int(x), int(y))
            return [int(y), int(x)]#This may seem weird to return y then x, but 
                                   #Because of the ways the table is set up it is 
                                   #Neccessary
        else: return None

    ###############################################################################
    #Update Window Method
    #This runs every time an event occurs and it re-creates the window
    #to make sure it is up to date and displaying the correct information
    ###############################################################################
    def update_window(screen, table, time, strikes):
        screen.fill(const.BACKGROUND_COLOR)
        #Update time
        text = const.FONT.render("Time: "+ Table.format_time(time), True, const.TEXT_COLOR)
        screen.blit(text, (const.BOARD_WIDTH - 240, const.BOARD_HEIGHT))
        #Update Strikes
        text = const.FONT.render("X" * strikes, True, const.INCORRECT_COLOR)
        screen.blit(text, (20, const.BOARD_HEIGHT))
        #Re-Draw the grid-lines and the cell information
        table.create_table()  
    
    ###############################################################################
    #Format Time Method
    #Sets the way the time value will be displayed to the user
    ###############################################################################
    def format_time(secs):
        sec = secs % 60
        minute = secs // 60
        time_val = " " + str(minute) + ":" + str(sec)
        return time_val

    ###############################################################################
    #Solved Method
    #Checks if the Puzzle is done
    ###############################################################################
    def solved(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.cells[i][j].value == 0: return False
        return True
    
    ###############################################################################
    #Solve Puzzle Method
    #This method is utilized by the insert value method. It solves the sudoku 
    #Puzzle and returns true if it is possible to solve and false if it is not.
    #(Update Table is not called so the answer to this puzzle is not saved here)
    ###############################################################################
    def solve_puzzle(self):
        empty = Table.empty_cell(self.table)
        if not empty: return True
        else:
            row, column = empty
            for i in range(1, 10):
                if Table.valid_number(self.table, i, [row, column]):
                    self.table[row][column] = i
                    if self.solve_puzzle(): return True
                    self.table[row][column] = 0
            return False
    ###############################################################################
    #Show Puzzle Being Solved
    ###############################################################################
    def solve_puzzle_GUI(self):
        self.update_table()
        empty = Table.empty_cell(self.table)
        if not empty: return True
        else:
            row, column = empty
            for i in range(1, 10):
                if Table.valid_number(self.table, i, [row, column]):
                    self.cells[row][column].set_value(i)
                    self.cells[row][column].try_number(self.screen, True)
                    self.update_table()
                    pygame.display.update()
                    pygame.time.delay(100)

                    if self.solve_puzzle_GUI(): return True
                    else:
                        self.cells[row][column].set_value(0)
                        self.update_table()
                        self.cells[row][column].try_number(self.screen, False)
                        pygame.display.update()
                        pygame.time.delay(100)
            return False
    ###############################################################################
    #Valid Number Method
    #Checks to see if the number entered is a valid number for that location
    #It checks to see if the number can be found in the row, column, or square
    ###############################################################################
    def valid_number(table, number, position):
        for i in range(len(table)):
	    #Check the Row
            if table[i][position[1]] == number and position[0] != i:
                return False
        #Check The Column
            if table[position[0]][i] == number and position[1] != i:
                return False
        #Check the Square
        square_x = position[0] // 3
        square_y = position[1] // 3
        for i in range(square_x*3, square_x*3 + 3):
            for j in range(square_y*3, square_y*3 + 3):
                if table[i][j] == number and position != [i, j]:
                    return False

        return True  
    ###############################################################################         
    #Empty Cell Finder 
    #Returns the next empty cell or returns None if there are none
    ###############################################################################
    def empty_cell(table):
        for i in range(const.ROWS):
            for j in range(const.COLUMNS):
                if table[i][j] == 0:
                    return [i, j]
        return None
