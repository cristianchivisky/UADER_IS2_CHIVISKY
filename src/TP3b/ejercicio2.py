import os
#*--- Abstracción de implementación (TrenLaminador1)
class TrenLaminador1:
	def __init__(self):
		self.largo = 5

	def genera_lamina(self, espesor, ancho):
		print('TrenLaminador1 va a generar una lamina de dimensiones:')
		print(f'{espesor}" de espesor, {ancho}mts. de ancho y {self.largo}mts. de largo.')

#*--- Abstracción de implementación (TrenLaminador2)
class TrenLaminador2:
	def __init__(self):
		self.largo = 10

	def genera_lamina(self, espesor, ancho):
		print('TrenLaminador2 va a generar una lamina de dimensiones:')
		print(f'{espesor}" de espesor, {ancho}mts. de ancho y {self.largo}mts. de largo.')

#*---Clase Lamina de Acero con sus propiedades pero con método de fabricación flexible
class LaminaAcero:

	def __init__(self, espesor, ancho, producing_tren):
		self._espesor = espesor
		self._ancho = ancho
		self._producing_tren = producing_tren

#*---- cuando se invoca la producción invoca al objeto cuyo puntero se almacenó al crear
	def genera(self):
		self._producing_tren.genera_lamina(self._espesor, self._ancho)

#*-----------------------------------------------------------
#* main
#*-----------------------------------------------------------

os.system("clear")

#*--- implementa una primer lamina y le asigna TrenLaminador1()
lamina1 = LaminaAcero(0.5, 1.5, TrenLaminador1())
lamina1.genera()
print('\n')
#*--- implementa una segunda lamina y le asigna TrenLaminador2()
lamina2 = LaminaAcero(0.5, 1.5, TrenLaminador2())
lamina2.genera()
