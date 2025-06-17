from typing import List, Optional
from src.especialidad import Especialidad


class Medico:
    def __init__(self, matricula: str, nombre: str, especialidades: Optional[List[Especialidad]] = None):
        if not matricula.strip():
            raise ValueError("La matrícula tiene que estar vacía.")
        if not nombre.strip():
            raise ValueError("El nombre del médico tiene que  estar vacío.")

        self.matricula: str = matricula
        self.nombre: str = nombre
        self.especialidades: List[Especialidad] = especialidades or []

    def agregar_especialidad(self, esp: Especialidad):
        if not isinstance(esp, Especialidad):
            raise TypeError("La especialidad debe ser instancia de Especialidad.")
        if any(e.obtener_especialidad() == esp.obtener_especialidad() for e in self.especialidades):
            raise ValueError(f"Este medico ya tiene esta especialidad: {esp.obtener_especialidad()}.")
        self.especialidades.append(esp)

    def obtener_matricula(self) -> str:
        return self.matricula

    def obtener_especialidad_para_dia(self, dia: str) -> Optional[str]:
        for e in self.especialidades:
            if e.verificar_dia(dia):
                return e.obtener_especialidad()
        return None

    def __str__(self) -> str:
        especialidades_str = "\n  ".join(str(e) for e in self.especialidades)
        return f"{self.nombre}, {self.matricula}, [\n  {especialidades_str}\n]"

