import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, groups, obstacle_sprites):

        super().__init__(groups)

        self.image = pygame.image.load('./graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites