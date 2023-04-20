#!/usr/bin/python3.7
import sys
from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        # Primero se llama al método factory para crear un nuevo objeto hamburguesa.
        hamburguesa = self.factory_method()

        # A continuación uso el objeto creado invocando la operación específica para el mismo (que no figura definida en la clase que estoy usando).
        #result = f"Ejecución del Creator con {hamburguesa.forma_entrega()}\n"
        return hamburguesa.forma_entrega()

class Hamburguesa():
    @abstractmethod
    def forma_entrega():
        pass
class EntregaMostrador():
    def forma_entrega(self) -> str:
        return "Entregada en mostrador"
class EntregaCliente():
    def forma_entrega(self) -> str:
        return "Retirada por el cliente"
class EntregaDelivery():
    def forma_entrega(self) -> str:
        return "Enviada por delivery"
    
class CreatorEntregaMostrador(Creator):
    def factory_method(self) -> Hamburguesa:
        return EntregaMostrador()

class CreatorEntregaCliente(Creator):
    def factory_method(self) -> Hamburguesa:
        return EntregaCliente()

class CreatorEntregaDelivery(Creator):
    def factory_method(self) -> Hamburguesa:
        return EntregaDelivery()

class HamburguesaFactory():
    def crear_hamburguesa(self, entrega):
        aux= None
        if entrega == "mostrador":
            aux = CreatorEntregaMostrador().some_operation()
        elif entrega == "cliente":
            aux = CreatorEntregaCliente().some_operation()
        elif entrega == "delivery":
            aux = CreatorEntregaDelivery().some_operation()
        return aux
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('informe el tipo de entrega "mostrador", "delivery" o "cliente"')
        sys.exit()
    else:
        TIPO_ENTREGA = str(sys.argv[1])
        s1 = HamburguesaFactory().crear_hamburguesa(TIPO_ENTREGA)
        print(s1)
