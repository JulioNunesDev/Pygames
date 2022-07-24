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
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (128*3,64*3))
        self.rect = self.image.get_rect()
        self.rect.topleft = 200,70

        self.animar = False
    
    def atacar(self):
        self.animar = True

    def update(self):
        if self.animar == True:
            self.atual += 0.2
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128*3,64*3))



image_fundo = pygame.image.load('sprites_fundo/fundo.jpg').convert()
image_fundo = pygame.transform.scale(image_fundo, (largura, altura) )


frames = pygame.time.Clock()

todas_as_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_as_sprites.add(sapo)






while True:
    frames.tick(60)
    tela.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            sapo.atacar()

    tela.blit(image_fundo, (0,0))
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()