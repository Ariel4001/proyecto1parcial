# estudiante.py
# Miembros del grupo:
# * CASTRO PILAY ARIEL ANDRES
# * OLLOA ARBOLEDA JORGE LUIS
# * CERVANTES MENENDEZ ALISSON DANIELA
# * TRIVIÑO TORRES LAILA DANYELA

class Estudiante:
    """
    Clase que representa a un estudiante y su participación en actividades extracurriculares.
    Permite registrar actividades y generar un certificado de participación.
    """

    def __init__(self, nombre, matricula, carrera):
        self._nombre = nombre
        self._matricula = matricula
        self._carrera = carrera
        self._actividades = []

    # Getters y Setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, valor):
        self._matricula = valor

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, valor):
        self._carrera = valor

    def agregar_actividad(self, actividad):
        """
        Agrega una actividad a la lista del estudiante.
        """
        self._actividades.append(actividad)

    def generar_certificado(self):
        """
        Genera un certificado con todas las actividades del estudiante.
        """
        print("=" * 60)
        print("CERTIFICADO DE PARTICIPACIÓN".center(60))
        print("=" * 60)
        print(f"Nombre del Estudiante: {self.nombre}")
        print(f"Matrícula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
        print("-" * 60)
        print("Actividades Registradas:".center(60))
        print("-" * 60)

        if not self._actividades:
            print("No se han registrado actividades.".center(60))
        else:
            for i, actividad in enumerate(self._actividades, start=1):
                print(f"\nActividad #{i}".center(60))
                print(actividad.generar_reporte().center(60))

        print("\n" + "=" * 60)
        print("Gracias por tu participación".center(60))
        print("=" * 60)


# Prueba individual
if __name__ == "__main__":
    from deportiva import ActividadDeportiva

    futbol = ActividadDeportiva("Torneo de Fútbol", "2025-04-10", 2, "Fútbol")
    estudiante = Estudiante("Carlos Pérez", "20231234", "Ingeniería en Sistemas")
    estudiante.agregar_actividad(futbol)
    estudiante.generar_certificado()

