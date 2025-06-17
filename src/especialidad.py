from typing import List

class Especialidad:
    def __init__(self, tipo: str, dias: List[str]):
        if not dias:
            raise ValueError("Una especialidad tiene que tener un día consulta.")
        if not tipo.strip():
            raise ValueError("El tipo de especialidad no puede ser vacío.")
        if not dias or any(not d.strip() for d in dias):
            raise ValueError("Cada día debe tener una cadena válida no vacía.")

        self.tipo: str = tipo
        self.dias: List[str] = [d.strip().lower() for d in dias]

    def obtener_especialidad(self) -> str:
        return self.tipo

    def verificar_dia(self, dia: str) -> bool:
        return dia.strip().lower() in self.dias

    def __str__(self) -> str:
        dias_str = ", ".join(self.dias)
        return f"{self.tipo} (Días: {dias_str})"