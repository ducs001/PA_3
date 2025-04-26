
class RegistroAsistencia:
    def actualizar(self,evento):
        print(f"[Registro]{evento.empleado.nombre}{evento.tipo}")

class NotificadorRRHH:
    def actualizar(self,evento):
        print(f"[RRHH] Notificacion: {evento.empleado.nombre}{evento.tipo}")

class NotificadorSupervisor:
    def actualizar(self,evento):
        print(f"[Supervisor] {evento.empleado.nombre} ha {evento.tipo}")


