import pygame
from game.definitions.color_definitions import Colors

class InstructionsScreen:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.SysFont(None, 70)  # Fuente más grande para el título
        self.font = pygame.font.SysFont(None, 50)
        self.button_color = Colors.RED
        self.button_rect = pygame.Rect(0, 0, 200, 50)
        self.button_rect.topleft = (20, screen.get_height() - 70)
        self.button_text = self.font.render('Regresar', True, Colors.BLACK)
        self.button_text_rect = self.button_text.get_rect(center=self.button_rect.center)

    def draw(self):
        self.screen.fill(Colors.BLACK)  

        title = self.title_font.render('Instrucciones del Juego', True, Colors.WHITE)
        title_rect = title.get_rect(center=(self.screen.get_width() / 2, 60))  
        self.screen.blit(title, title_rect) 
        
        instructions = [
            ("Utiliza las siguientes teclas para jugar:",""),
            ("A, D", " : Girar cámara"),
            ("W, S", " : Zoom"),
            ("Flechas", " : Mover Tetris"),
            ("R, F", " : Girar Tetris"),
            ("Espacio", " : Soltar Tetris")
        ]

        y_offset = 150
        for key, action in instructions:
            key_text = self.font.render(key, True, Colors.PINK)  
            action_text = self.font.render(action, True, Colors.BLUE)  

            action_pos = (40 + key_text.get_width(), y_offset)

            self.screen.blit(key_text, (40, y_offset))
            self.screen.blit(action_text, action_pos)

            y_offset += 70 

        pygame.draw.rect(self.screen, self.button_color, self.button_rect)
        self.screen.blit(self.button_text, self.button_text_rect)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.button_rect.collidepoint(event.pos):
            return True
        return False