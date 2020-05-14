import pygame

class 我方飞机(pygame.sprite.Sprite):
    def __init__(self, 背景尺寸):
        pygame.sprite.Sprite.__init__(self)

        self.图片1 = pygame.image.load("图片\玩家1.png").convert_alpha()
        self.图片2 = pygame.image.load("图片\玩家2.png").convert_alpha()
        self.矩形 = self.图片1.get_rect()
        self.宽, self.高 = 背景尺寸[0], 背景尺寸[1]
        self.矩形.left, self.矩形.top = \
            (self.宽 - self.矩形.width) // 2,\
                self.高 - self.矩形.height - 60
        self.速度 = 10

    def 向上(self):
        if self.矩形.top > 0:
            self.矩形.top -= self.速度
        else:
            self.矩形.top = 0

    def 向下(self):
        if self.矩形.bottom < self.高 - 60:
            self.矩形.top += self.速度
        else:
            self.矩形.bottom = self.高 - 60

    def 向左(self):
        if self.矩形.left > 0:
            self.矩形.left -= self.速度
        else:
            self.矩形.left = 0

    def 向右(self):
        if self.矩形.right < self.宽:
            self.矩形.left += self.速度
        else:
            self.矩形.left = self.宽 - self.矩形.width