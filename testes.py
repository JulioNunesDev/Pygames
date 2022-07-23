import pygame
import sys
from  time import sleep

janela_w = 500
janela_h = 400

pygame.init()
teladojogo = pygame.display.set_mode((janela_w, janela_h))
pygame.display.set_caption('Julio Game');
musicas = pygame.mixer.music.load('./sons/visc.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play()

x_player, y_player = 0, 0



player2 = pygame.Rect(15, 300, 60, 40)

vidas = 0
fps = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if pygame.key.get_pressed()[pygame.K_w]:
        y_player -= 5
    if pygame.key.get_pressed()[pygame.K_d]:
        x_player += 5
    if pygame.key.get_pressed()[pygame.K_s]:
        y_player += 5
    if pygame.key.get_pressed()[pygame.K_a]:
        x_player -= 5
    
     

    

    
    

    teladojogo.fill((0,0,0))
    player = pygame.draw.rect(teladojogo, (255, 0 , 0), (x_player, y_player, 60, 80))
    pygame.draw.rect(teladojogo, (0, 0 , 255), player2)

        
    player2.move(50, 80)

    if player.colliderect(player2):
         print('colidiu')

    fps.tick(60)
    pygame.display.update()