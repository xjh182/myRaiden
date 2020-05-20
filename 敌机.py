import pygame
from random import *

class 小敌机(pygame.sprite.Sprite):
    def __init__(self, 背景尺寸):
        pygame.sprite.Sprite.__init__(self)

        self.图片 = pygame.image.load("图片\敌人1.png").convert_alpha()

        self.摧毁的图片 = []
        self.摧毁的图片.extend([\
            pygame.image.load("图片\敌人1炸1.png").convert_alpha(),
            pygame.image.load("图片\敌人1炸2.png").convert_alpha(),
            pygame.image.load("图片\敌人1炸3.png").convert_alpha(),
            pygame.image.load("图片\敌人1炸4.png").convert_alpha()
            ])
        self.rect = self.图片.get_rect()
        self.宽, self.高 = 背景尺寸[0], 背景尺寸[1]
        self.速度 = 3
        self.活着 = True
        self.mask = pygame.mask.from_surface(self.图片)
        self.rect.left, self.rect.top = \
            randint(0, self.宽 - self.rect.width),\
                randint(-5 * self.高, 0)

    def 移动(self):
        if self.rect.top < self.高:
            self.rect.top += self.速度
        else:
            self.重置

    def 重置(self):
        self.活着 = True
        self.rect.left, self.rect.top = \
            randint(0, self.宽 - self.rect.width),\
                randint(-5 * self.高, 0)

class 中敌机(pygame.sprite.Sprite):
    装甲 = 8

    def __init__(self, 背景尺寸):
        pygame.sprite.Sprite.__init__(self)

        self.图片 = pygame.image.load("图片\敌人2.png").convert_alpha()
        self.被打时图片 = pygame.image.load("图片\敌人2_被击中.png").convert_alpha()

        self.摧毁的图片 = []
        self.摧毁的图片.extend([\
            pygame.image.load("图片\敌人2炸1.png").convert_alpha(),
            pygame.image.load("图片\敌人2炸2.png").convert_alpha(),
            pygame.image.load("图片\敌人2炸3.png").convert_alpha(),
            pygame.image.load("图片\敌人2炸4.png").convert_alpha()
            ])
        self.rect = self.图片.get_rect()
        self.宽, self.高 = 背景尺寸[0], 背景尺寸[1]
        self.速度 = 2
        self.活着 = True
        self.mask = pygame.mask.from_surface(self.图片)
        self.rect.left, self.rect.top = \
            randint(0, self.宽 - self.rect.width),\
                randint(-10 * self.高, -self.高)
        self.装甲 = 中敌机.装甲
        self.被打 = False

    def 移动(self):
        if self.rect.top < self.高:
            self.rect.top += self.速度
        else:
            self.重置

    def 重置(self):
        self.活着 = True
        self.装甲 = 中敌机.装甲
        self.rect.left, self.rect.top = \
            randint(0, self.宽 - self.rect.width),\
                randint(-10 * self.高, -self.高)

class 大敌机(pygame.sprite.Sprite):
    装甲 = 30

    def __init__(self, 背景尺寸):
        pygame.sprite.Sprite.__init__(self)

        self.图片1 = pygame.image.load("图片\敌人3_1.png").convert_alpha()
        self.图片2 = pygame.image.load("图片\敌人3_2.png").convert_alpha()
        self.被打时图片 = pygame.image.load("图片\敌人3_被击中.png").convert_alpha()

        self.摧毁的图片 = []
        self.摧毁的图片.extend([\
            pygame.image.load("图片\敌人3炸1.png").convert_alpha(),
            pygame.image.load("图片\敌人3炸2.png").convert_alpha(),
            pygame.image.load("图片\敌人3炸3.png").convert_alpha(),
            pygame.image.load("图片\敌人3炸4.png").convert_alpha(),
            pygame.image.load("图片\敌人3炸5.png").convert_alpha(),
            pygame.image.load("图片\敌人3炸6.png").convert_alpha()
            ])

        self.rect = self.图片1.get_rect()
        self.宽, self.高 = 背景尺寸[0], 背景尺寸[1]
        self.速度 = 1
        self.活着 = True
        self.mask = pygame.mask.from_surface(self.图片1)
        self.rect.left, self.rect.top = \
            randint(0, self.宽 - self.rect.width),\
                randint(-15 * self.高, -5*self.高)
        self.装甲 = 大敌机.装甲
        self.被打 = False

    def 移动(self):
        if self.rect.top < self.高:
            self.rect.top += self.速度
        else:
            self.重置

    def 重置(self):
        self.活着 = True
        self.装甲 = 大敌机.装甲
        self.rect.left, self.rect.top = \
            randint(0, self.宽 - self.rect.width),\
                randint(-15 * self.高, -5*self.高)