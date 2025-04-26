import asyncio
import tkinter as tk
import threading

from modelos.empleados import Empleado
from eventos.observables import SistemaEventos
from eventos.observadores import RegistroAsistencia,NotificadorRRHH,NotificadorSupervisor
from app.interfaz import InterfazAsistencia
from app.simulacion import simular_eventos

def main():

    #crear empleados
    empleados=[Empleado("Juan"),Empleado("Ana"),Empleado("Luis")]

    #eventos 

    sistema=SistemaEventos()
    sistema.suscribir(RegistroAsistencia())
    sistema.suscribir(NotificadorRRHH())
    sistema.suscribir(NotificadorSupervisor())

    #Iniciamos la simulacion en un hilo aparte

    def iniciar_simulacion():
        asyncio.run(simular_eventos(sistema,empleados))

    threading.Thread(target=iniciar_simulacion,daemon=True).start()

    #comenzamos la interfaz tk inter
    root=tk.Tk()
    root.title("Sistema de asistencia")
    app = InterfazAsistencia(root,empleados,sistema)
    root.mainloop()

if __name__== "__main__":
    main()
