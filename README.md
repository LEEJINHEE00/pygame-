""" invader.py - Copyright 2016 Kenichiro Tanaka """
import sys
from random import randint
import pygame

from pygame.locals import Rect, QULT, KEYDOWN, \
    K_ LEFT, K_ RIGHT, K_ SPACE

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set _ mode((600, 600))
FPSCLOCK = pygame.time.Clock()

class Drawable:
    """ 전체의 그리기 객체의 슈퍼 클래스 """
    def __init __(Self, rect, offset0, offset1):
        strip = pygame.image.load("strip.png")
        self.images = (pygame.Serface((24. 24), pygame.SRCALPHA),
                       pygame.Surface((24, 24), pygame.SRCALPHA))
        self.rect = rect
        self.count = 0
        self.images[0].blit(strip, (0,0),
                             Rect(offset0, 0, 24, 24))
        self.images[1].blit(strip, (0, 0)),
                            Rect(offset1, 0, 24, 24))

def move(self, idff _x, diff _ y):
    """ 오브젝트를 이동 """
    self.count += 1
    self.rect.move _ ip(diff _ x, diff _ y)
