import sys
from game.definitions.color_definitions import Colors
from game.definitions.global_definitions import GlobalDefinitions
from game.classes.engine import GUI, GUIText, GUIRect, Color
from tkinter import Tk, Canvas
import tkinter as tk
class GameTetris3D:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.running = False
        self.button_rect.center = (self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.global_variables = GlobalDefinitions()


    def initialize_game(self):
        self.global_variables.initialize_tiles()


class Menu(GUI):
    def key_press(self, key):
        raise NotImplementedError

class Pause(Menu):
    def draw(self, canvas, **kwargs):
        w, h = canvas.winfo_width(), canvas.winfo_height()
        wf, hf = 240, 80
        frame = GUIRect((w - wf) * 0.5, (h - hf) * 0.5, wf, hf, Color(250, 150, 150))
        frame.draw(canvas, **kwargs)
        text = GUIText("Pause", w * 0.5, h * 0.5, 50, Color(100, 100, 100))
        text.draw(canvas, **kwargs)

    def key_press(self, key):
        if key == 'p':
            return None
        else:
            return self

class GameOver():
    def __init__(self):
        self.a = 0

    def draw(self, canvas, **kwargs):
        w, h = canvas.winfo_width(), canvas.winfo_height()
        wf, hf = 450, 110
        frame = GUIRect((w - wf) * 0.5, (h - hf) * 0.5, wf, hf, Color(250, 150, 150))
        frame.draw(canvas, **kwargs)
        head = GUIText("Game Over", w * 0.5, (h - hf) * 0.5 + 35, 40, Color(100, 100, 100))
        head.draw(canvas, **kwargs)
        cont = GUIText("<SPACE> para reiniciar", w * 0.5, (h - hf) * 0.5 + 85, 15, Color(100, 100, 100))
        cont.draw(canvas, **kwargs)

    def key_press(self, key):
        if ord(key) == 32:
            for widget in tk._default_root.winfo_children():
                widget.destroy()
        return self


class HighScore(Menu):
    def __init__(self, table, next_menu):
        self._next_menu = next_menu
        self._table = table

    def draw(self, canvas, **kwargs):
        w, h = canvas.winfo_width(), canvas.winfo_height()
        fw, fh = 500, 400
        frame = GUIRect((w - fw) * 0.5, (h - fh) * 0.5, fw, fh, Color(250, 150, 150))
        frame.draw(canvas, **kwargs)

        head_space = 35
        head = GUIText("High Scores", w * 0.5, (h - fh) * 0.5 + head_space, 30, Color(100, 100, 100))
        head.draw(canvas, **kwargs)

        table_space = 205
        rank = "\n".join(str(i) for i in range(1, 11))
        names = "\n".join(self._table.names())
        time = "\n".join(self._table.times())
        score = "\n".join(str(s) for s in self._table.scores())
        rank_l = GUIText(rank, (w - fw) * 0.5 + 30, (h - fh) * 0.5 + table_space, 18, Color(100, 100, 100), GUIText.RIGHT)
        names_l = GUIText(names, (w - fw) * 0.5 + 115, (h - fh) * 0.5 + table_space, 18, Color(100, 100, 100), GUIText.LEFT)
        time_l = GUIText(time, w * 0.5, (h - fh) * 0.5 + table_space, 18, Color(100, 100, 100), GUIText.CENTER)
        score_l = GUIText(score, (w + fw) * 0.5 - 30, (h - fh) * 0.5 + table_space, 18, Color(100, 100, 100), GUIText.RIGHT)
        rank_l.draw(canvas, **kwargs)
        names_l.draw(canvas, **kwargs)
        time_l.draw(canvas, **kwargs)
        score_l.draw(canvas, **kwargs)

       

    def key_press(self, key):
        if ord(key) == 13:
            return self._next_menu
        return self



class StartGame(Menu):
    LEVEL_STR = ("easy", "medium", "hard")

    def __init__(self, game):
        self._game = game
        self._help = Help(self)

    def draw(self, canvas, **kwargs):
        w, h = canvas.winfo_width(), canvas.winfo_height()
        fw, fh = 440, 305
        frame = GUIRect((w - fw) * 0.5, (h - fh) * 0.5, fw, fh, Color(250, 150, 150))
        frame.draw(canvas, **kwargs)
        head = GUIText(("Estas en el nivel (%s)" % (self._game.level())), w * 0.5, (h - fh) * 0.5 + 30, 30, Color(100, 100, 100))
        head.draw(canvas, **kwargs)
        text = GUIText("Presiona la letra S para comenzar a jugar\n"
                    #    "<1> Change game level to 1\n"
                    #    "<2> Change game level to 2\n"
                    #    "<3> Change game level to 3\n"
                       ,w * 0.5, (h - fh) * 0.5 + 180, 18, Color(100, 100, 100))
        text.draw(canvas, **kwargs)

    def key_press(self, key):
        if key == 's':
            self._game.reset_game()
            return None
        if key == '1':
            self._game.set_level(0)
        if key == '2':
            self._game.set_level(1)
        if key == '3':
            self._game.set_level(2)
        if key == 'h':
            return self._help
        return self


class Help(Menu):
    def __init__(self, next_menu):
        self.text = """
        Comandos del Juego:
        - Movimiento:
            - Espacio: Mover rápido hacia abajo
            - Flecha izquierda: Mover a la izquierda
            - Flecha abajo: Mover hacia atrás
            - Flecha derecha: Mover a la derecha
            - Flecha arriba: Mover hacia adelante
        - Rotación:
            - s: Rotar en el eje X en dirección negativa
            - w: Rotar en el eje X en dirección positiva
            - a: Rotar en el eje Y en dirección negativa
            - d: Rotar en el eje Y en dirección positiva
            - q: Rotar en el eje Z en dirección negativa
            - e: Rotar en el eje Z en dirección positiva
        - Cámara:
            - z: Rotar cámara a la izquierda
            - c: Rotar cámara a la derecha
        - Menús:
            - p: Pausar/Despausar
        """
        self.frame = GUIRect(50, 50, 300, 200, Color(200, 200, 200))
        self.text_widget = GUIText(self.text, 100, 75, 12, Color(0, 0, 0))
        self._next_menu = next_menu

    def draw(self, canvas, **kwargs):
        w, h = canvas.winfo_width(), canvas.winfo_height()
        fw, fh = 500, 650
        frame = GUIRect((w - fw) * 0.5, (h - fh) * 0.5, fw, fh, Color(250, 150, 150))
        frame.draw(canvas, **kwargs)
        head = GUIText("Help", w * 0.5, (h - fh) * 0.5 + 30, 30, Color(100, 100, 100))
        head.draw(canvas, **kwargs)

    def key_press(self, key):
        if ord(key) == 13:
            return self._next_menu
        return self