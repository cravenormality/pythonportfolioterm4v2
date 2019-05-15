from tkinter import *
import pygame
from pygame import mixer
import random
import time
import math
import os
import threading
from mutagen.mp3 import MP3

WIDTH = 600
HEIGHT = 480
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLAYLST = []

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()


def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(BLACK)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Melodic", largeText)
        TextRect.center = ((WIDTH/2),(HEIGHT/2))
        screen.blit(TextSurf, TextRect)
        pygame.display.update()
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            main()
        

def main():
    gameexit = False
    while not gameexit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(BLACK)

        pygame.display.flip()


game_intro()
main()
pygame.quit()