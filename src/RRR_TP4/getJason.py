"""Copyright IS2 © 2022, 2023 todos los derechos reservados."""
#*-------------------------------------------------------------
#getJason
#*-------------------------------------------------------------
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List
import json
import sys

class AlphabeticalOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        """Inicializa el iterador."""
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """Este metodo obtiene siguiente elemento."""
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value

class WordsCollection(Iterable):
    """Inicializa la colección de palabras."""
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        """Agrega un elemento a la coleccion"""
        self._collection.append(item)

class SingletonMeta(type):
    """Clase que implementa el patron Singleton."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Este metodo se llama cuando se crea una instancia de la clase APItoken."""
        if cls not in cls._instances:
            # Si no existe una instancia previa de la clase, se crea una nueva
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance# Se guarda la instancia creada
        return cls._instances[cls]  # Se devuelve la instancia almacenada en _instances

class APItoken(metaclass=SingletonMeta):
    """Esta clase implementa la logica para extraer un token
      de un archivo JSON y mostrar un mensaje de ayuda."""
    def __init__(self):
        """Este metodo se ejecuta al crear una instancia de la clase"""

    def extraer_token(self, jsonkey):
        """Este metodo permite extraer un token de un archivo JSON."""
        try:
            with open("sitedata.json", 'r') as myfile:
                data = myfile.read()
        except FileNotFoundError:
            print('No existe el archivo JSON')
            sys.exit()
        except ValueError:
            print('Error al cargar el archivo JSON')
            sys.exit()
        try:
            obj = json.loads(data)
            return str(obj[jsonkey])
        except KeyError:
            print('Token incorrecto, no existe en el archivo JSON')
            sys.exit()
        except:
            print('Error al extraer el token del archivo JSON')
            sys.exit()

class Handler(object):

    def __init__(self):
        """Inicializa el objeto Handler."""
        self.nextHandler = None

    def handle(self, numero_pedido, monto):
        """Maneja el pedido de pago."""
        if self.nextHandler == None:
            print("No hay saldo suficiente en las cuentas, no se puedo realizar el pago")
            return
        self.nextHandler.handle(numero_pedido, monto)

class Cuenta1Handler(Handler):
    def __init__(self, collection: WordsCollection, token):
        """Inicializa el objeto Cuenta1Handler."""
        super(Cuenta1Handler, self).__init__()
        self.token=token
        self.monto=1000
        self.collection = collection


    def handle(self, numero_pedido, monto):
        """Maneja el pedido de pago en el Banco 1."""
        print(f"Banco 1: explora pedido de pago {numero_pedido}")
        if monto <= self.monto:
            self.procesar_pago(numero_pedido, monto)
        else:
            print("Saldo insuficiente, Banco 1: pasa al siguiente actuador")
            super(Cuenta1Handler, self).handle(numero_pedido, monto)

    def procesar_pago(self, numero_pedido, monto):
        """Procesa el pago exitoso en el Banco 1."""
        self.monto -= monto
        print(f'Pago exitoso, numero de pedido {numero_pedido}, token: {self.token}, monto ${monto}\n')
        self.collection.add_item(f'Numero de pedido {numero_pedido}, Token: {self.token}, Monto ${monto}')

class Cuenta2Handler(Handler):
    def __init__(self, collection: WordsCollection, token):
        """Inicializa el objeto Cuenta2Handler."""
        super(Cuenta2Handler, self).__init__()
        self.token=token
        self.monto=2000
        self.collection = collection


    def handle(self, numero_pedido, monto):
        """Maneja el pedido de pago en el Banco 2."""
        print(f"Banco 2: explora pedido de pago {numero_pedido}")
        if monto <= self.monto:
            self.procesar_pago(numero_pedido, monto)
        else:
            print("Saldo insuficiente, Banco 2: pasa al siguiente actuador")
            super(Cuenta2Handler, self).handle(numero_pedido, monto)

    def procesar_pago(self, numero_pedido, monto):
        """Procesa el pago exitoso en el Banco 2."""
        self.monto -= monto
        print(f'Pago exitoso, numero de pedido {numero_pedido}, token: {self.token}, monto: ${monto}\n')
        self.collection.add_item(f'Numero de pedido {numero_pedido}, Token: {self.token}, Monto ${monto}')

#*--------------------------------------------------------------
# main
#*--------------------------------------------------------------
if __name__ == "__main__":

    z1=APItoken() # Se crea una instancia de la clase APItoken
    token1 = z1.extraer_token('token1')
    token2 = z1.extraer_token('token2')
    collection = WordsCollection()
    cuenta1=Cuenta1Handler(collection, token1) # Se inicializan los actuadores
    cuenta2=Cuenta2Handler(collection, token2)
    cuenta1.nextHandler=cuenta2 # Establece ahora la cadena de llamada
    

    cuenta1.handle('1', 500)
    cuenta1.handle('2', 500)
    cuenta1.handle('3', 500)
    cuenta1.handle('4', 500)
    cuenta1.handle('5', 500)
    cuenta1.handle('6', 500)
    cuenta1.handle('7', 500)

    print("\nPagos realizados:")
    print("\n".join(collection))
    print("")
