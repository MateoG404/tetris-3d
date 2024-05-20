import numpy as np
from OpenGL.GL import *

class Shape:
    def __init__(self):
        self.vertices = np.array([
            # Definir vértices del cubo (bloque)
        ])
        self.position = np.array([0, 0, 0])

    def draw(self):
        glBegin(GL_QUADS)
        for vertex in self.vertices:
            glVertex3fv(vertex)
        glEnd()

    def move(self, direction):
        # Mover la figura en la dirección especificada
        pass

    def rotate(self, axis, angle):
        # Rotar la figura alrededor del eje especificado
        pass
