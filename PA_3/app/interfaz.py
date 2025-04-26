import tkinter as tk
from eventos.evento import EventoAsistencia 

class InterfazAsistencia:
    def __init__(self, root,empleados,sistema_eventos):
        self.root=root
        self.empleados = empleados
        self.sistema_eventos = sistema_eventos

        self.lista=tk.Listbox(root)

        for e in empleados:
            self.lista.insert(tk.END,e.nombre)
        self.lista.pack()

        tk.Button(root,text="Registar Entrada",command=self.entrada).pack()
        tk.Button(root,text ="Registrar Salida",command=self.salida).pack()
    def entrada(self):
        self.registrar_evento("entrada")

    def salida(self):
        self.registrar_evento("salida")

    def registrar_evento(self,tipo):
        seleccion=self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            empleado = self.empleados[index]
            evento =EventoAsistencia(empleado,tipo)
            self.sistema_eventos.emitir_evento(evento)

