import sys
import pygame
from settings.settings import *
from random import randint

largura = 1280
altura = 720

pygame.init()

#Setando musicas
pygame.mixer.music.set_volume(0.10)
musica_de_fundo = pygame.mixer.music.load('./sons/BoxCat.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('./sons/smw_coin.wav')

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Julio Game');

font = pygame.font.SysFont('arial', 35, True, True)
pontos = 0
fps = 60

x_maca = randint(40, 1000)
y_maca =  randint(60, 700)

tam_cobra_w = 20
tam_cobra_h = 20
cobra = pygame.Rect(10, 10, tam_cobra_w, tam_cobra_h)
color = (255,0,0)

lista_cobra = []
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(screen, (0,255,0), (XeY[0],XeY[1], 20, 20))


while  True:
    mensagem = f'Pontos:{pontos}'
    texto_fomatado = font.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        cobra.x += 20
    elif keys[pygame.K_LEFT]:
        cobra.x -= 20
    elif keys[pygame.K_UP]:
        cobra.y -= 20
    
    elif keys[pygame.K_DOWN]:
        cobra.y += 20 
   
        
    
    if cobra.y >= altura:
        cobra.y = 0
   

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255 ,0), cobra)
    maca = pygame.draw.rect(screen, color, (x_maca, y_maca, 20, 20))
    clock.tick(fps)
    screen.blit(texto_fomatado, (1090, 40))

        
    if cobra.colliderect(maca):
        x_maca = randint(40, 1000)
        y_maca = randint(40, 700)
        pontos+=1
        tam_cobra_w += 20
        barulho_colisao.play()

    lista_cabeca = []
    lista_cabeca.append(cobra.x)
    lista_cabeca.append(cobra.y)

    lista_cobra.append(lista_cabeca)

    aumenta_cobra(lista_cobra)
    pygame.display.update()