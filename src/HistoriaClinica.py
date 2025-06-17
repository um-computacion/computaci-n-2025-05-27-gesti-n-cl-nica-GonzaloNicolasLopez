from datetime import datetime
from typing import List
from src.paciente import Paciente
from src.turno import Turno
from src.receta import Receta


class HistoriaClinica:
    def __init__(self, paciente: Paciente):
        self.paciente: Paciente = paciente
        self.turnos: List[Turno] = []
        self.recetas: List[Receta] = []

    def agregar_turno(self, turno: Turno):
        if turno is None:
            raise ValueError("El turno no puede ser Nulo.")
        self.turnos.append(turno)

    def agregar_receta(self, receta: Receta):
        if receta is None:
            raise ValueError("La receta no puede ser Nulo.")
        self.recetas.append(receta)

    def obtener_turnos(self) -> List[Turno]:
        return list(self.turnos)

    def obtener_recetas(self) -> List[Receta]:
        return list(self.recetas)

    def __str__(self) -> str:
        t = "\n".join(str(x) for x in self.turnos) or "—"
        r = "\n".join(str(x) for x in self.recetas) or "—"
        return (f"Historia de {self.paciente.obtener_dni()}:\n"
                f"TURNOS:\n{t}\nRECETAS:\n{r}")