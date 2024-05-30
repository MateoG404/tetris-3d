from .game.classes.menuInitial import MenuInicial

class NewGame:
    def startNewGame(self):
        print("Starting new game")
        
        self.menu = MenuInicial(1200, 800)
    def run(self):
        self.menu.start()
        return 0