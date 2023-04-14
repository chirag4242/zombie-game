import pygame, sys
from settings import *

class Editor: 
    def __init__(self):
        # setup 
        self.display_surface = pygame.display.get_surface()

    def event_loop(self): 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def run(self,delta_time):
        self.display_surface.fill('white')
        self.event_loop()