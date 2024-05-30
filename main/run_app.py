import sys
from game.definitions.color_definitions import Colors
from game.utilities.instructions import InstructionsScreen
from game.classes.tetris import Game 
from game.classes.run_game import StartGame, Menu
from game.classes.engine import GUI, GUIText, GUIRect, Color
from game.classes.menuInitial import MenuInicial
import os
     
def run():
    menu = MenuInicial(1200, 800)
    menu.start()


if __name__ == "__main__":
    run()
