import pygame

class UIScreen:
    def __init__(self):
        self.UIscreen=[[[-1]*5 for i in range(5)] for j in range(5)]
        self.UIrectList=[]
        self.persp = True
        self.dT = 10 # Constante de tiempo para evitar que el juego se ejecute muy rápido