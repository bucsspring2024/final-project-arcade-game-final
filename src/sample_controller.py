import pygame
import random
import time
import shelve

class Controller:
    def __init__(self):
        # Setup pygame data
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

    def mainloop(self):
        # Select state loop
        while True:
            self.menuloop()

    def menuloop(self):
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Update data

        # Redraw

    def gameloop(self):
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Update data

        # Redraw

    def gameoverloop(self):
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Update data

        # Redraw

# Uncomment below line to test the controller
# Controller().mainloop()