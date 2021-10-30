from GUI.GUITable import Table
import pygame
import time
import constants as const
from GUI.GUI_Submit_Button import submit_button
from GUI.GUI_Header import header_box

class main_GUI:
###############################################################################
#This is where all of the Gui classes will be utilized. I will then call this 
#this class in the main.py file to run the GUI
###############################################################################
    screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
    pygame.display.set_caption('Sudoku Solver')
    level_header = header_box(0, 0, const.SCREEN_WIDTH, const.SCREEN_HEIGHT * (1/7), 'Choose Your Difficulty')
    level1 = submit_button(0, const.SCREEN_HEIGHT * (1/7), const.SCREEN_WIDTH, const.SCREEN_HEIGHT * (2/7), 'Easy Puzzle')
    level2 = submit_button(0, const.SCREEN_HEIGHT * (3/7), const.SCREEN_WIDTH, const.SCREEN_HEIGHT * (2/7), 'Intermediate Puzzle')
    level3 = submit_button(0, const.SCREEN_HEIGHT * (5/7), const.SCREEN_WIDTH, const.SCREEN_HEIGHT * (2/7), 'Hard Puzzle')
    levels = [level1, level2, level3]
    running = True
    key = None
    start = time.time()
    strikes = 0
    level_selected = False
    while running:
        screen.fill(const.TEXT_COLOR)
        if not level_selected:
            level_header.draw(screen)
            for level in levels:
                level.draw(screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for level in levels:
                    level.handle_event(event)
                    if level.active:
                        if level.text == 'Easy Puzzle':
                            puzzle_level = const.BOARD_EASY
                        elif level.text == 'Intermediate Puzzle':
                            puzzle_level = const.BOARD_INTERMEDIATE
                        else:
                            puzzle_level = const.BOARD_HARD
                        table = Table(const.ROWS, const.COLUMNS, const.BOARD_WIDTH, const.BOARD_HEIGHT, puzzle_level, screen)
                        level_selected = True
        else:
            playtime = round(time.time() - start)
            #This iterates through all of the events that occur (one by one)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1: key = 1
                    if event.key == pygame.K_2: key = 2
                    if event.key == pygame.K_3: key = 3
                    if event.key == pygame.K_4: key = 4
                    if event.key == pygame.K_5: key = 5
                    if event.key == pygame.K_6: key = 6
                    if event.key == pygame.K_7: key = 7
                    if event.key == pygame.K_8: key = 8
                    if event.key == pygame.K_9: key = 9
                    if event.key == pygame.K_KP1: key = 1
                    if event.key == pygame.K_KP2: key = 2
                    if event.key == pygame.K_KP3: key = 3
                    if event.key == pygame.K_KP4: key = 4
                    if event.key == pygame.K_KP5: key = 5
                    if event.key == pygame.K_KP6: key = 6
                    if event.key == pygame.K_KP7: key = 7
                    if event.key == pygame.K_KP8: key = 8
                    if event.key == pygame.K_KP9: key = 9
                    if event.key == pygame.K_DELETE:
                        table.clear_temp_val()
                        key = None
                    #If the space bar is hit. Solve the puzzle
                    if event.key == pygame.K_SPACE:
                        print('Space Pressed')
                        table.solve_puzzle_GUI()
                        if table.solved():
                            print("Auto Completion Successful") 
                            print('Solved In: ', playtime)                   
                    if event.key == pygame.K_RETURN:
                        i, j = table.focused
                        if table.cells[i][j].temp_val != 0:
                            if table.insert_values(table.cells[i][j].temp_val):
                                print("Success")
                                strikes = 0
                                if table.solved():
                                    print("You Did It!")
                                    print("Play Time:", playtime)
                            else:
                                print("Wrong")
                                strikes += 1
                            key = None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    clicked = table.click(pos)
                    if clicked:
                        table.focus(clicked[0], clicked[1])
                        key = None

                if table.focused and key != None:
                    table.insert_temp_value(key)
                #This makes usre to update the window after every event to make sure
                #We are displaying the most up to date information
                Table.update_window(screen, table, playtime, strikes)
                pygame.display.update()