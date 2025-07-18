from PySide6.QtCore import QDateTime, QDate, QLocale
from PySide6.QtGui import QIntValidator, QDoubleValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from src.UI.vtnSistemaActividad import Ui_vtnSistemaActividad
from src.datos.estudianteDao import EstudianteDao
from src.dominio.estu import Estudiante


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_vtnSistemaActividad()
        self.ui.setupUi(self)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnBuscar.clicked.connect(self.buscar)
        self.ui.btnActualizar.clicked.connect(self.actualizar)
        self.ui.btnEliminar.clicked.connect(self.eliminar)
        self.ui.txtCedula.setValidator(QIntValidator())
        self.ui.txtBuscar.setValidator(QIntValidator())
        duracion_validator = QDoubleValidator()
        duracion_validator.setLocale(QLocale(QLocale.Language.English, QLocale.Country.UnitedStates))
        duracion_validator.setRange(0.0, 1000.0)
        duracion_validator.setDecimals(2)
        self.ui.txtDuracion.setValidator(duracion_validator)


    def buscar(self):
        if len(self.ui.txtBuscar.text().strip()) < 10:
            QMessageBox.warning(self, "Advertencia", "Ingrese la cedula a buscar correctamente.")
        else:
            estudiante = EstudianteDao.seleccionar_persona(self.ui.txtBuscar.text().strip())
            if estudiante:
                self.ui.txtNombre.setText(estudiante.nombre)
                self.ui.txtCedula.setText(estudiante.cedula)
                fecha_qdate = QDate.fromString(estudiante.fecha, "yyyy-MM-dd")
                if fecha_qdate.isValid():
                    self.ui.dtFecha.setDate(fecha_qdate)
                self.ui.txtDuracion.setText(str(estudiante.duracion))
                self.ui.txtMatricula.setText(estudiante.matricula)
                self.ui.txtCarrera.setText(estudiante.carrera)
                self.ui.cbTipoactividad.setCurrentText(estudiante.tipo_actividad)
            else:
                #print("No se encontro la persona.")
                QMessageBox.information(self, "Advertencia", "No se encontro la persona con la cedula.")


    def guardar(self):
        nombre = self.ui.txtNombre.text().strip()
        cedula = self.ui.txtCedula.text().strip()
        fecha_seleccionada_qdate = self.ui.dtFecha.date()
        fecha_para_db = fecha_seleccionada_qdate.toString("yyyy/MM/dd")
        duracion_str = self.ui.txtDuracion.text().replace(',', '.')
        try:
            duracion = float(duracion_str)
        except ValueError:
            QMessageBox.warning(self, "Error de Entrada", "Ingrese correctamente los datos, o no deje un campo vacio.")
            return
        matricula = self.ui.txtMatricula.text().strip()
        carrera = self.ui.txtCarrera.text().strip()
        tipo_actividad = self.ui.cbTipoactividad.currentText()

        fecha_actual = QDate.currentDate()
        limite_inferior_fecha = QDate(2020, 1, 1)

        # print(f"DEBUG - Tipo Duracion ANTES de DAO: {type(duracion)} - {duracion}")
        # print("--- DEBUG - Tipos y Valores de Parámetros antes del DAO ---")
        # print(f"Nombre:           Tipo={type(nombre)}, Valor='{nombre}'")
        # print(f"Cedula:           Tipo={type(cedula)}, Valor='{cedula}'")
        # print(f"Fecha:            Tipo={type(fecha_seleccionada_qdate)}, Valor='{fecha_seleccionada_qdate}'")
        # print(f"Duracion:         Tipo={type(duracion)}, Valor={duracion}")  # duracion debería ser float aquí
        # print(f"Matricula:        Tipo={type(matricula)}, Valor='{matricula}'")
        # print(f"Carrera:          Tipo={type(carrera)}, Valor='{carrera}'")
        # print(f"Tipo Actividad:   Tipo={type(tipo_actividad)}, Valor='{tipo_actividad}'")
        # print(f"DEBUG VALIDACION - Tipo fecha_seleccionada_qdate: {type(fecha_seleccionada_qdate)}, Valor: {fecha_seleccionada_qdate}")
        # print(f"DEBUG VALIDACION - Tipo fecha_actual: {type(fecha_actual)}, Valor: {fecha_actual}")
        # print(f"DEBUG VALIDACION - Tipo limite_inferior_fecha: {type(limite_inferior_fecha)}, Valor: {limite_inferior_fecha}")


        if nombre == "" or len(cedula) < 10 or \
            fecha_seleccionada_qdate > fecha_actual or fecha_seleccionada_qdate < limite_inferior_fecha or\
            duracion <= 0 or matricula == "" or carrera == "" or tipo_actividad == "Seleccionar":
            QMessageBox.warning(self, "Advertencia", "Complete los datos correctamente.\n"
                                                     "O llene los campos correctamente.")
        else:
            estudiante = Estudiante(
                nombre= nombre,
                cedula = cedula,
                fecha = fecha_para_db,
                duracion = duracion,
                matricula = matricula,
                carrera = carrera,
                tipo_actividad = tipo_actividad
            )
            if EstudianteDao.insertar_persona(estudiante) == -1:
                QMessageBox.critical(self, "Error", "No se pudo guardar el estudiante.")
                #print(estudiante)
            else:
                QMessageBox.information(self, "Registro con exito", "El registro se guardo correctamente.")
                self.ui.statusbar.showMessage('GRACIAS POR USAR NUESTRO SISTEMA', 5000)
                self.limpiar()



    def limpiar(self):
        self.ui.txtBuscar.clear()
        self.ui.txtNombre.clear()
        self.ui.txtCedula.clear()
        self.ui.txtMatricula.clear()
        self.ui.dtFecha.setDateTime(QDateTime.currentDateTime())
        self.ui.txtDuracion.clear()
        self.ui.txtCarrera.clear()
        self.ui.cbTipoactividad.setCurrentIndex(0)


    def actualizar(self):
        nombre = self.ui.txtNombre.text().strip()
        cedula = self.ui.txtCedula.text().strip()
        fecha_seleccionada_qdate = self.ui.dtFecha.date()
        fecha_para_db = fecha_seleccionada_qdate.toString("yyyy/MM/dd")
        duracion_str = self.ui.txtDuracion.text().replace(',', '.')
        try:
            duracion = float(duracion_str)
        except ValueError:
            QMessageBox.warning(self, "Error de Entrada", "La duración no es un número válido.")
            return
        matricula = self.ui.txtMatricula.text().strip()
        carrera = self.ui.txtCarrera.text().strip()
        tipo_actividad = self.ui.cbTipoactividad.currentText()

        fecha_actual = QDate.currentDate()
        limite_inferior_fecha = QDate(2020, 1, 1)
        if QMessageBox.question(self, 'Confirmación', "Desea actualizar el registro?") == QMessageBox.Yes:
            if nombre == "" or len(cedula) < 10 or \
                    fecha_seleccionada_qdate > fecha_actual or fecha_seleccionada_qdate < limite_inferior_fecha or \
                    duracion <= 0 or matricula == "" or carrera == "" or tipo_actividad == "Seleccionar":
                QMessageBox.warning(self, "Advertencia", "Complete los datos correctamente.\n"
                                                         "O llene los campos correctamente.")
            else:
                estudiante = Estudiante(
                    nombre=nombre,
                    cedula=cedula,
                    fecha=fecha_para_db,
                    duracion=duracion,
                    matricula=matricula,
                    carrera=carrera,
                    tipo_actividad=tipo_actividad
                )
                if EstudianteDao.actualizar_persona(estudiante) == -1:
                    QMessageBox.critical(self, "Error", "No se pudo guardar el estudiante.")
                    # print(estudiante)
                else:
                    QMessageBox.information(self, "Informacion", "Se actualizo el estudiante correctamente.")
                    self.ui.statusbar.showMessage('GRACIAS POR USAR NUESTRO SISTEMA', 5000)
                    self.limpiar()



    def eliminar(self):
        cedula = self.ui.txtCedula.text().strip()
        if QMessageBox.question(self, "Confirmación", "Desea borrar el registro.") == QMessageBox.Yes:
            retorno = EstudianteDao.eliminar_persona(cedula)
            if retorno != -1:
                QMessageBox.information(self, "Informacion", "Registro eliminado exitosamente.")
                self.ui.statusbar.showMessage("Registro eliminado con éxito", 5000)
                self.limpiar()
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar.")




