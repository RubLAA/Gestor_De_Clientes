import csv
import config
from database import db
from tkinter.messagebox import askokcancel, WARNING

class Cliente: 
 
    def __init__(self, dni, nombre, apellido): 
        self.dni = dni 
        self.nombre = nombre 
        self.apellido = apellido 

    def __str__(self): 
        return f"({self.dni}) {self.nombre} {self.apellido}"
    
class Clientes: 
    
    # Creamos la lista y cargamos los clientes en memoria 
    lista = [] 
    with open(config.DATABASE_PATH, newline="\n") as fichero:
        reader = csv.reader(fichero, delimiter=";") 
        for dni, nombre, apellido in reader: 
            cliente = Cliente(dni, nombre, apellido) 
            lista.append(cliente) 
    
    @staticmethod 
    def buscar(dni): 
        for cliente in Clientes.lista: 
            if cliente.dni == dni: 
                return cliente 
    
    @staticmethod 
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()  # <-- Guarda en el CSV
        return cliente
    
    @staticmethod 
    def modificar(dni, nombre, apellido): 
        for i, cliente in enumerate(Clientes.lista): 
            if cliente.dni == dni: 
                Clientes.lista[i].nombre = nombre 
                Clientes.lista[i].apellido = apellido 
                Clientes.guardar() # new 
                return Clientes.lista[i]
    
    @staticmethod 
    def borrar(dni): 
        for i, cliente in enumerate(Clientes.lista): 
            if cliente.dni == dni: 
                cliente = Clientes.lista.pop(i) 
                Clientes.guardar() # new 
                return cliente 
            
    @staticmethod 
    def guardar(): 
        with open(config.DATABASE_PATH, "w", newline="\n") as fichero:  
            writer = csv.writer(fichero, delimiter=";") 
            for c in Clientes.lista: 
                writer.writerow((c.dni, c.nombre, c.apellido)) 
    
    @staticmethod
    def delete(self): 
        cliente = self.treeview.focus() 
        if cliente: 
            campos = self.treeview.item(cliente, 'values') 
            confirmar = askokcancel( 
                title='Confirmación', 
                message=f'¿Borrar a {campos[1]} {campos[2]}?', 
                icon=WARNING
                ) 
            if confirmar: 
                self.treeview.delete(cliente) 
                # !!! Borrar también en el fichero 
                db.Clientes.borrar(campos[0])

    @staticmethod
    def create_client(self): 
        self.master.treeview.insert( 
            parent='', index='end', iid=self.dni.get(), 
            values=(self.dni.get(), self.nombre.get(), 
        self.apellido.get())
        ) 
        # !!! Crear también en el fichero 
        db.Clientes.crear(
            self.dni.get(), 
            self.nombre.get(), 
            self.apellido.get()
            ) 
        self.close() 

    @staticmethod
    def update_client(self): 
        cliente = self.master.treeview.focus() 
        # Sobreescribir los datos 
        self.master.treeview.item( 
            cliente, 
            values=(self.dni.get(), 
            self.nombre.get(), 
            self.apellido.get())
            ) 
        # !!! Modificar también en el fichero 
        db.Clientes.modificar(
            self.dni.get(), 
            self.nombre.get(), 
            self.apellido.get()
            ) 
        self.close()