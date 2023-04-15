import pygame
from pygame.image import load
from settings import *
from editor import Editor

class Main:
    def __init__(self):
        pygame.init()
        self.display_area = pygame.display.set_mode(
            (WIDTH_OF_WINDOW, HEIGHT_OF_WINDOW))
        self.clock = pygame.time.Clock()
        self.editor = Editor()

        # cursor 
        # load is added as alias of pygame.image.load
        surface_cursor = load("./sprites/png/cursor/mouse.png").convert_alpha()
        
        cursor = pygame.cursors.Cursor((0,0),surface_cursor)
        pygame.mouse.set_cursor(cursor)


    def run(self):
        while True: 
            delta_time = self.clock.tick()/1000
            self.editor.run(delta_time)
            pygame.display.update()

if __name__ == "__main__":
    main = Main()
    main.run()