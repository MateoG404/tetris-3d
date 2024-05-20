from OpenGL.GL import *
from OpenGL.GLU import *

class Camera:
    def __init__(self):
        self.angle_x = 0
        self.angle_y = 0

    def apply(self):
        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0)

    def rotate(self, x, y):
        self.angle_x += x
        self.angle_y += y
