import asyncio
import random
from eventos.evento import EventoAsistencia
async def simular_eventos(sistema,empleados):
    while True:
        empleado = random.choice(empleados)
        tipo_evento = random.choice(["entrada","salida"])
        evento = EventoAsistencia(empleado,tipo_evento)
        sistema.emitir_evento(evento)
        await asyncio.sleep(random.randint(2,5))

