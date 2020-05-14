import pygame
from pygame.locals import *
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
敌人3出现音效 = pygame.mixer.Sound("音效\敌人3出现.wav")
敌人3出现音效.set_volume(0.2)
敌人1爆炸音效 = pygame.mixer.Sound("音效\敌人1炸.wav")
敌人1爆炸音效.set_volume(0.1)
敌人2爆炸音效 = pygame.mixer.Sound("音效\敌人2炸.wav")
敌人2爆炸音效.set_volume(0.2)
敌人3爆炸音效 = pygame.mixer.Sound("音效\敌人3炸.wav")
敌人3爆炸音效.set_volume(0.5)
我炸了音效 = pygame.mixer.Sound("音效\我炸了.wav")
我炸了音效.set_volume(0.2)

def main():
    pygame.mixer.music.play(-1)

    时钟 = pygame.time.Clock()

    运行中 = True

    while  运行中:
        for 事件 in pygame.event.get():
            if 事件.type == QUIT:
                pygame.quit()
                sys.exit()

        窗口.blit(背景, (0,0))

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