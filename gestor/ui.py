from tkinter import Tk, Frame, CENTER, NO, Scrollbar, RIGHT, Y, Button, Toplevel, Label, Entry, DISABLED, NORMAL
from tkinter.messagebox import askokcancel, WARNING
from tkinter import ttk
import database as db
import helpers

class CenterWidgetMixin: 
    def center(self):  # Quita la coma extra
        self.update() 
        w = self.winfo_width() 
        h = self.winfo_height() 
        ws = self.winfo_screenwidth() 
        hs = self.winfo_screenheight() 
        x = int((ws/2) - (w/2)) 
        y = int((hs/2) - (h/2)) 
        self.geometry(f"{w}x{h}+{x}+{y}")

class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self): 
        super().__init__() 
        self.title('Gestor de clientes') 
        self.build() 
        self.center()
        

    def build(self): 
        # Top Frame 
        frame = Frame(self) 
        frame.pack() 
        
        # Scrollbar 
        scrollbar = Scrollbar(frame) 
        scrollbar.pack(side=RIGHT, fill=Y) 
        
        # Treeview (¡definirlo una sola vez!)
        treeview = ttk.Treeview(frame, yscrollcommand=scrollbar.set) 
        treeview['columns'] = ('DNI', 'Nombre', 'Apellido') 
        
        # Configurar columnas 
        treeview.column("#0", width=0, stretch=NO) 
        treeview.column("DNI", anchor=CENTER) 
        treeview.column("Nombre", anchor=CENTER) 
        treeview.column("Apellido", anchor=CENTER) 
        
        # Configurar cabeceras 
        treeview.heading("#0", anchor=CENTER) 
        treeview.heading("DNI", text="DNI", anchor=CENTER) 
        treeview.heading("Nombre", text="Nombre", anchor=CENTER) 
        treeview.heading("Apellido", text="Apellido", anchor=CENTER) 
        
        # Empaquetar Treeview 
        treeview.pack() 

        # Fill treeview data 
        for cliente in db.Clientes.lista: 
            treeview.insert( 
                parent='', index='end', iid=cliente.dni, 
                values=(cliente.dni, cliente.nombre, cliente.apellido)) 

        # Bottom Frame 
        frame = Frame(self) 
        frame.pack(pady=20) 
        
        # Buttons 
        Button(frame, text="Crear", command=self.create_client_window).grid(row=1, column=0) 
        Button(frame, text="Modificar", command=None).grid(row=1, column=1) 
        Button(frame, text="Borrar", command=self.delete).grid(row=1, column=2) 

        # Export treeview to the class 
        self.treeview = treeview

    def delete(self): 
        cliente = self.treeview.focus() 
        if cliente: 
            campos = self.treeview.item(cliente, 'values') 
            confirmar = askokcancel( 
                title='Confirmación', 
                message=f'¿Borrar a {campos[1]} {campos[2]}?', 
                icon= WARNING) 
            if confirmar: 
                # remove the row 
                self.treeview.delete(cliente) 
    
    def create_client_window(self): 
        CreateClientWindow(self)

class CreateClientWindow(Toplevel, CenterWidgetMixin): 
    def __init__(self, parent): 
        super().__init__(parent) 
        self.title('Crear cliente') 
        self.build() 
        self.center() 
        self.transient(parent)
        self.grab_set()
        

    def build(self): 
        # Top frame 
        frame = Frame(self) 
        frame.pack(padx=20, pady=10) 

        # Labels 
        Label(frame, text="DNI (2 ints y 1 upper char)").grid(row=0, 
        column=0) 
        Label(frame, text="Nombre (2 a 30 chars)").grid(row=0, 
        column=1) 
        Label(frame, text="Apellido (2 a 30 chars)").grid(row=0, 
        column=2) 

        # Estado inicial de las validaciones (DNI, Nombre, Apellido)
        self.validaciones = [False, False, False]

        # Entries and validations 
        dni = Entry(frame) 
        dni.grid(row=1, column=0) 
        dni.bind("<KeyRelease>", lambda ev: self.validate(ev, 0)) 
        nombre = Entry(frame) 
        nombre.grid(row=1, column=1) 
        nombre.bind("<KeyRelease>", lambda ev: self.validate(ev, 1)) 
        apellido = Entry(frame) 
        apellido.grid(row=1, column=2) 
        apellido.bind("<KeyRelease>", lambda ev: self.validate(ev, 2))

        # Exportar botón "Crear" para modificarlo
        self.crear = crear
        self.dni = dni 
        self.nombre = nombre 
        self.apellido = apellido 

        # Bottom frame 
        frame = Frame(self) 
        frame.pack(pady=10) 

        # Buttons 
        crear = Button(frame, text="Crear", 
        command=self.create_client) 
        crear.configure(state=DISABLED) 
        crear.grid(row=0, column=0) 
        Button(frame, text="Cancelar", command=self.close).grid(row=0, 
        column=1) 

        

    def create_client(self): 
        pass 

    def close(self): 
        self.destroy() 
        self.update() 

    def validate(self, event, index): 
        valor = event.widget.get() 
        # Validar el dni si es el primer campo o textual para los otros dos 
        valido = helpers.dni_valido(valor, db.Clientes.lista) if index == 0 else (valor.isalpha() and len(valor) >= 2 and len(valor) <= 30) 
        event.widget.configure({"bg": "Green" if valido else "Red"}) 
        # Cambiar estado del botón en base a las validaciones 
        self.validaciones[index] = valido 
        self.crear.config(state=NORMAL if self.validaciones == [1, 1, 1] else DISABLED)
    
    def create_client(self): 
        self.master.treeview.insert( 
            parent='', index='end', iid=self.dni.get(), 
            values=(self.dni.get(), self.nombre.get(), 
        self.apellido.get())) 
        self.close()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()