import pygame
from settings import *


class Menu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.create_buttons()

    def create_buttons(self):
        # menu area creation
        size = 180
        margin = 6
        topLeft = (WIDTH_OF_WINDOW - size - margin,
                   HEIGHT_OF_WINDOW - size - margin)
        self.rect = pygame.Rect(topLeft, (size, size))

        # button areas
        generic_button_rect = pygame.Rect(
            topLeft, (self.rect.width / 2,  self.rect.height / 2))
        button_margin = 5
        self.tile_button_rect = generic_button_rect.copy(
        ).inflate(-button_margin, -button_margin)
        self.coin_button_rect = generic_button_rect.copy().inflate(-button_margin, -button_margin).move(
            self.rect.width / 2, 0)

    def display(self):
        pygame.draw.rect(self.display_surface, 'red', self.rect)
        pygame.draw.rect(self.display_surface, 'green',
                         self.tile_button_rect)
        pygame.draw.rect(self.display_surface, 'blue', self.coin_button_rect)
