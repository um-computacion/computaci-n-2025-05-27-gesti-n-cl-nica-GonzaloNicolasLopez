from datetime import datetime

class Paciente:
    def __init__(self, dni: str, nombre: str, fecha_nacimiento: str):
        if not dni.strip().isdigit():
            raise ValueError("Ingrese los numeros del DNI.")

        if not nombre.strip():
            raise ValueError("Ingrese el nombre.")

        try:
            datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        except ValueError:
            raise ValueError(f"Fecha no valida : {fecha_nacimiento}. Use dd/mm/aaaa.")
        self.__dni__: str = dni
        self.__nombre__: str = nombre
        self.__fecha__nacimiento: str = fecha_nacimiento

    def obtener_dni(self) -> str:
        return self.__dni__

    def __str__(self) -> str:
        return f"{self.__nombre__} ({self.__dni__}) - Nac: {self.__fecha__nacimiento}"