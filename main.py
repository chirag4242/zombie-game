import pygame
import sys
from settings import *


class Main:
    def __init__(self):
        pygame.init()
        self.display_area = pygame.display.set_mode(
            (WIDTH_OF_WINDOW, HEIGHT_OF_WINDOW))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.run()