# actividad_deportiva.py
# Miembros del grupo:
# * CASTRO PILAY ARIEL ANDRES
# * OLLOA ARBOLEDA JORGE LUIS
# * CERVANTES MENENDEZ ALISSON DANIELA
# * TRIVIÑO TORRES LAILA DANYELA

from src.dominio.actividades import Actividad

class ActividadDeportiva(Actividad):
    """
    Subclase de Actividad que representa una actividad deportiva.
    Añade el atributo 'disciplina' y sobrescribe el método generar reporte().
    """

    def __init__(self, nombre, fecha, duracion, disciplina):
        super().__init__(nombre, fecha, duracion)
        self._disciplina = disciplina

    # Getter y Setter para disciplina
    @property
    def disciplina(self):
        return self._disciplina

    @disciplina.setter
    def disciplina(self, valor):
        self._disciplina = valor

    def generar_reporte(self):
        """
        Genera un reporte específico para actividades deportivas.
        """
        return (f"🏅 Actividad Deportiva: {self.nombre}\n"
                f"📅 Fecha: {self.fecha}\n"
                f"⏱️ Duración: {self.duracion} horas\n"
                f"⚽ Disciplina: {self.disciplina}")


# Prueba individual
if __name__ == "__main__":
    futbol = ActividadDeportiva("Torneo de Fútbol", "2025-04-10", 2, "Fútbol")
    print(futbol.generar_reporte())
