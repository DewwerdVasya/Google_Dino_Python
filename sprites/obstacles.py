import os.path
import random

import pygame.sprite


class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        images = ['largecactus1.png', 'largecactus2.png',
                  'largecactus3.png', 'smallcactus1.png',
                  'smallcactus2.png', 'smallcactus3.png']
        image = os.path.join(r"assets\images", random.choice(images))
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        surface = pygame.display.get_surface()
        self.rect.bottomleft = (2 * surface.get_width(), surface.get_height() / 1.95)
        self.speed = 5

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()











