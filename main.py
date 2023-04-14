import pygame
from settings import *
from editor import Editor

class Main:
    def __init__(self):
        pygame.init()
        self.display_area = pygame.display.set_mode(
            (WIDTH_OF_WINDOW, HEIGHT_OF_WINDOW))
        self.clock = pygame.time.Clock()
        self.editor = Editor()
    
    def run(self):
        delta_time = self.clock.tick()/1000j
        self.editor.run(delta_time)
        pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.run()