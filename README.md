Se creo un proyecto en donde se simula un sistema donde los estudiantes pueden registrar actividades
extracurriculares y obtener un perfil de participación.
En cada subclase, heredando de la super clase, se puede registrar actividades de distintas tematicas.

A continuacion.
Se lo realizo de la siguiente manera:

Super clase 
Se creo una super clase llamada "Actividad", en esta se creo atributos de los cuales haremos la herencia en las subclases
La clase Actividad es una clase abstracta, lo que significa que no se puede crear un objeto directamente a partir de ella. Esto se debe a que contiene 
al menos un método marcado con @abstractmethod, en este caso generar_reporte().
Esto obliga a que todas las subclases implementen su propia versión de ese método, asegurando que cada tipo de actividad tenga su propio comportamiento específico.

si se intenta crear un objeto saldra este mensaje:

TypeError: Can't instantiate abstract class Actividad with abstract method generar_reporte

ejecucion de la super clase:
![image](https://github.com/user-attachments/assets/e62185d4-2a2d-439c-80a6-799ee3265a42)

Subclase ActidivdadDeportiva:
Representa una actividad fisica o deportiva.
* Hereda de Actividad
* Actividad adicional: disciplina
* metodo sobrescrito: generar_reportes(), muestra los detalles deportivos

ejecucion de la subclase ActividadDeportiva:
![image](https://github.com/user-attachments/assets/65b5f8a9-84e7-4476-ba60-41abec5f16f0)


Subclase ActividadCultural:
Representa una actividad artistica o cultural.
* Hereda de Actividad
* Atributos adicionales: tipo_evento, lugar, organizador
* Metodo sobrescrito: generar_reporte(), muestra detalles del evento cultural

ejecucion de la subclase ActividadCultural:
![image](https://github.com/user-attachments/assets/9071ca2d-0eac-47b2-9811-a84f4d0f68a7)


Subclase ActividadAcademica:
Representa una actividad educativa o de formacion.
* Hereda de Actividad
* Atributos adicionales: tema, ponente, modalidad
* Metodo sobrescrito: generar_reporte(), muestra detalles academicos

ejecucion de la subclase ActividadAcademica:
![image](https://github.com/user-attachments/assets/7181a39c-e54b-4591-a5e5-4cbd684df28e)


Clase Estudiante
Representa a un estudiante que participa en actividades.
* Atributos: nombre, matricula, carrera, y una lista de actividades
* Metodos:
  * agregar_actividad() para registrar_actividades
  * generar_certificado() para mostrar un resumen decorado en consola
* Esta clase no hereda de la super clase

  ejecucion de la clase estudiante:
  ![image](https://github.com/user-attachments/assets/e7f57a88-cc2c-4bbc-9e28-fa007df07c6f)
  ![image](https://github.com/user-attachments/assets/eb652495-7213-4716-b0b8-1e2bab3f2fbb)


  Archivo Main
  En este archivo se prueba todo, o sea, generalmente todos los modulos, metodos, herencias, polimorfismos, etc.
  En las siguientes capturas se podra evidenciar que todo funciona correctamente.


  ejecucion del archivo Main:
  ![image](https://github.com/user-attachments/assets/ad3b79a8-1cc3-4375-9bda-435e3c65ff7c)
  ![image](https://github.com/user-attachments/assets/e2109dd8-c34a-4bad-8316-d56389f68a19)









