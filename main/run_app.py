import sys
from game.definitions.color_definitions import Colors
from game.utilities.instructions import InstructionsScreen
from game.classes.tetris import Game 
from game.classes.run_game import StartGame, Menu
from game.classes.engine import GUI, GUIText, GUIRect, Color

import os
     
def run():

    game = Game(1200, 800)
    game.start()

if __name__ == "__main__":
    run()