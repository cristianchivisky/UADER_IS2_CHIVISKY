#!/usr/python
import os

class Handler(object):

    def __init__(self):
        self.nextHandler = None

    def handle(self, request):
        if self.nextHandler == None:
           print("Número no consumido.\n")
           return
        self.nextHandler.handle(request)

#*-------------------------------- PrimeHandler

class PrimeHandler(Handler):

    def handle(self, number):
        print(f"PrimeHandler: verifica si el número {number} es primo")
        if self.is_prime(number):
            print (f'Número {number} consumido por PrimeHandler\n')
        else:
            print("PrimeHandler: pasa al siguiente actuador")
            super(PrimeHandler, self).handle(number)

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


#*-------------------------------- ParHandler

class ParHandler(Handler):

    def handle(self, number):
        print(f"ParHandler: verifica si el número {number} es par")
        if self.is_par(number):
            print(f'Número {number} consumido por ParHandler\n')
        else:
            #print("ParHandler: pasa al siguiente actuador")
            super(ParHandler, self).handle(number)

    def is_par(self, num):
        if num % 2 == 0:
            return True
        else:
            return False


if __name__ == '__main__':

    os.system("clear")
#*---------------------------------------------------------------
#* Inicializa los actuadores
#*---------------------------------------------------------------
    prime_handler = PrimeHandler()
    par_handler = ParHandler()

#*---- Establece ahora la cadena de llamada

    prime_handler.nextHandler = par_handler

#*---- Se envían números a la cadena de responsabilidad para que lo procese
    for i in range(1, 100):
        prime_handler.handle(i)


