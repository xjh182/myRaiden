import pygame
from pygame.locals import *
import 我方飞机
import 敌机
import sys
import traceback
import os

os.getcwd()

pygame.init()
pygame.mixer.init()

背景尺寸 = 宽, 高 = 480, 700
窗口 = pygame.display.set_mode(背景尺寸)
pygame.display.set_caption("打灰机")

背景 = pygame.image.load("图片/背景.png").convert()

pygame.mixer.music.load("音效/bgm.ogg")
pygame.mixer.music.set_volume(0.2)
枪声 = pygame.mixer.Sound("音效\枪声.wav")
枪声.set_volume(0.2)
补给音效 = pygame.mixer.Sound("音效\补给.wav")
补给音效.set_volume(0.2)
获得炸弹音效 = pygame.mixer.Sound("音效\获得炸弹.wav")
获得炸弹音效.set_volume(0.2)
敌机3出现音效 = pygame.mixer.Sound("音效\敌人3出现.wav")
敌机3出现音效.set_volume(0.2)
敌机1爆炸音效 = pygame.mixer.Sound("音效\敌人1炸.wav")
敌机1爆炸音效.set_volume(0.1)
敌机2爆炸音效 = pygame.mixer.Sound("音效\敌人2炸.wav")
敌机2爆炸音效.set_volume(0.2)
敌机3爆炸音效 = pygame.mixer.Sound("音效\敌人3炸.wav")
敌机3爆炸音效.set_volume(0.5)
我炸了音效 = pygame.mixer.Sound("音效\我炸了.wav")
我炸了音效.set_volume(0.2)

def 增加小敌机(小敌机组, 全部敌机组, 数量):
    for 每一个 in range(数量):
        敌机1 = 敌机.小敌机(背景尺寸)
        小敌机组.add(敌机1)
        全部敌机组.add(敌机1)

def 增加中敌机(中敌机组, 全部敌机组, 数量):
    for 每一个 in range(数量):
        敌机2 = 敌机.中敌机(背景尺寸)
        中敌机组.add(敌机2)
        全部敌机组.add(敌机2)

def 增加大敌机(大敌机组, 全部敌机组, 数量):
    for 每一个 in range(数量):
        敌机3 = 敌机.大敌机(背景尺寸)
        大敌机组.add(敌机3)
        全部敌机组.add(敌机3)

def main():
    pygame.mixer.music.play(-1)

    我 = 我方飞机.我方飞机(背景尺寸)

    敌机们 = pygame.sprite.Group()

    小敌机 = pygame.sprite.Group()
    增加小敌机(小敌机, 敌机们, 15)

    中敌机 = pygame.sprite.Group()
    增加中敌机(中敌机, 敌机们, 4)

    大敌机 = pygame.sprite.Group()
    增加大敌机(大敌机, 敌机们, 2)

    时钟 = pygame.time.Clock()

    小敌机爆炸索引 = 0
    中敌机爆炸索引 = 0
    大敌机爆炸索引 = 0
    我自己爆炸索引 = 0

    切换图片 = True

    延迟 = 100

    运行中 = True

    while  运行中:
        for 事件 in pygame.event.get():
            if 事件.type == QUIT:
                pygame.quit()
                sys.exit()

        # 检测用户的键盘操作
        键盘按下 = pygame.key.get_pressed()

        if 键盘按下[K_w] or 键盘按下[K_UP]:
            我.向上()
        if 键盘按下[K_s] or 键盘按下[K_DOWN]:
            我.向下()
        if 键盘按下[K_a] or 键盘按下[K_LEFT]:
            我.向左()
        if 键盘按下[K_d] or 键盘按下[K_RIGHT]:
            我.向右()

        窗口.blit(背景, (0,0))

        #绘制大型敌机
        for 每一个 in 大敌机:
            if 每一个.活着:
                每一个.移动()
                if 切换图片:
                    窗口.blit(每一个.图片1, 每一个.rect)
                else:
                    窗口.blit(每一个.图片2, 每一个.rect)
                #即将出现音效
                if 每一个.rect.bottom == -50:
                    敌机3出现音效.play(-1)
            else:
                #毁灭
                if not(延迟 % 3):
                    if 大敌机爆炸索引 == 0:
                        敌机3爆炸音效.play()
                    窗口.blit(每一个.摧毁的图片[大敌机爆炸索引], 每一个.rect)
                    大敌机爆炸索引 = (大敌机爆炸索引 + 1) % 6
                    if 大敌机爆炸索引 == 0:
                        敌机3出现音效.stop()
                        每一个.重置()

        #绘制中型敌机
        for 每一个 in 中敌机:
            if 每一个.活着:
                每一个.移动()
                窗口.blit(每一个.图片, 每一个.rect)
            else:
                #毁灭
                if not(延迟 % 3):
                    if 中敌机爆炸索引 == 0:
                        敌机2爆炸音效.play()
                    窗口.blit(每一个.摧毁的图片[我自己爆炸索引], 每一个.rect)
                    我自己爆炸索引 = (我自己爆炸索引 + 1) % 4
                    if 中敌机爆炸索引 == 0:
                        每一个.重置()

        #绘制小型敌机
        for 每一个 in 小敌机:
            if 每一个.活着:
                每一个.移动()
                窗口.blit(每一个.图片, 每一个.rect)
            else:
                #毁灭
                if not(延迟 % 3):
                    if 小敌机爆炸索引 == 0:
                        敌机1爆炸音效.play()
                    窗口.blit(每一个.摧毁的图片[大敌机爆炸索引], 每一个.rect)
                    大敌机爆炸索引 = (大敌机爆炸索引 + 1) % 4
                    if 小敌机爆炸索引 == 0:
                        每一个.重置()

        与敌人碰撞 = pygame.sprite.spritecollide(我, 敌机们, False, pygame.sprite.collide_mask)
        if 与敌人碰撞:
            我.活着 = True
            for 敌人 in 与敌人碰撞:
                敌人.活着 = False

        #绘制自己
        if 我.活着:
            if 切换图片:
                窗口.blit(我.图片1, 我.rect)
            else:
                窗口.blit(我.图片2, 我.rect)
        else:
            #毁灭
            我炸了音效.play()
            if not(延迟 % 3):
                窗口.blit(每一个.摧毁的图片[我自己爆炸索引], 每一个.rect)
                我自己爆炸索引 = (大敌机爆炸索引 + 1) % 4
                if 我自己爆炸索引 == 0:
                    print("你机没了")
                    运行中 = False

        if not(延迟 % 5):
            切换图片 = not 切换图片

        延迟 -= 1
        if not 延迟:
            延迟 = 100

        pygame.display.flip()

        时钟.tick(60)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()