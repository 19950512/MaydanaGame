import pygame, sys
import socket  # Adicionando a biblioteca para comunicação via sockets
from settings import *
import time
from level import Level
from debug import debug
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('Maydana Online')
        self.clock = pygame.time.Clock()

        self.level = Level()
    
    def run(self):

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level.run()

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    
    game.run()