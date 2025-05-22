# actividad_academica.py
# Miembros del grupo:
# * CASTRO PILAY ARIEL ANDRES
# * OLLOA ARBOLEDA JORGE LUIS
# * CERVANTES MENENDEZ ALISSON DANIELA
# * TRIVIÑO TORRES LAILA DANYELA

from src.actividades import Actividad

class ActividadAcademica(Actividad):
    """
    Subclase de Actividad que representa una actividad académica.
    Añade atributos como tema, ponente y modalidad.
    """

    def __init__(self, nombre, fecha, duracion, tema, ponente, modalidad):
        super().__init__(nombre, fecha, duracion)
        self._tema = tema
        self._ponente = ponente
        self._modalidad = modalidad

    # Getter y Setter para tema
    @property
    def tema(self):
        return self._tema

    @tema.setter
    def tema(self, valor):
        self._tema = valor

    # Getter y Setter para ponente
    @property
    def ponente(self):
        return self._ponente

    @ponente.setter
    def ponente(self, valor):
        self._ponente = valor

    # Getter y Setter para modalidad
    @property
    def modalidad(self):
        return self._modalidad

    @modalidad.setter
    def modalidad(self, valor):
        self._modalidad = valor

    def generar_reporte(self):
        """
        Genera un reporte específico para actividades académicas.
        """
        return (f"📚 Actividad Académica: {self.nombre}\n"
                f"📅 Fecha: {self.fecha}\n"
                f"⏱️ Duración: {self.duracion} horas\n"
                f"📖 Tema: {self.tema}\n"
                f"👨‍🏫 Ponente: {self.ponente}\n"
                f"💻 Modalidad: {self.modalidad}")
