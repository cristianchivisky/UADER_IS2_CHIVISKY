import os
#*------------- Define una clase para los nodos terminales (leaf)
class Pieza:
	def __init__(self, *args):

#*--- indenta las posiciones a medida que se agregan
		self.position = args[0]

#*--- lista elementos
	def showDetails(self):
		'''Prints the position of the child element.'''
		print("\t", end ="")
		print(self.position)

#*---- Elemento compuesto, representa objetos en cualquier nivel de la jerarquia excepto el último
class ProductoPrincipal:

	def __init__(self, *args):
		self.position = args[0]
		self.children = []

#*----- Crea jerarquia
	def add(self, child):
		self.children.append(child)

#*---- Remueve jerarquia
	def remove(self, child):
		self.children.remove(child)

#*---- muestra detalles (itera a los niveles inferiores
	def showDetails(self):
		print(self.position)
		for child in self.children:
			print("\t", end ="")
			child.showDetails()

if __name__ == "__main__":
	os.system("clear")

#*------ Crea el top level de la jerarquia
	productoPrincipal = ProductoPrincipal("Producto Principal")

#*----- Crea el primer sub-conjunto
	subConjunto1 = ProductoPrincipal("Sub-conjunto-1")

	pieza11 = Pieza("Pieza #1")
	pieza12 = Pieza("Pieza #2")
	pieza13 = Pieza("Pieza #3")
	pieza14 = Pieza("Pieza #4")

	subConjunto1.add(pieza11)
	subConjunto1.add(pieza12)
	subConjunto1.add(pieza13)
	subConjunto1.add(pieza14)

#*---- Crea el segundo sub-conjunto
	subConjunto2 = ProductoPrincipal("Sub-conjunto-2")

	pieza21 = Pieza("Pieza #1")
	pieza22 = Pieza("Pieza #2")
	pieza23 = Pieza("Pieza #3")
	pieza24 = Pieza("Pieza #4")

	subConjunto2.add(pieza21)
	subConjunto2.add(pieza22)
	subConjunto2.add(pieza23)
	subConjunto2.add(pieza24)

#*---- Crea el tercer sub-conjunto
	subConjunto3 = ProductoPrincipal("Sub-conjunto-3")

	pieza31 = Pieza("Pieza #1")
	pieza32 = Pieza("Pieza #2")
	pieza33 = Pieza("Pieza #3")
	pieza34 = Pieza("Pieza #4")

	subConjunto3.add(pieza31)
	subConjunto3.add(pieza32)
	subConjunto3.add(pieza33)
	subConjunto3.add(pieza34)

#*---- Agrega ahora los tre subconjuntos al nivel raiz

	productoPrincipal.add(subConjunto1)
	productoPrincipal.add(subConjunto2)
	productoPrincipal.add(subConjunto3)

#*---- Muestra el resultado
	productoPrincipal.showDetails()

opcion=input('\nPesione "Enter" para agregar un subconjunto adicional con 4 piezas')
if opcion=='':
	#*---- Crea el sub-conjunto adicional
	subConjunto4 = ProductoPrincipal("Sub-conjunto-adicional")

	pieza41 = Pieza("Pieza #1")
	pieza42 = Pieza("Pieza #2")
	pieza43 = Pieza("Pieza #3")
	pieza44 = Pieza("Pieza #4")

	subConjunto4.add(pieza41)
	subConjunto4.add(pieza42)
	subConjunto4.add(pieza43)
	subConjunto4.add(pieza44)

	productoPrincipal.add(subConjunto4)

	productoPrincipal.showDetails()