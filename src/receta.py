from datetime import datetime
from src.paciente import Paciente
from src.medico import Medico

class RecetaInvalidaException(Exception):
    pass

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str]):
        if not medicamentos:
            raise RecetaInvalidaException("Debe ingresar al menos 1 medicament.")
        self.paciente = paciente
        self.medico = medico
        self.medicamentos = medicamentos
        self.fecha = datetime.now()

    def __str__(self) -> str:
        f_str = self.fecha.strftime("%d/%m/%Y %H:%M")
        meds = ", ".join(self.medicamentos)
        return (
            f"Receta - {self.paciente.obtener_dni()} por "
            f"{self.medico.obtener_matricula()} el {f_str}: {meds}"
        )

    def obtener_paciente(self) -> Paciente:
        return self.paciente

    def obtener_medico(self) -> Medico:
        return self.medico

    def obtener_medicamentos(self) -> list[str]:
        return self.medicamentos

    def obtener_fecha(self) -> datetime:
        return self.fecha
