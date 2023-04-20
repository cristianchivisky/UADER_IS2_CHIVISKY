from abc import ABC, abstractmethod
class Factura(ABC):
    def __init__(self, importe):
        self.importe = importe
    @abstractmethod
    def tipo_factura(self):
        pass
    def __str__(self):
        return f"{self.tipo_factura()}: ${self.importe}"

class FacturaResponsableInscripto(Factura):
    def tipo_factura(self):
        return "Factura Responsable Inscripto"

class FacturaNoInscripto(Factura):
    def tipo_factura(self):
        return "Factura IVA No Inscripto"

class FacturaExento(Factura):
    def tipo_factura(self):
        return "Factura IVA Exento"

class FacturaFactory(ABC):
    @abstractmethod
    def crear_factura(self, importe):
        pass

class FacturaResponsableInscriptoFactory(FacturaFactory):
    def crear_factura(self, importe):
        return FacturaResponsableInscripto(importe + importe * 0.21)

class FacturaNoInscriptoFactory(FacturaFactory):
    def crear_factura(self, importe):
        return FacturaNoInscripto(importe)

class FacturaExentoFactory(FacturaFactory):
    def crear_factura(self, importe):
        return FacturaExento(importe)

# Uso del patrón Factory Method
# Ejemplo de uso:
if __name__ == "__main__":
    
    try:
        condicion_impositiva = input('Informe la condición impositiva del cliente: ')
        if condicion_impositiva == '':
            raise ValueError('Debe ingresar si es Responsable inscripto, IVA no inscripto o IVA exento!')
    except ValueError as e:
            print(e)
    else:
        IMPORTE_TOTAL= 300000
        if condicion_impositiva == "Responsable inscripto":
            factura_factory = FacturaResponsableInscriptoFactory()
        elif condicion_impositiva == "IVA no inscripto":
            factura_factory = FacturaNoInscriptoFactory()
        elif condicion_impositiva == "IVA exento":
            factura_factory = FacturaExentoFactory()

        factura = factura_factory.crear_factura(IMPORTE_TOTAL)
        print(factura)  # imprimirá la factura correspondiente a la condición impositiva del cliente
