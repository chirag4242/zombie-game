import pygame
import sys
from pygame.math import Vector2 as vector
from pygame.mouse import get_pressed as mouse_inputs
from pygame.mouse import get_pos as mouse_position
from settings import *
from menu import Menu


class Editor:
    def __init__(self):
        # setup
        self.display_surface = pygame.display.get_surface()

        # navigation with vector
        self.origin = vector()
        self.pan_active = False
        self.pan_offset = vector()

        # Support line surface
        self.support_line_surface = pygame.Surface(
            (WIDTH_OF_WINDOW, HEIGHT_OF_WINDOW))
        self.support_line_surface.set_colorkey('green')
        self.support_line_surface.set_alpha(30)

        # selection
        self.selection_index = 2

        # menu
        self.menu = Menu()
        self.menu.display()

    # input
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.pan_input(event)

    def selection_hotkeys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.selection_index -= 1
            if event.key == pygame.K_RIGHT:
                self.selection_index += 1
            self.selection_index = max(2, min(self.selection_index, 18))

    def pan_input(self, event):
        # mouse_inputs is alias of pygame.mouse.mouse_inputs
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_inputs()[1]:
            self.pan_active = True
            self.pan_offset = vector(mouse_position()) - self.origin

        if not mouse_inputs()[1]:
            self.pan_active = False

        # if left ctrl is pressed then moving up and down
        # else left and right
        if event.type == pygame.MOUSEWHEEL:
            if pygame.key.get_pressed()[pygame.K_LCTRL]:
                self.origin.y -= event.y * 50
            else:
                self.origin.x -= event.y * 50

        if self.pan_active:
            # mouse_position is alias pygame.mouse.get_pos
            self.origin = vector(mouse_position()) - self.pan_offset

    # drawing tile grid
    def draw_grid_tiles(self):
        # grid
        columns = WIDTH_OF_WINDOW // SIZE_OF_TILE
        rows = HEIGHT_OF_WINDOW // SIZE_OF_TILE

        offset_vector = vector(x=self.origin.x - int(self.origin.x/SIZE_OF_TILE) * SIZE_OF_TILE,
                               y=self.origin.y - int(self.origin.y/SIZE_OF_TILE) * SIZE_OF_TILE)

        self.support_line_surface.fill('green')
        for column in range(columns + 1):
            x = offset_vector.x + column * SIZE_OF_TILE
            pygame.draw.line(self.support_line_surface,
                             LINE_COLOR, (x, 0), (x, HEIGHT_OF_WINDOW))
        for row in range(rows + 1):
            y = offset_vector.y + row * SIZE_OF_TILE
            pygame.draw.line(self.support_line_surface,
                             LINE_COLOR, (0, y), (WIDTH_OF_WINDOW, y))
        self.display_surface.blit(self.support_line_surface, (0, 0))

    # run design application
    def run(self, delta_time):
        self.display_surface.fill('white')
        self.event_loop()
        self.draw_grid_tiles()
        pygame.draw.circle(self.display_surface, 'red', self.origin, 10)
        self.menu.display()
