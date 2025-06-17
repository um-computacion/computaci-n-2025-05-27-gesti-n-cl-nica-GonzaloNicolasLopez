from datetime import datetime
from src.paciente import Paciente
from src.medico import Medico

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        if paciente is None:
            raise ValueError("El paciente no debe ser Nulo.")
        if medico is None:
            raise ValueError("El médico no debe ser Nulo.")
        if fecha_hora is None:
            raise ValueError("no puede ser nula la fecha y hora.")
        if not especialidad.strip():
            raise ValueError("no puede estar vacia la especialidad.")

        self.paciente: Paciente = paciente
        self.medico: Medico = medico
        self.fecha_hora: datetime = fecha_hora
        self.especialidad: str = especialidad

    def obtener_medico(self) -> Medico:
        return self.medico

    def obtener_fecha_hora(self) -> datetime:
        return self.fecha_hora

    def __str__(self) -> str:
        f = self.fecha_hora.strftime("%d/%m/%Y %H:%M")
        return (f"Turno - {self.paciente.obtener_dni()} con "
                f"{self.medico.obtener_matricula()} el {f} "
                f"({self.especialidad})")
