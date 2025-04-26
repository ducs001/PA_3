import rx
from rx import operators as ops

class SistemaEventos:
    def __init__(self):
        self.eventos=rx.subject.Subject()
    def suscribir(self,observador):
        self.eventos.subscribe(lambda e: observador.actualizar(e))

    def emitir_evento(self,evento):
        self.eventos.on_next(evento)

