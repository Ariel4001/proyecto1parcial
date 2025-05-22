# actividad.py
# Miembros del grupo:
# * CASTRO PILAY ARIEL ANDRES
# * OLLOA ARBOLEDA JORGE LUIS
# * CERVANTES MENENDEZ ALISSON DANIELA
# * TRIVIÑO TORRES LAILA DANYELA

from abc import ABC, abstractmethod

class Actividad(ABC):
    """
    Clase base abstracta que representa una actividad extracurricular.
    Contiene atributos comunes y un método abstracto para generar reportes.
    """

    def __init__(self, nombre, fecha, duracion):
        self._nombre = nombre
        self._fecha = fecha
        self._duracion = duracion

    # Getter y Setter para nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    # Getter y Setter para fecha
    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

    # Getter y Setter para duracion
    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, valor):
        self._duracion = valor

    @abstractmethod
    def generar_reporte(self):
        """
        Método abstracto que debe ser implementado por las subclases.
        """
        pass