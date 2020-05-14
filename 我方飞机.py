import pygame

class 我方飞机(pygame.sprite.Sprite):
    def __init__(self, 背景尺寸):
        pygame.sprite.Sprite.__init__(self)

        self.图片1 = pygame.image.load("图片\玩家1.png").convert_alpha()
        self.图片2 = pygame.image.load("图片\玩家2.png").convert_alpha()

        self.摧毁的图片 = []
        self.摧毁的图片.extend([\
            pygame.image.load("图片\玩家炸1.png").convert_alpha(),
            pygame.image.load("图片\玩家炸2.png").convert_alpha(),
            pygame.image.load("图片\玩家炸3.png").convert_alpha(),
            pygame.image.load("图片\玩家炸4.png").convert_alpha(),
            ])

        self.rect = self.图片1.get_rect()
        self.宽, self.高 = 背景尺寸[0], 背景尺寸[1]
        self.rect.left, self.rect.top = \
            (self.宽 - self.rect.width) // 2,\
                self.高 - self.rect.height - 60
        self.速度 = 10
        self.活着 = True
        self.mask = pygame.mask.from_surface(self.图片1)

    def 向上(self):
        if self.rect.top > 0:
            self.rect.top -= self.速度
        else:
            self.rect.top = 0

    def 向下(self):
        if self.rect.bottom < self.高 - 60:
            self.rect.top += self.速度
        else:
            self.rect.bottom = self.高 - 60

    def 向左(self):
        if self.rect.left > 0:
            self.rect.left -= self.速度
        else:
            self.rect.left = 0

    def 向右(self):
        if self.rect.right < self.宽:
            self.rect.left += self.速度
        else:
            self.rect.left = self.宽 - self.rect.width