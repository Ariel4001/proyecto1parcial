import sys
import pyodbc as bd

class Conexion:
    """
    Clase que permite abrir conexion a la BBDD y abrir cursor.
    """
    _SERVIDOR = 'DESKTOP-HB9BQS3\\ARIELCASTRO'
    _BBDD = 'RegistroActividades'
    _USUARIO = 'SistemaActividadesEstudiantiles'
    _PASSWORD = '1234'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        """
        Obtiene la conexion a la BBDD con los parametros de conexion pasados como constantes
        :return:
        """
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                           cls._SERVIDOR + ';DATABASE=' + cls._BBDD + ';UID=' + cls._USUARIO + ';PWD=' + cls._PASSWORD
                                           + ';TrustServerCertificate=yes')
                print(f'Conexión exitosa: {cls._conexion}') # Añadido para depuración
                return cls._conexion
            except Exception as e:
                print(f'Ocurrió una excepción al obtener la conexión: {e}') # Mensaje más claro
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        """
        Obtiene el cursor que
        :return:
        """
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                print(f'Se abrió correctamente el cursor: {cls._cursor}') # Añadido para depuración
                return cls._cursor
            except Exception as e:
                print(f'Ocurrió una excepción al obtener el cursor: {e}') # Mensaje más claro
                sys.exit()
        else:
            return cls._cursor


if __name__ == '__main__':
    print(Conexion.obtenerConexion())
    print(Conexion.obtenerCursor())