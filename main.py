import sys
import pygame
from settings.settings import *

largura = 1280
altura = 720

pygame.init()

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Julio Game');

font = pygame.font.SysFont('arial', 35, True, True)
pontos = 0
fps = 60
player = pygame.Rect(10, 10, 50, 50)
player2 = pygame.Rect(300, 10, 100, 50)
color = (255,255,0)
while  True:
    mensagem = f'Pontos:{pontos}'
    texto_fomatado = font.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player.x += 3
    elif keys[pygame.K_LEFT]:
        player.x -= 3
    elif keys[pygame.K_UP]:
        player.y -= 3
    
    elif keys[pygame.K_DOWN]:
        player.y += 3 
       
    if player.colliderect(player2):
        color = (255, 0, 245)
        pontos+=1
        
    else:
        color = (255, 255, 0)
    
    if player.y >= altura:
        player.y = 0
   

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0 ,0), player, 3)
    pygame.draw.rect(screen, color, player2, 3)
    clock.tick(fps)
    screen.blit(texto_fomatado, (1090, 40))
    pygame.display.update()