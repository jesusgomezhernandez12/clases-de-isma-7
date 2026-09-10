from datetime import datetime

class Profesion:
  def __init__(
    self,
    nombre,
    matematicas,
    programacion,
    liderazgo,
    investigacion,
    comunicacion,
    salario
  ):
    self.nombre = nombre
    self.matematicas = matematicas
    self.programacion = programacion
    self.liderazgo = liderazgo
    self.investigacion = investigacion
    self.comunicacion = comunicacion
    self.salario = salario

class AgenteVocacional:

    def __init__(self):
        self.historial= []
        self.profesiones = [
           
            Profesion(
               "Ingenieria en sistemas",
               10,10,7,6,8,5,9
            ),

            Profesion(
               "Científico de Datos",
                 10,9,6,5,10,4,10
            ),

            Profesion(
               "medicina", 
               8,1,5,7,9,8,10
            ),

            Profesion(
                 "arquitectura",
                 6,2,10,7,4,7,8
            ),

            Profesion(
               "derecho",
               5,1,5,9,4,10,8
            )

            Profesion(
                "administracion",
                5,2,6,10,3,9,8
            )

            Profesion(
               "diseño grafico",
               2,2,10,4,3,6,6
            )

            Profesion(
               "docencia",
               4,2,7,7,7,10,6
            )

        ]

def calcular_heuristica(self, usaurio, profesion):
   
