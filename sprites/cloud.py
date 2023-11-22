import pygame.sprite
import random


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"assets\images\cloud.png")
        self.rect = self.image.get_rect()
        self.speed = random.randint(3, 6)
        surface = pygame.display.get_surface()
        self.rect.x = surface.get_width()
        self.rect.y = random.randint(0, 170)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()


















