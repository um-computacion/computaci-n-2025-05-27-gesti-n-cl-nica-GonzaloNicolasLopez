Cómo ejecutar el sistema.
Primero clonamos el repositorio
segundo entramos al repositorio
tercero creamos una carpeta src y una carpeta test
cuarto creamos todas las clases y el cli
quinto hacemos los test de las clases

Cómo ejecutar las pruebas.
primero abrir una terminal y entrar al directorio:
C:\Users\Home\Desktop\python\computaci-n-2025-05-27-gesti-n-cl-nica-GonzaloNicolasLopez>
segundo ejecutar los test a la vez poner:
python -m unittest
para ejecutar de a un test poner:
python -m unittest test.test_nombre_del_test
tercero verificar que todos los test corran
cuarto si algun test falla, arreglar el error

Explicación de diseño general.
Este es un sistema de gestion de una clínica que facilita las clases como turnos,pacientes,especialidades.
Este sistema usa enfoques orientados a objetos para relacionarlos con la clínica. Hay distos tipos de clases:
Turno: Nos guarda los turnos agendados con los pacientes, una hora y la fecha, el medico, una especialidad y los dias de la semana.
Receta: Nos da una receta médica que realiaza un médico para un paciente y incluye todos los medicamentados que necesita el paciente.
Paciente: Nos proporciona los datos del paciente como: DNI, el nombre y el apellido y su historial clínica.
Medico: Nos da los atributos del medico como su nombre y apellido, su matricula, sus especialidades. Podemos agregar mas especialidades y podemos corroborar que dias atiende un medico.
HistoriaClinica: Nos muestra la historia clínica de un paciente, que tienen recetas asociados y turnos.
Especialidad: Nos muestra la especilidad médica con el nombre y con los dias que atiende esa especialidad el medico.
Clinica: Es la clase principal que dirige médicos,recetas y turnos. Nos muestra los metodos para agregar médicos y pacientes, emitir recetas, agendar turnos y para obtener historias clinicas.
CLI: Permite que los usuarios puedan interactuar con la clinica a traves de la interfaz con las diferentes lineas del comando. El CLI nos da opcines para agendar turnos,agregar medicos, agregar pacientes, ver historias clinicas,pacientes,turnos,medicos registrados y emitir recetas.
Este sistema permite que podamos agregar nuevas funcionalidades sin dañar la estructura que este vigente, tambien implementamos validaciones para evitar duplicados de medicos y de pacientes.
Cada clase tiene sus respectivos test para poder verificar los funcionamientos de los metodos, verificando que se cumplan todos los requisitos.
