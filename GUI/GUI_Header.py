import pygame
import constants as const

class header_box:
######################################################################
# Constructor
######################################################################
    def __init__(self, x, y, width, height, text):
        self.header = pygame.Rect(x, y, width, height)
        self.text = text    
        self.color = const.SECONDARY_TEXT_COLOR
        self.text_surface = const.FONT.render(text, True, const.BACKGROUND_COLOR)
######################################################################
# Draw Method
#
# This method is used to add the Header to the Screen / Window 
######################################################################
    def draw(self, screen):
       #Text 
        screen.blit(self.text_surface, (self.header.x + 5, self.header.y + 5))
        pygame.draw.rect(screen, self.color, self.header, 2)
