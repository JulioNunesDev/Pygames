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
velocidade = 2
x_controller = velocidade
y_controller = 0

tam_cobra_w = 20
tam_cobra_h = 20

x_cobra = int(largura/2)
y_cobra = int(altura/2) 

color_maca = (255,0,0)
color_cobra = (0,255,0)

lista_cobra = []

cobra_is_dead = False

comprimento_inicial = 5
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(screen, (0,255,0), (XeY[0],XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cabeca, lista_cobra, x_maca, y_maca, cobra_is_dead
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura/2)
    y_cobra = int(altura/2) 
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 1000)
    y_maca =  randint(60, 700)
    cobra_is_dead = False


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
    if lista_cobra.count(lista_cabeca) > 1:

        font2 = pygame.font.SysFont('arial', 40, True, True)

        mensagem2 = 'Game over! Pressione a tecla R para jogar novamente'

        texto_formatado2 = font2.render(mensagem2, True, (0,0,0))
        ret_texto = texto_formatado2.get_rect()

        cobra_is_dead = True
        while cobra_is_dead:
            screen.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        reiniciar_jogo()
            ret_texto.center = (largura//2, altura//2)
            screen.blit(texto_formatado2, ret_texto)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra =0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
    pygame.display.update()