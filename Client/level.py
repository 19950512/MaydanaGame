from typing import Iterable, Union
import pygame
from pygame.sprite import AbstractGroup
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self, received_map):

        # get the display surface
        self.display_surface = pygame.display.get_surface()


        # sprit group setup
        self.visible_sprites = YSortCameraGroup()
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
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.half_screen_width = self.display_surface.get_size()[0] // 2
        self.half_screen_height = self.display_surface.get_size()[1] // 2

        self.offset = pygame.math.Vector2(100, 200)

    def custom_draw(self, player):

        # getting offset
        self.offset.x = player.rect.centerx - self.half_screen_width
        self.offset.y = player.rect.centery - self.half_screen_height

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)