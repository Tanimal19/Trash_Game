import pygame
from setting import *


class Tower:
    def __init__(self):
        self.image = pygame.image.load("Entity/Tower.PNG").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.8)
        self.rect = self.image.get_rect(midbottom=(1100, horizon_y))

        self.max_health = 1000
        self.health = 1000

    def draw(self, canvas):
        canvas.blit(self.image, self.rect)

    def update(self):
        if self.health <= 0:
            self.image = pygame.image.load("Entity/Tower_break.PNG").convert_alpha()
            self.image = pygame.transform.rotozoom(self.image, 0, 0.8)

        if self.health > self.max_health:
            self.health = self.max_health

        self.rect = self.image.get_rect(midbottom=(1100, horizon_y))


class HealthBar:
    def __init__(self, canvas):
        self.canvas = canvas

    def update(self, ratio):
        pygame.draw.rect(self.canvas, RED, (0, 0, WIDTH * ratio, 12))
        pygame.draw.rect(self.canvas, "black", (0, 0, WIDTH, 12), 3)
