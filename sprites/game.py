import pygame.sprite


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.step = 0
        self.points = 0
        self.font = pygame.font.Font(r"assets\fonts\gamefont.ttf", 20)
        self.image = self.font.render(f"HI {self.points}", True,
                                      (83, 83, 83))
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 70

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.image = self.font.render(f"HI {self.points}", True,
                                      (83, 83, 83))

    def update(self):
        self.step += 1
        if self.step % 10 == 0:
            self.points += 1


class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load(r"assets\images\reset.png")
        self.font = pygame.font.Font(r"assets\fonts\gamefont.ttf", 20)
        self.image = self.font.render("G A M E  O V E R", True,
                                      (83, 83, 83))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 110
        self.rect1 = self.image1.get_rect()
        self.rect1.x = 333
        self.rect1.y = 150

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.image1, self.rect1)
        self.image = self.font.render(f"G A M E  O V E R", True,
                                      (83, 83, 83))