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
velocidade = 10
x_controller = velocidade
y_controller = 0

tam_cobra_w = 20
tam_cobra_h = 20

x_cobra = int(largura/2)
y_cobra = int(altura/2) 

color_maca = (255,0,0)
color_cobra = (0,255,0)

lista_cobra = []
comprimento_inicial = 5
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if x_controller == velocidade:
                    pass
                else:
                    x_controller = -velocidade
                    y_controller = 0
            elif event.key == pygame.K_d:
                 if x_controller == -velocidade:
                    pass
                 else:
                    x_controller = velocidade
                    y_controller = 0
            elif event.key == pygame.K_w:
                if y_controller == velocidade:
                    pass
                else:
                    y_controller = -velocidade
                    x_controller = 0
            elif event.key == pygame.K_s:
                if y_controller == -velocidade:
                    pass
                else: 
                    y_controller = velocidade
                    x_controller = 0

    x_cobra += x_controller
    y_cobra +=  y_controller
    
  
        
    
   

    screen.fill((0, 0, 0))

    cobra = pygame.draw.rect(screen, color_cobra, (x_cobra, y_cobra, tam_cobra_w, tam_cobra_h))
    maca = pygame.draw.rect(screen, color_maca, (x_maca, y_maca, 20, 20))
    clock.tick(fps)
    screen.blit(texto_fomatado, (1090, 40))

    
    if y_cobra >= altura:
        y_cobra = 0

    if cobra.colliderect(maca):
        x_maca = randint(40, 1000)
        y_maca = randint(40, 700)
        pontos+=1
        comprimento_inicial += 1
        barulho_colisao.play()

    lista_cabeca = []
    lista_cabeca.append(cobra.x)
    lista_cabeca.append(cobra.y)

    lista_cobra.append(lista_cabeca)
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
    pygame.display.update()