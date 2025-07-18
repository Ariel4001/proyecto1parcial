from src.datos.conexion import Conexion
from src.dominio.estu import Estudiante


class EstudianteDao:
    _ERROR = -1
    _INSERT = ("INSERT INTO Estudiantes (nombre, cedula, fecha, duracion_actividad,"
               "matricula, carrera, tipo_actividad) "
               "VALUES (?,?,?,?,?,?,?)")

    _SELECT = ("SELECT nombre, cedula, fecha, duracion_actividad, matricula,"
               "carrera, tipo_actividad FROM Estudiantes "
               "WHERE cedula = ?")

    _UPDATE = ("UPDATE Estudiantes SET nombre = ?, cedula = ?, fecha = ?, "
               "duracion_actividad = ?, matricula = ?, carrera = ?, tipo_actividad = ? "
               "WHERE cedula = ?")

    _DELETE = ("DELETE FROM Estudiantes "
               "WHERE cedula = ?")


    @classmethod
    def insertar_persona(cls, estudiante):
        try:
            # cursor = Conexion.obtenerCursor()
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.nombre, estudiante.cedula, estudiante.fecha,
                         estudiante.duracion, estudiante.matricula, estudiante.carrera,
                         estudiante.tipo_actividad,)
                retorno = cursor.execute(cls._INSERT, datos)
                return retorno.rowcount
        except Exception as e:
            print(e)
            cursor.rollback()
            return cls._ERROR



    @classmethod
    def seleccionar_persona(cls, cedula):
        try:
            # cursor = Conexion.obtenerCursor()
            with Conexion.obtenerCursor() as cursor:
                datos = (cedula,)
                retorno = cursor.execute(cls._SELECT, datos).fetchone()
                persona = Estudiante( nombre=retorno[0],
                                      cedula=retorno[1],
                                      fecha =retorno[2],
                                      duracion = retorno[3],
                                      matricula =retorno[4],
                                      carrera = retorno [5],
                                      tipo_actividad= retorno[6])
                return persona
        except Exception as e:
            print(e)
            cursor.rollback()
            return None

    @classmethod
    def actualizar_persona(cls, estudiante):
        try:
            # cursor = Conexion.obtenerCursor()
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.nombre, estudiante.cedula, estudiante.fecha,
                         estudiante.duracion, estudiante.matricula, estudiante.carrera
                         ,estudiante.tipo_actividad,estudiante.cedula,)
                retorno = cursor.execute(cls._UPDATE, datos)
                return retorno.rowcount
        except Exception as e:
            print(e)
            cursor.rollback()
            return cls._ERROR


    @classmethod
    def eliminar_persona(cls, cedula):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (cedula,)
                retorno = cursor.execute(cls._DELETE, datos)
                return retorno.rowcount
        except Exception as e:
            print(e)
            cursor.rollback()
            return cls._ERROR


if __name__ == "__main__":
    est1= Estudiante("Jemina suarez", "0123456789", "13/05/2024",
                   2.5 , "2222-2222", "GIG",
                   "deportiva")
    estudiante = EstudianteDao.insertar_persona(est1)
    print("estudiante agregado correctamente")
    print(estudiante)




