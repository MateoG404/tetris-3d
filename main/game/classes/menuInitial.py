import tkinter as tk
from game.classes.tetris import Game 
import sys

class MenuInicial():
    def __init__(self, width, height):
        print("width", width, "height", height)
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.minsize(width, height)
        self.root.title("Tetris Computación Visual")
        self._frame = tk.Frame(self.root)
        self._frame.pack(fill=tk.BOTH, expand=True)
        self._canvas = tk.Canvas(self._frame, bg="black")
        self._canvas.pack(fill=tk.BOTH, expand=True)

        self.botonJugar = tk.Button(self.root, text="A jugar", command=self.jugar, width=10, height=2)
        self.botonJugar.place(x=self.width * 0.45, y=self.height * 0.35 + 100)

        self.botonInstrucciones = tk.Button(self.root, text="Ver instrucciones", command=self.ver_instrucciones, width=10, height=2)
        self.botonInstrucciones.place(x=self.width * 0.45, y=self.height * 0.35 + 150)

        self.botonRegresarMenu = tk.Button(self.root, text="Regresar al Menú", command=self.regresar_menu, width=10, height=2, fg="red")

    def run(self):
        game = Game(1200, 800)
        game.start()
        return 0
    
    def jugar(self):
        # Destruir todos los widgets en el frame
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.destroy()
        print("¡Botón 1 presionado!")
        # Iniciar el juego
        sys.exit(self.run())
        
       

    def regresar_menu(self):
        self.botonRegresarMenu.destroy()
        self.botonJugar = tk.Button(self.root, text="A jugar", command=self.jugar, width=10, height=2)
        self.botonJugar.place(x=self.width * 0.45, y=self.height * 0.35 + 100)
        self.botonInstrucciones = tk.Button(self.root, text="Ver instrucciones", command=self.ver_instrucciones, width=10, height=2)
        self.botonInstrucciones.place(x=self.width * 0.45, y=self.height * 0.35 + 150)
        self.instrucciones.destroy()

    def ver_instrucciones(self):
        print("¡Botón 2 presionado!")
        self.botonJugar.destroy()
        self.botonInstrucciones.destroy()
        self.instrucciones = tk.Label(self.root, text="Aquí van las instrucciones...", bg="white", fg="black")
        self.instrucciones.place(x=self.width * 0.25, y=self.height * 0.25, width=self.width * 0.5, height=self.height * 0.5)
        self.botonRegresarMenu.place(x=self.width * 0.1 + 900, y=self.height * 0.8 + 100)

    def start(self):
        self.root.mainloop()


