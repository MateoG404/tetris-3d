import pygame
from shapes import Shape
from camera import Camera

class Game:
    def __init__(self):
        self.shapes = [Shape()]
        self.camera = Camera()
        self.score = 0
        self.level = 1
        self.speed = 1

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Mover figura a la izquierda
                pass
            elif event.key == pygame.K_RIGHT:
                # Mover figura a la derecha
                pass
            elif event.key == pygame.K_UP:
                # Rotar figura
                pass
            elif event.key == pygame.K_DOWN:
                # Acelerar caída de figura
                pass
            elif event.key == pygame.K_SPACE:
                # Soltar figura rápido
                pass

        if event.type == pygame.MOUSEMOTION:
            # Rotar cámara
            pass

    def update(self):
        # Lógica de actualización del juego
        pass

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.camera.apply()
        for shape in self.shapes:
            shape.draw()
