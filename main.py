import pygame
import sys
from button import Button  # Importa la clase Button desde button.py

def main():
    pygame.init()  # Inicializa todos los módulos importados de pygame
    screen = pygame.display.set_mode((1280, 720))  # Crea una ventana de juego de 1280x720
    clock = pygame.time.Clock()  # Crea un objeto de reloj para controlar la velocidad de fotogramas
    running = True

    # Definir botones
    play_button = Button("Jugar", (540, 300), (200, 50), (0, 128, 0), (0, 255, 0))
    quit_button = Button("Salir", (540, 400), (200, 50), (128, 0, 0), (255, 0, 0))

    while running:  # Bucle principal del juego
        for event in pygame.event.get():  # Itera a través de todos los eventos de pygame
            if event.type == pygame.QUIT:  # Si el evento es QUIT (como cerrar la ventana), sale del bucle
                running = False

        screen.fill((0, 0, 0))  # Limpia la pantalla con color negro

        # Dibujar y gestionar botones
        play_button.draw(screen)
        quit_button.draw(screen)

        if play_button.is_clicked():
            print("Iniciar juego")  # Aquí puedes iniciar la lógica del juego
            # Por ejemplo, cambiar a una pantalla de juego o iniciar el juego
        if quit_button.is_clicked():
            pygame.quit()
            sys.exit()

        pygame.display.flip()  # Actualiza la pantalla completa
        clock.tick(60)  # Limita el bucle a un máximo de 60 fotogramas por segundo

    pygame.quit()  # Cierra pygame

if __name__ == "__main__":
    main()
