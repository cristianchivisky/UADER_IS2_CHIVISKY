import os

class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
	   
   def getAvion(self):
      avion = Avion()
      
      # Primero el chasis
      body = self.__builder.getBody()
      avion.setBody(body)
      
      # Luego 2 turbinas
      i=0
      while i < 2:
        turbina = self.__builder.getTurbina()
        avion.setTurbina(turbina)
        i += 1

    # Luego 2 alas
      i=0
      while i < 2:
        ala = self.__builder.getAla()
        avion.setAla(ala)
        i += 1
      
      # Finalmente un tren de aterrizaje
      tren_aterrizaje = self.__builder.getTrenAterrizaje()
      avion.setTrenAterrizaje(tren_aterrizaje)

      # Retorna el avión completo
      return avion

#*----------------------------------------------------------------
#* Esta es la definición de un objeto avión inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Avion:
   def __init__(self):
      self.__body = None
      self.__turbina = list()
      self.__ala = list()
      self.__tren_aterrizaje = None
      

   def setBody(self, body):
      self.__body = body

   def setTurbina(self, turbina):
      self.__turbina.append(turbina)

   def setAla(self, ala):
      self.__ala.append(ala)

   def setTrenAterrizaje(self, tren_aterrizaje):
      self.__tren_aterrizaje = tren_aterrizaje

   def specification(self):
      print ("chasis: %s" % (self.__body.shape))
      print ("turbinas: %d" % (self.__turbina[0].horsepower), "hp")
      print ("alas: %d" % (self.__ala[0].size), "mts")
      print ("tren de aterrizaje: %s" % (self.__tren_aterrizaje.type))
#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class Builder:
      def getBody(self): pass
      def getTurbina(self): pass
      def getAla(self): pass
      def getTrenAterrizaje(self): pass

#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un Avión
#* Establece instancias para chasis, turbina, ala y tren de aterrizaje 
#* estableciendo las partes específicas que (en un avión) 
#* deben tener esas partes
#*-------------------------------------------------------
class AvionBuilder(Builder):
   def getBody(self):
      body = Body()
      body.shape = "Burden"
      return body
   
   def getTurbina(self):
      turbina = Turbina()
      turbina.horsepower = 380
      return turbina
   
   def getAla(self):
      ala = Ala()
      ala.size = 8
      return ala
   
   def getTrenAterrizaje(self):
      tren_aterrizaje = TrenAterrizaje()
      tren_aterrizaje.type = "Retractable"
      return tren_aterrizaje

#*----------------------------------------------------------------
#* Define partes genéricas para un avión(sin inicializar)
#*----------------------------------------------------------------
class Body:
   shape = None

class Turbina:
   horsepower = None

class Ala:
   size = None

class TrenAterrizaje:
   type = None

#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():

#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el 
#* proceso de construcción
#*----------------------------------------------------------------
   avionBuilder = AvionBuilder() # initializing the class
   director = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un Avión
#*----------------------------------------------------------------   
   director.setBuilder(avionBuilder)

#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un Avión según
#* la hoja de ruta
#*----------------------------------------------------------------
   condor = director.getAvion()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   condor.specification()
   print ("\n\n")

#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
   os.system("clear")
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avión\n")

   main()
