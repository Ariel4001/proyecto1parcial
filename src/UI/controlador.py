from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem
from PySide6.QtCore import QDate, Qt

# Importa la interfaz generada por Qt Designer
from src.UI.vtnSistemaActividad import Ui_MainWindow

# Importa la lógica de negocio y las excepciones de validación
from src.servicio.sistema_actividades import SistemaActividades, ValidacionError

class MainWindowController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Inicializa la instancia del sistema de actividades
        self.sistema = SistemaActividades()

        # --- Conexiones de Botones y Eventos ---

        # Pestaña "Datos del Estudiante" - (Para simplificar, el estudiante se intentará registrar al agregar actividad)
        # Podrías añadir un botón específico "Guardar Datos Estudiante" y conectarlo aquí si lo prefieres.

        # Pestaña "Registro de Actividades"
        self.ui.deportivaRadio.toggled.connect(self._actualizar_info_especifica)
        self.ui.culturalRadio.toggled.connect(self._actualizar_info_especifica)
        self.ui.academicaRadio.toggled.connect(self._actualizar_info_especifica)

        self.ui.addActivityButton.clicked.connect(self._agregar_actividad)
        self.ui.clearFormButton.clicked.connect(self._limpiar_formulario_actividad)

        # Pestaña "Lista de Actividades"
        self.ui.removeActivityButton.clicked.connect(self._eliminar_actividad)
        self.ui.generateCertificateButton.clicked.connect(self._generar_certificado)

        # Pestaña "Certificado" (Botones para guardar/imprimir - funcionalidad avanzada, aquí solo placeholder)
        self.ui.saveCertificateButton.clicked.connect(self._guardar_certificado)
        self.ui.printCertificateButton.clicked.connect(self._imprimir_certificado)

        # Conexiones de menú (ejemplo: Salir)
        self.ui.actionSalir.triggered.connect(self.close)
        self.ui.actionAcerca_de.triggered.connect(self._mostrar_acerca_de)

        # Inicializa la interfaz
        self._actualizar_info_especifica() # Asegura que la página correcta se muestre al inicio
        self._actualizar_lista_actividades() # Carga actividades si ya hay algunas (útil si se carga desde persistencia)


    # --- Métodos de Ayuda para la UI ---

    def _mostrar_mensaje(self, titulo, mensaje, tipo="informacion"):
        """Muestra un QMessageBox al usuario."""
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(titulo)
        msg_box.setText(mensaje)
        if tipo == "error":
            msg_box.setIcon(QMessageBox.Icon.Critical)
        elif tipo == "advertencia":
            msg_box.setIcon(QMessageBox.Icon.Warning)
        else: # informacion
            msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.exec()

    def _limpiar_formulario_actividad(self):
        """Limpia todos los campos del formulario de registro de actividades."""
        self.ui.activityNameLineEdit.clear()
        self.ui.fechaDateEdit.setDate(QDate.currentDate()) # Restablece a la fecha actual
        self.ui.duracionSpinBox.setValue(1.0) # Restablece a un valor predeterminado

        # Limpiar campos específicos de cada tipo
        self.ui.disciplinaLineEdit.clear()
        self.ui.tipoEventoLineEdit.clear()
        self.ui.lugarLineEdit.clear()
        self.ui.organizadorLineEdit.clear()
        self.ui.temaLineEdit.clear()
        self.ui.ponenteLineEdit.clear()
        self.ui.modalidadComboBox.setCurrentIndex(0) # Restablece a la primera opción

        # Restablecer la selección de radio button a "Deportiva"
        self.ui.deportivaRadio.setChecked(True)
        self.ui.tabWidget.setCurrentIndex(1) # Vuelve a la pestaña de registro

    def _actualizar_info_especifica(self):
        """Cambia la página del QStackedWidget según el radio button seleccionado."""
        if self.ui.deportivaRadio.isChecked():
            self.ui.specificInfoStack.setCurrentIndex(0) # Página deportiva
        elif self.ui.culturalRadio.isChecked():
            self.ui.specificInfoStack.setCurrentIndex(1) # Página cultural
        elif self.ui.academicaRadio.isChecked():
            self.ui.specificInfoStack.setCurrentIndex(2) # Página académica

    def _actualizar_lista_actividades(self):
        """Actualiza el QListWidget con las actividades registradas."""
        self.ui.activitiesListWidget.clear()
        actividades = self.sistema.obtener_actividades()
        for i, actividad in enumerate(actividades):
            # Muestra el nombre de la actividad y su tipo
            item_text = f"{i+1}. {actividad.nombre} ({actividad.__class__.__name__.replace('Actividad', '')})"
            self.ui.activitiesListWidget.addItem(item_text)

    # --- Métodos de Conexión a la Lógica de Negocio (SistemaActividades) ---

    def _registrar_estudiante_en_ui(self):
        """
        Intenta registrar o actualizar la información del estudiante desde la UI.
        Retorna True si el estudiante se registró/validó exitosamente, False en caso contrario.
        """
        nombre = self.ui.nameLineEdit.text().strip()
        matricula = self.ui.matriculaLineEdit.text().strip()
        carrera = self.ui.carreraLineEdit.text().strip()

        try:
            self.sistema.registrar_estudiante(nombre, matricula, carrera)
            # No se muestra un mensaje de éxito aquí, ya que se asocia más a la acción de agregar actividad
            return True
        except ValidacionError as e:
            self._mostrar_mensaje("Error de Validación de Estudiante", str(e), "error")
            self.ui.tabWidget.setCurrentIndex(0) # Lleva al usuario a la pestaña del estudiante
            return False

    def _agregar_actividad(self):
        """
        Recoge los datos del formulario de actividades, los valida y los agrega al sistema.
        """
        if not self._registrar_estudiante_en_ui():
            # Si la validación del estudiante falla, detener la adición de actividad
            return

        tipo_actividad = ""
        if self.ui.deportivaRadio.isChecked():
            tipo_actividad = "Deportiva"
        elif self.ui.culturalRadio.isChecked():
            tipo_actividad = "Cultural"
        elif self.ui.academicaRadio.isChecked():
            tipo_actividad = "Académica"

        nombre_actividad = self.ui.activityNameLineEdit.text().strip()
        fecha_qdate = self.ui.fechaDateEdit.date()
        duracion = self.ui.duracionSpinBox.value()

        kwargs = {}
        if tipo_actividad == "Deportiva":
            kwargs['disciplina'] = self.ui.disciplinaLineEdit.text().strip()
        elif tipo_actividad == "Cultural":
            kwargs['tipo_evento'] = self.ui.tipoEventoLineEdit.text().strip()
            kwargs['lugar'] = self.ui.lugarLineEdit.text().strip()
            kwargs['organizador'] = self.ui.organizadorLineEdit.text().strip()
        elif tipo_actividad == "Académica":
            kwargs['tema'] = self.ui.temaLineEdit.text().strip()
            kwargs['ponente'] = self.ui.ponenteLineEdit.text().strip()
            kwargs['modalidad'] = self.ui.modalidadComboBox.currentText()

        try:
            self.sistema.agregar_actividad(
                tipo_actividad, nombre_actividad, fecha_qdate, duracion, **kwargs
            )
            self._mostrar_mensaje("Éxito", "Actividad agregada correctamente.", "informacion")
            self._limpiar_formulario_actividad()
            self._actualizar_lista_actividades()
            self.ui.tabWidget.setCurrentIndex(2) # Cambiar a la pestaña de lista de actividades
        except ValidacionError as e:
            self._mostrar_mensaje("Error de Validación", str(e), "error")
        except Exception as e:
            self._mostrar_mensaje("Error Inesperado", f"Ocurrió un error: {str(e)}", "error")

    def _eliminar_actividad(self):
        """Elimina la actividad seleccionada de la lista."""
        selected_row = self.ui.activitiesListWidget.currentRow()
        if selected_row == -1:
            self._mostrar_mensaje("Advertencia", "Por favor, seleccione una actividad para eliminar.", "advertencia")
            return

        try:
            self.sistema.eliminar_actividad(selected_row)
            self._mostrar_mensaje("Éxito", "Actividad eliminada correctamente.", "informacion")
            self._actualizar_lista_actividades()
            self.ui.certificateTextEdit.clear() # Limpiar certificado si estaba mostrando una actividad eliminada
        except ValidacionError as e:
            self._mostrar_mensaje("Error al Eliminar", str(e), "error")
        except Exception as e:
            self._mostrar_mensaje("Error Inesperado", f"Ocurrió un error: {str(e)}", "error")

    def _generar_certificado(self):
        """Genera y muestra el certificado de la actividad seleccionada."""
        selected_row = self.ui.activitiesListWidget.currentRow()
        if selected_row == -1:
            self._mostrar_mensaje("Advertencia", "Por favor, seleccione una actividad para generar el certificado.", "advertencia")
            return

        try:
            certificado_texto = self.sistema.generar_certificado(selected_row)
            self.ui.certificateTextEdit.setText(certificado_texto)
            self.ui.tabWidget.setCurrentIndex(3) # Cambiar a la pestaña de certificado
            self._mostrar_mensaje("Éxito", "Certificado generado correctamente.", "informacion")
        except ValidacionError as e:
            self._mostrar_mensaje("Error al Generar Certificado", str(e), "error")
        except Exception as e:
            self._mostrar_mensaje("Error Inesperado", f"Ocurrió un error: {str(e)}", "error")

    def _guardar_certificado(self):
        """Placeholder para la funcionalidad de guardar certificado."""
        self._mostrar_mensaje("Funcionalidad Pendiente", "La función de 'Guardar Certificado' aún no está implementada.", "informacion")

    def _imprimir_certificado(self):
        """Placeholder para la funcionalidad de imprimir certificado."""
        self._mostrar_mensaje("Funcionalidad Pendiente", "La función de 'Imprimir Certificado' aún no está implementada.", "informacion")

    def _mostrar_acerca_de(self):
        """Muestra un cuadro de diálogo 'Acerca de'."""
        self._mostrar_mensaje("Acerca de Sistema de Gestión de Actividades Extracurriculares",
                              "Versión 1.0\n\nDesarrollado con PySide6 y la ayuda de Gemini.", "informacion")


