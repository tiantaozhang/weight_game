# -*- coding: utf8 -*-

import sys, pygame
from pygame.locals import *
from random import randrange

class Weight(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #画 sprite时使用的图像和矩形
        self.image = weight_image
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        """
        将秤砣移动到屏幕顶端的随机位置
        :return:
        """
        self.rect.top = -self.rect.height
        self.rect.centerx = randrange(screen_size[0])

    def update(self):
        """
        更新秤砣，显示下一帧
        :return:
        """
        self.rect.top += 1
        if self.rect.top > screen_size[1]:
            self.reset()


# init
pygame.init()
screen_size = 800, 600
pygame.display.set_mode(screen_size, FULLSCREEN)
pygame.mouse.set_visible(0)


weight_image = pygame.image.load('weight.png')
weight_image = weight_image.convert() # to match the display

# 创建子图形組，增加weight
sprites = pygame.sprite.RenderUpdates()
sprites.add(Weight())


screen = pygame.display.get_surface()
bg = (255, 255, 255)
screen.fill(bg)
pygame.display.flip()


def clear_callback(surf, rect):
    surf.fill(bg, rect)





#清楚前面的位置
sprites.clear(screen, clear_callback)

sprites.update()

updates = sprites.draw(screen)

pygame.display.update(updates)


while True:
    #
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
