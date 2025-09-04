import pygame

#Isso foi do cacete, pois inicia o modelo do pygame

pygame.init()

WIDTH, HEIGHT = 1550, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo Indie")

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()

