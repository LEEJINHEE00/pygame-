""" mine_sweeper.py - Copyright 2016 Kenichiro Tanaka  """
import sys
from math import floor
from random import randint
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

WIDTH = 10
HEIGHT = 10
SIZE = 40
NUM_OF_BOMBS = 20
EMPTY = 0
BOMB = 2
OPENED = 2
OPEN_COUNT = 0
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
