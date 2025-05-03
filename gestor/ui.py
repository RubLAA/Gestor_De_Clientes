from tkinter import Tk, Button

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('Gestor de clientes')
        self.build()

    def build(self):
        # Usa "self" como contenedor del botón (no self.root)
        button = Button(self, text="Hola", command=self.hola)
        button.pack()

    def hola(self):
        print("¡Hola mundo!")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()