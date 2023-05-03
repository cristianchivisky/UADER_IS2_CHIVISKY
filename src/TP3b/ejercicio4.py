import os
#*--- Esta es la clase que representa el numero original
class Numero():

	def __init__(self, numero):
		self._numero = numero
		self._op = ''

	def mostrar_operacion(self):
		return f'{self._numero}'

	def operacion(self):
		return self._numero

#*--- Esta es la clase que le suma 2
class SumarDos(Numero):
	def __init__(self, componente):
		self._componente = componente

	def mostrar_operacion(self):
		return f"({self._componente.mostrar_operacion()}) + 2 "

	def operacion(self):
		return self._componente.operacion() + 2

#*--- Esta es la clase que lo multiplica por 2

class MultiplicarPorDos(Numero):
	def __init__(self, componente):
		self._componente = componente

	def mostrar_operacion(self):
		return f"({self._componente.mostrar_operacion()}) x 2 "

	def operacion(self):
		return self._componente.operacion() * 2

#*--- Esta es la clase que lo divide por 3

class DividirPorTres(Numero):
	def __init__(self, componente):
		self._componente = componente

	def mostrar_operacion(self):
		return f"({self._componente.mostrar_operacion()}) / 3"

	def operacion(self):
		return self._componente.operacion() / 3

#*------------------------------------------------------------------------
#* main
#*------------------------------------------------------------------------
if __name__ == '__main__':

	os.system("clear")
	try:
		numero=input('Ingrese un número: ')
		if numero == '':
			raise ValueError('Debe ingresar un número')
	except ValueError as error:
		print(error)
	else:
		numero=int(numero)
		before_numero=Numero(numero)
		after_numero= DividirPorTres(MultiplicarPorDos(SumarDos(before_numero)))
		print(f'\n{after_numero.mostrar_operacion()}')
		print(f"\nAntes {before_numero.operacion()} y despues {after_numero.operacion()}\n")
