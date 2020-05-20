import pygame
from random import *

class 子弹补给(pygame.sprite.Sprite):
    def __init__(self, 背景尺寸):
        pygame.sprite.Sprite.__init__(self)
        self.图片 = pygame.image.load("图片\子弹补给.png")
        self.rect = self.图片.get_rect()
        self.宽, self.高 = 背景尺寸[0], 背景尺寸[1]
        self.left, self.bottom = randint(0, self.宽 - self.rect.width), -100
        self.速度 = 1
        self.活着 = False
        self.mask = pygame.mask.from_surface(self.图片)

    def 移动(self):
        if self.rect.top < self.高:
            self.rect.top += self.速度
        else:
            self.活着 = False

    def 重置(self):
        self.活着 = True

class 炸弹补给(pygame.sprite.Sprite):
    def __init__(self, 背景尺寸):
        pygame.sprite.Sprite.__init__(self)
        self.图片 = pygame.image.load("图片\炸弹补给.png")
        self.rect = self.图片.get_rect()
        self.宽, self.高 = 背景尺寸[0], 背景尺寸[1]
        self.left, self.bottom = randint(0, self.宽 - self.rect.width), -100
        self.速度 = 5
        self.活着 = False
        self.mask = pygame.mask.from_surface(self.图片)

    def 移动(self):
        if self.rect.top < self.高:
            self.rect.top += self.速度
        else:
            self.活着 = False

    def 重置(self):
        self.活着 = True
