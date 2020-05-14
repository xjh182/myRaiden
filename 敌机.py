import pygame
from random import *

class 小敌机(pygame.sprite.Sprite):
    def __init__(self, 背景尺寸):
        pygame.sprite.Sprite.__init__(self)

        self.图片 = pygame.image.load("图片\敌人1.png").convert_alpha()
        self.矩形 = self.图片.get_rect()
        self.宽, self.高 = 背景尺寸[0], 背景尺寸[1]
        self.速度 = 3
        self.矩形.left, self.矩形.top = \
            randint(0, self.宽 - self.矩形.width),\
                randint(-5 * self.高, 0)

    def 移动(self):
        if self.矩形.top < self.高:
            self.矩形.top += self.速度
        else:
            self.重置

    def 重置(self):
        self.矩形.left, self.矩形.top = \
            randint(0, self.宽 - self.矩形.width),\
                randint(-5 * self.高, 0)

class 中敌机(pygame.sprite.Sprite):
    def __init__(self, 背景尺寸):
        pygame.sprite.Sprite.__init__(self)

        self.图片 = pygame.image.load("图片\敌人2.png").convert_alpha()
        self.矩形 = self.图片.get_rect()
        self.宽, self.高 = 背景尺寸[0], 背景尺寸[1]
        self.速度 = 2
        self.矩形.left, self.矩形.top = \
            randint(0, self.宽 - self.矩形.width),\
                randint(-10 * self.高, -self.高)

    def 移动(self):
        if self.矩形.top < self.高:
            self.矩形.top += self.速度
        else:
            self.重置

    def 重置(self):
        self.矩形.left, self.矩形.top = \
            randint(0, self.宽 - self.矩形.width),\
                randint(-10 * self.高, -self.height)

class 大敌机(pygame.sprite.Sprite):
    def __init__(self, 背景尺寸):
        pygame.sprite.Sprite.__init__(self)

        self.图片1 = pygame.image.load("图片\敌人3_1.png").convert_alpha()
        self.图片2 = pygame.image.load("图片\敌人3_2.png").convert_alpha()
        self.矩形 = self.图片1.get_rect()
        self.宽, self.高 = 背景尺寸[0], 背景尺寸[1]
        self.速度 = 1
        self.矩形.left, self.矩形.top = \
            randint(0, self.宽 - self.矩形.width),\
                randint(-15 * self.高, -5*self.高)

    def 移动(self):
        if self.矩形.top < self.高:
            self.矩形.top += self.速度
        else:
            self.重置

    def 重置(self):
        self.矩形.left, self.矩形.top = \
            randint(0, self.宽 - self.矩形.width),\
                randint(-15 * self.高, -5*self.height)