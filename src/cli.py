import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.clinica import (
    Clinica, 
    PacienteNoEncontradoException, 
    MedicoNoDisponibleException, 
    TurnoOcupadoException, 
    RecetaInvalidaException
)
from src.paciente import Paciente
from src.medico import Medico
from src.especialidad import Especialidad
from datetime import datetime


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresione ENTER para continuar...")

class CLI:
    def __init__(self):
        self.clinica = Clinica()

    def mostrar_menu(self):
        print("\n" + "="*40)
        print("   CLÍNICA")
        print("="*40)
        print("1) Agregar paciente")
        print("2) Agregar médico")
        print("3) Agregar especialidad a médico")
        print("4) Agendar turno")
        print("5) Emitir receta")
        print("6) Ver historia clínica")
        print("7) Ver todos los turnos")
        print("8) Ver todos los pacientes")
        print("9) Ver todos los médicos")
        print("0) Salir")
        print("="*40)

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Opción: ").strip()
            limpiar_pantalla()
            try:
                if opcion == "1":
                    self._op_agregar_paciente()
                elif opcion == "2":
                    self._op_agregar_medico()
                elif opcion == "3":
                    self._op_agregar_especialidad()
                elif opcion == "4":
                    self._op_agendar_turno()
                elif opcion == "5":
                    self._op_emitir_receta()
                elif opcion == "6":
                    self._op_ver_historia()
                elif opcion == "7":
                    self._op_ver_turnos()
                elif opcion == "8":
                    self._op_ver_pacientes()
                elif opcion == "9":
                    self._op_ver_medicos()
                elif opcion == "0":
                    print("saliendo del sistema")
                    break
                else:
                    print("Opción inválida.")
            except (ValueError,
                    PacienteNoEncontradoException,
                    MedicoNoDisponibleException,
                    TurnoOcupadoException,
                    RecetaInvalidaException) as e:
                print(f"Error: {e}")
            pausar()

    def _op_agregar_paciente(self):
        dni = input("DNI: ").strip()
        nombre = input("Nombre y Apellido: ").strip()
        fn = input("Fecha nacimiento (dd/mm/aaaa): ").strip()
        p = Paciente(dni, nombre, fn)
        self.clinica.agregar_paciente(p)
        print("Paciente registrado.")

    def _op_agregar_medico(self):
        mat = input("Matrícula: ").strip()
        nombre = input("Nombre y Apellido: ").strip()
        m = Medico(mat, nombre)
        self.clinica.agregar_medico(m)
        print("Médico registrado.")

    def _op_agregar_especialidad(self):
        mat = input("Matrícula del médico: ").strip()
        medico = self.clinica.obtener_medico_por_matricula(mat)
        tipo = input("Tipo de especialidad: ").strip()
        dias = [d.strip() for d in input("Días : ").split(",")]
        esp = Especialidad(tipo, dias)
        medico.agregar_especialidad(esp)
        print("Especialidad registrada.")

    def _op_agendar_turno(self):
        dni = input("DNI del paciente: ").strip()
        mat = input("Matrícula del médico: ").strip()
        fecha = input("Fecha (dd/mm/aaaa): ").strip()
        hora = input("Hora (HH:MM): ").strip()

        try:
            dt = datetime.strptime(f"{fecha} {hora}", "%d/%m/%Y %H:%M")
        except ValueError:
            print("Fecha o hora inválida. Usá el formato dd/mm/aaaa y HH:MM.")
            return
        esp = input("Especialidad: ").strip()
        self.clinica.agendar_turno(dni, mat, dt, esp)
        print("Turno anotado.")

    def _op_emitir_receta(self):
        dni = input("DNI del paciente: ").strip()
        mat = input("Matrícula del médico: ").strip()
        meds = [m.strip() for m in input("Medicamentos: ").split(",") if m.strip()]
        self.clinica.emitir_receta(dni, mat, meds)
        print("Receta finalizada.")

    def _op_ver_historia(self):
        dni = input("DNI paciente: ").strip()
        historia = self.clinica.obtener_historia_clinica_por_dni(dni)
        print(historia)

    def _op_ver_turnos(self):
        turnos = self.clinica.obtener_turnos()
        if not turnos:
            print("No se discpone turnos agendados.")
        else:
            for t in turnos:
                print(t)

    def _op_ver_pacientes(self):
        pacientes = self.clinica.obtener_pacientes()
        if not pacientes:
            print("No se encuentran pacientes registrados.")
        else:
            for p in pacientes:
                print(p)

    def _op_ver_medicos(self):
        medicos = self.clinica.obtener_medicos()
        if not medicos:
            print("No se encuentran médicos registrados.")
        else:
            for m in medicos:
                print(m)

if __name__ == "__main__":
    CLI().ejecutar()