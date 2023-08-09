import pygame
import sys

pygame.init()

# Definir las dimensiones de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Título de la ventana
pygame.display.set_caption('Cerdito de cuerpo completo')

# Color de fondo
background_color = (255, 255, 255)

# Velocidad de refresco (FPS)
fps = 60
clock = pygame.time.Clock()

# Carga las imágenes del cerdito
pig_image = pygame.image.load('pig.JPG')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         pygame.quit()
    sys.exit()

    # Limpia la pantalla con el color de fondo
    screen.fill(background_color)

    # Dibuja el cerdito en la pantalla
    screen.blit(pig_image, (width // 2 - pig_image.get_width() // 2, height // 2 - pig_image.get_height() // 2))

    # Actualiza la pantalla
    pygame.display.flip()

    # Controla el FPS
    clock.tick(fps)