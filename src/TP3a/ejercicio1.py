#!/usr/python
import sys
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Factorial(metaclass=SingletonMeta):
    def __init__(self, num1):
        self.num = num1

    def calcular_factorial(self):
        num=self.num 
        if num < 0: 
            print("Factorial de un número negativo no existe")

        elif num == 0: 
            return 1
            
        else: 
            fact = 1
            while(num > 1): 
                fact *= num 
                num -= 1
            return fact 

if __name__ == "__main__":
    # The client code.
    if len(sys.argv) == 1:
        print("Debe informar un número!")
        sys.exit()
    else:
        numero=int(sys.argv[1])
    s1 = Factorial(numero)
    print(f'El factorial de {numero} es: {s1.calcular_factorial()}')
    