# main.py
# Miembros del grupo:
# * CASTRO PILAY ARIEL ANDRES
# * OLLOA ARBOLEDA JORGE LUIS
# * CERVANTES MENENDEZ ALISSON DANIELA
# * TRIVIÑO TORRES LAILA DANYELA

from src.dominio.deportiva import ActividadDeportiva
from src.dominio.cultural import ActividadCultural
from src.dominio.academica_atr_adi import ActividadAcademica
from src.dominio.estu import Estudiante


def main():
    # Crear actividades
    futbol = ActividadDeportiva("Torneo de Fútbol", "2025-04-10", 2, "Fútbol")
    teatro = ActividadCultural("Obra de Teatro", "2025-03-15", 1.5, "Teatro", "Auditorio Central", "Club Cultural")
    seminario = ActividadAcademica("Seminario de biologia", "2025-05-05", 3, "Inteligencia Artificial", "Dra. Cervantes", "Virtual")

    # Crear estudiante
    estudiante = Estudiante("Carlos Pérez", "20231234", "Ingeniería en Sistemas")

    # Registrar actividades
    estudiante.agregar_actividad(futbol)
    estudiante.agregar_actividad(teatro)
    estudiante.agregar_actividad(seminario)

    # Generar certificado
    estudiante.generar_certificado()

if __name__ == "__main__":
    main()

