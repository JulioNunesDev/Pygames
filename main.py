import pygame
from pygame.locals import *
import sys

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')

BLACK = (0,0,0)

class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/attack_1.png')) 
        self.sprites.append(pygame.image.load('sprites/attack_2.png')) 
        self.sprites.append(pygame.image.load('sprites/attack_3.png')) 
        self.sprites.append(pygame.image.load('sprites/attack_4.png')) 
        self.sprites.append(pygame.image.load('sprites/attack_5.png')) 
        self.sprites.append(pygame.image.load('sprites/attack_6.png')) 
        self.sprites.append(pygame.image.load('sprites/attack_7.png')) 
        self.sprites.append(pygame.image.load('sprites/attack_8.png')) 
        self.sprites.append(pygame.image.load('sprites/attack_9.png')) 
        self.sprites.append(pygame.image.load('sprites/attack_10.png')) 





while True:
    tela.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()