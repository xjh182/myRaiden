import pygame

class 子弹1(pygame.sprite.Sprite):
    def __init__(self,位置):
        pygame.sprite.Sprite.__init__(self)

        self.图片 = pygame.image.load("图片\子弹1.png").convert_alpha()
        self.rect = self.图片.get_rect()
        self.rect.left, self.rect.top = 位置
        self.速度 = 12
        self.活着 = True
        self.mask = pygame.mask.from_surface(self.图片)

    def 发射(self):
        self.rect.top -= self.速度

        if self.rect.top < 0:
            self.活着 = False

    def 重置(self,位置):
        self.rect.left, self.rect.top = 位置
        self.活着 = True

class 子弹2(pygame.sprite.Sprite):
    def __init__(self,位置):
        pygame.sprite.Sprite.__init__(self)

        self.图片 = pygame.image.load("图片\子弹2.png").convert_alpha()
        self.rect = self.图片.get_rect()
        self.rect.left, self.rect.top = 位置
        self.速度 = 14
        self.活着 = True
        self.mask = pygame.mask.from_surface(self.图片)

    def 发射(self):
        self.rect.top -= self.速度

        if self.rect.top < 0:
            self.活着 = False

    def 重置(self,位置):
        self.rect.left, self.rect.top = 位置
        self.活着 = True