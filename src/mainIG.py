import sys

from PySide6.QtWidgets import QApplication

from src.UI.controlador import MainWindowController

app = QApplication([])
vtnSistemaActividad = MainWindowController()
vtnSistemaActividad.show()
sys.exit(app.exec())