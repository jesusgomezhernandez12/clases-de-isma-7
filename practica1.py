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
            ),

            Profesion(
                "administracion",
                5,2,6,10,3,9,8
            ),

            Profesion(
               "diseño grafico",
               2,2,10,4,3,6,6
            ),

            Profesion(
               "docencia",
               4,2,7,7,7,10,6
            )

        ]

def calcular_heuristica(self, usuario, profesion):
   score = 0
   score += (10 - abs(usuario["matematicas"] - profesion.matematicas)) * 3
   score += (10 - abs(usuario["programacion"] - profesion.programacion)) * 3
   score += (10 - abs(usuario["creatividad"] - profesion.creatividad)) * 2
   score += (10 - abs(usuario["liderazgo"] - profesion.liderazgo)) * 2
   score += (10 - abs(usuario["investigacion"] - profesion.investigacion)) * 3
   score += (10 - abs(usuario["comunicacion"] - profesion.comunicacion)) * 2
   score += (10 - abs(usuario["salario"] - profesion.salario)) * 4
   
   return score

def recomendar(self, usuario):

   resultados = []

   for profesion in self.profesiones:

      valor = self.calcular_heuristica(
         usuario,
         profesion
      )

      resultados.append(
         (profesion.nombre, valor)
      )

      resultados.sort(
         key=lambda x: x[1],
         reverse=True
      )

      self.historial.append(
         {
            "fecha": datetime.now(),
            "resultado": resultados[0][0]
         }
      )

      return resultados

   def mostrar_historial(self):

      print("Historial de consultas\n")

      if len(self.historial) == 0:
         print("No hay historial de consultas")
         return   

      for consulta in self.historial:

         print(
            consulta["fecha"],
            "-> ",
            consulta["resultado"]
         )

def capturar_datos():

   print("\nresponde del 1 al 10")

   usuario ={}

   usuario["matematicas"] = int(
      input("gusto por matematicas:")
   )

   usuario["programacion"] = int(
      input("gusto por programacion:")
   )

   usuario["creatividad"] = int(
      input("creatividad:")
   )

   usuario["liderazgo"] = int(
      input("liderazgo:")
   )

   usuario["investigacion"] = int(
      input("interes por la investigacion:")
   )

   usuario["comunicacion"] = int(
      input("habilidad de comunicacion:")
   )





         
