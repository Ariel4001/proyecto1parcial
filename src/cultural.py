# actividad_cultural.py
# Miembros del grupo:
# * CASTRO PILAY ARIEL ANDRES
# * OLLOA ARBOLEDA JORGE LUIS
# * CERVANTES MENENDEZ ALISSON DANIELA
# * TRIVIÑO TORRES LAILA DANYELA

from src.actividades import Actividad

class ActividadCultural(Actividad):
    """
    Subclase de Actividad que representa una actividad cultural.
    Añade atributos como tipo de evento, lugar y organizador.
    """

    def __init__(self, nombre, fecha, duracion, tipo_evento, lugar, organizador):
        super().__init__(nombre, fecha, duracion)
        self._tipo_evento = tipo_evento
        self._lugar = lugar
        self._organizador = organizador

    # Getter y Setter para tipo_evento
    @property
    def tipo_evento(self):
        return self._tipo_evento

    @tipo_evento.setter
    def tipo_evento(self, valor):
        self._tipo_evento = valor

    # Getter y Setter para lugar
    @property
    def lugar(self):
        return self._lugar

    @lugar.setter
    def lugar(self, valor):
        self._lugar = valor

    # Getter y Setter para organizador
    @property
    def organizador(self):
        return self._organizador

    @organizador.setter
    def organizador(self, valor):
        self._organizador = valor

    def generar_reporte(self):
        """
        Genera un reporte específico para actividades culturales.
        """
        return (f"🎭 Actividad Cultural: {self.nombre}\n"
                f"📅 Fecha: {self.fecha}\n"
                f"⏱️ Duración: {self.duracion} horas\n"
                f"🎨 Tipo de Evento: {self.tipo_evento}\n"
                f"📍 Lugar: {self.lugar}\n"
                f"👤 Organizador: {self.organizador}")
