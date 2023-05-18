import os

class Subject:
#*------- Representa lo que se está observando

	def __init__(self):
		self._observers = []

	def notify(self, modifier = None):
		for observer in self._observers:
			if modifier != observer:
				observer.update(self)

	def attach(self, observer):
#*------- Agregar observador si ya no está en la lista
		if observer not in self._observers:
			self._observers.append(observer)

	def detach(self, observer):
#*------- Remover observador si está en la lista
		try:
			self._observers.remove(observer)
		except ValueError:
			pass

#*----------- Define a los observadores
class Data(Subject):

	def __init__(self, name =''):
		Subject.__init__(self)
		self.name = name
		self._data = 0

	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, value):
		self._data = value
		print(f"El ID ha sido actualizado a '{value}'")
		self.notify()


class Clase1:
	id = '5h7l'

	def update(self, subject):
		if subject.data == self.id:
		    print('Coincide con ID Clase1')

class Clase2:
	id = '8b3d'

	def update(self, subject):
		if subject.data == self.id:
		    print('Coincide con ID Clase2')


class Clase3:
	id = '2k9x'

	def update(self, subject):
		if subject.data == self.id:
		    print('Coincide con ID Clase3')

class Clase4:
	id = '1a5z'
	def update(self, subject):
		if subject.data == self.id:
		    print('Coincide con ID Clase4')

if __name__ == "__main__":

	os.system("clear")

	view1 = Clase1()
	view2 = Clase2()
	view3 = Clase3()
	view4 = Clase4()
	
	obj1 = Data('Data 1')
	
	obj1.attach(view1)
	obj1.attach(view2)
	obj1.attach(view3)
	obj1.attach(view4)

	obj1.data = '1f3j'
	obj1.data = '5h7l'
	obj1.data = '8b3d'
	obj1.data = '1s6b'
	obj1.data = '5n7d'
	obj1.data = '2k9x'
	obj1.data = '0g6w'
	obj1.data = '1a5z'
