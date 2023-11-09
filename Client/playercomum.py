import pygame
from settings import *
from player import Player

class PlayerComum(Player):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(pos, groups, obstacle_sprites)