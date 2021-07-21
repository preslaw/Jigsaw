import pygame

pygame.init()
screenSize = (800,600)
window = pygame.display.set_mode((screenSize))

image = pygame.image.load('101000_8.jpg')
image = pygame.transform.scale(image,screenSize)

run = True

while run:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(image,(0,0))

    pygame.display.update()

