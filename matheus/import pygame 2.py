import pygame
import os

#Isso foi do cacete, pois inicia o modelo do pygame

pygame.init()

WIDTH, HEIGHT = 1550, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Jogo Indie")

cor = (109,150,255)

imagem = "player.png"
if os.path.exists(imagem):
    img = pygame.image.load(imagem).convert_alpha()
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
else:
    print("F")

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(cor)
    screen.blit(img, img_rect.topleft)
    pygame.display.flip()

pygame.quit()