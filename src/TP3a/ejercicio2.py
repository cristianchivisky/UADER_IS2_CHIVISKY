#!/usr/python
import sys
from abc import ABC, abstractmethod
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self, base):
        # Primero se llama al método factory para crear un nuevo objeto Impuesto.
        impuesto = self.factory_method()

        # A continuación uso el objeto creado invocando la operación específica para el mismo (que no figura definida en la clase que estoy usando).
        #result = f"Ejecución del Creator con {impuesto.calcular_impuesto()}\n"
        return impuesto.calcular_impuesto(base)

class Impuesto(ABC):
    @abstractmethod
    def calcular_impuesto(self, num):
        pass

class IVA(Impuesto):
    def calcular_impuesto(self, num):
        iva = num * 21 /100
        return iva
class IIBB(Impuesto):
    def calcular_impuesto(self, num):
        iibb = num * 5 /100
        return iibb
class ContribucionesMunicipales(Impuesto):
    def calcular_impuesto(self, num):
        contrib_municipales = num * 1.2 /100
        return contrib_municipales
    
class CreatorIVA(Creator):
    def factory_method(self) -> Impuesto:
        return IVA()

class CreatorIIBB(Creator):
    def factory_method(self) -> Impuesto:
        return IIBB()

class CreatorContribucionesMunicipales(Creator):
    def factory_method(self) -> Impuesto:
        return ContribucionesMunicipales()

class ImpuestoFactory():
    def calcular(self, base_imponible):
        iva, iibb, contrib_municipales= None, None, None
        iva = CreatorIVA().some_operation(base_imponible)
        iibb = CreatorIIBB().some_operation(base_imponible)
        contrib_municipales = CreatorContribucionesMunicipales().some_operation(base_imponible)
        return iva + iibb + contrib_municipales

if __name__ == "__main__":
    # The client code.
    if len(sys.argv) == 1:
        print("Debe informar el valor del importe base imponible")
        sys.exit()
    else:
        NUMERO=int(sys.argv[1])
        s1 = ImpuestoFactory().calcular(NUMERO)
        print(s1)
