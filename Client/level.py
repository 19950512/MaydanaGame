import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self, received_map):

        # get the display surface
        self.display_surface = pygame.display.get_surface()


        # sprit group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.received_map = received_map

        # sprite setup
        self.create_map()

    def update_map(self, received_map):
        self.received_map = received_map
        self.create_map()

    def create_map(self):
        self.visible_sprites.empty()  # Limpa os sprites antes de criar novos

        for row_index, row in enumerate(self.received_map):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if col == 'x':
                    Tile(
                        pos=(x, y),
                        groups=[self.visible_sprites, self.obstacle_sprites]
                    )
                
                if col == 'p':
                    self.player = Player(
                        pos=(x, y),
                        groups=[self.visible_sprites],
                        obstacle_sprites=self.obstacle_sprites
                    )


    def run(self):

        # update sprites
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()