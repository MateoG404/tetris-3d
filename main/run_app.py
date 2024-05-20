import pygame
import sys
from game.definitions.color_definitions import Colors
from game.utilities.instructions import InstructionsScreen
from game.classes.tetris import Game 
import os

# class Game:
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
#         pygame.display.set_caption('Bienvenido Tetris 3D - Visual Computing 2024 - 1 ')
#         self.clock = pygame.time.Clock()
#         self.running = True
        
        
#         # Definicion colores
#         self.BackgroundColor = Colors.BLACK
#         self.ColorText = Colors.WHITE
        
#         # Configuracion de la fuente
#         self.font = pygame.font.SysFont(None, 55)
#         screen_width, screen_height = self.screen.get_size()
#         self.text = self.font.render('Bienvenido Tetris 3D - Visual Computing 2024 - 1 ', True, self.ColorText)
#         self.text_rect = self.text.get_rect(center=(screen_width/2, screen_height/2))

#         # Definicion del boton "Jugar"
#         self.button_color = Colors.PURPLE
#         self.button_rect = pygame.Rect(0, 0, 350, 50)
#         self.button_rect.center = (screen_width/2, screen_height/2 + 100) 
#         self.button_text = self.font.render('Jugar', True, Colors.BLACK) 
#         self.button_text_rect = self.button_text.get_rect(center=self.button_rect.center)  

#         # Definición del boton "Instrucciones"
#         self.instructions_button_color = Colors.BLUE
#         self.instructions_button_rect = pygame.Rect(0, 0, 350, 50)  
#         self.instructions_button_rect.center = (screen_width/2, screen_height/2 + 200)  
#         self.instructions_button_text = self.font.render('Instrucciones', True, Colors.BLACK)
#         self.instructions_button_text_rect = self.instructions_button_text.get_rect(center=self.instructions_button_rect.center)  

#         # Ventana de instrucciones
#         self.instructions_screen = InstructionsScreen(self.screen)
#         self.game_screen = GameTetris3D(self.screen)

#     def run(self):
#         while self.running:
#             self.handle_events()
#             self.draw()
#             self.clock.tick(60)
        
#         self.quit()

#     def handle_events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.running = False
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if self.button_rect.collidepoint(event.pos):
#                     self.runGame()  # Inicia el juego cuando se presiona el botón de jugar
#                 elif self.instructions_button_rect.collidepoint(event.pos):
#                     self.show_instructions()  # Muestra las instrucciones cuando se presiona el botón de instrucciones   
        
        
#     def draw(self):
#         self.screen.fill(self.BackgroundColor)
#         self.screen.blit(self.text, self.text_rect)
        
#         # Boton jugar
#         pygame.draw.rect(self.screen, self.button_color, self.button_rect)
#         self.screen.blit(self.button_text, self.button_text_rect)

#         # Boton instrucciones
#         pygame.draw.rect(self.screen, self.button_color, self.button_rect)
#         self.screen.blit(self.button_text, self.button_text_rect)
#         pygame.draw.rect(self.screen, self.instructions_button_color, self.instructions_button_rect)
#         self.screen.blit(self.instructions_button_text, self.instructions_button_text_rect)
        
#         pygame.display.flip()

#     def quit(self):
#         pygame.quit()
#         sys.exit()
#     def runGame(self):
#         self.game_screen.runGame()


#     def show_instructions(self):
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#                 elif self.instructions_screen.handle_events(event):
#                     return 

#             self.instructions_screen.draw()
#             pygame.display.flip()
            
def run():
    game = Game(550, 700)
    game.start()
    return 0

if __name__ == "__main__":
    sys.exit(run())

