# Punto de entrada principal de la aplicación

import pygame 

pygame.init()


# Create a screen object
size = [700, 500]
screen = pygame.display.set_mode(size)
# Set the title of the window
pygame.display.set_caption("My first Pygame window")
# Run the game until the user closes the window
running = True
while running:
 for event in pygame.event.get():
   if event.type == pygame.QUIT:
       running = False
