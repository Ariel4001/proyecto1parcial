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

    def __init__(self, nombre,cedula, fecha, duracion, matricula, carrera, tipo_actividad):
        self._nombre = nombre
        self._cedula = cedula
        self._fecha = fecha
        self._duracion = duracion
        self._matricula = matricula
        self._carrera = carrera
        self._tipo_actividad = tipo_actividad
        self._actividades = []

    # Getters y Setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def fecha(self):
        return self._fecha
    @fecha.setter
    def fecha (self, valor):
        self._fecha = valor

    @property
    def duracion (self):
        return self._duracion

    @duracion.setter
    def duracion(self, valor):
        self._duracion = valor

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self,valor):
        self._cedula = valor

    @property
    def tipo_actividad(self):
        return self._tipo_actividad

    @tipo_actividad.setter
    def tipo_actividad(self, valor):
        self._tipo_actividad = valor

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

    def __str__(self):
        return (f"Estudiante: {self._nombre}\n"
                f"Cédula: {self._cedula}\n"
                f"Fecha: {self._fecha}\n"
                f"Duración: {self._duracion} hrs\n"
                f"Matrícula: {self._matricula}\n"
                f"Carrera: {self._carrera}\n"
                f"Tipo de Actividad: {self._tipo_actividad}")

    # def agregar_actividad(self, actividad):
    #     """
    #     Agrega una actividad a la lista del estudiante.
    #     """
    #     self._actividades.append(actividad)
    #
    # def generar_certificado(self):
    #     """
    #     Genera un certificado con todas las actividades del estudiante.
    #     """
    #     print("=" * 60)
    #     print("CERTIFICADO DE PARTICIPACIÓN".center(60))
    #     print("=" * 60)
    #     print(f"Nombre del Estudiante: {self.nombre}")
    #     print(f"Matrícula: {self.matricula}")
    #     print(f"Carrera: {self.carrera}")
    #     print("-" * 60)
    #     print("Actividades Registradas:".center(60))
    #     print("-" * 60)
    #
    #     if not self._actividades:
    #         print("No se han registrado actividades.".center(60))
    #     else:
    #         for i, actividad in enumerate(self._actividades, start=1):
    #             print(f"\nActividad #{i}".center(60))
    #             print(actividad.generar_reporte().center(60))
    #
    #     print("\n" + "=" * 60)
    #     print("Gracias por tu participación".center(60))
    #     print("=" * 60)


# Prueba individual
# if __name__ == "__main__":
# #     from src.dominio.deportiva import ActividadDeportiva
# #
# #     futbol = ActividadDeportiva("Torneo de Fútbol", "2025-04-10", 2, "Fútbol")
# #     estudiante = Estudiante("Carlos Pérez", "20231234", "Ingeniería en Sistemas")
# #     estudiante.agregar_actividad(futbol)
# #     estudiante.generar_certificado()


