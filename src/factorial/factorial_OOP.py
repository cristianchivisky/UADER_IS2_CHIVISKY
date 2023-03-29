class Factorial:
    def __init__(self, num1, num2):
        self.minimo = num1
        self.maximo = num2
        self.resultado = []

    def min(self):
        self.minimo

    def min(self, a):
        self.minimo = a

    def max(self):
        self.maximo

    def max(self, a):
        self.maximo = a

    def res(self):
        num_aux = self.minimo
        for numero in (self.resultado):
            print(f'El factorial de {num_aux} es {numero}')
            num_aux += 1

    def run(self):
        min = int(self.minimo)
        max = int(self.maximo)
        if min >= 0 and max >= 0:
            aux = []
            for i in range(min, max+1):
                fact = 1
                while(i > 1):
                    fact *= i
                    i -= 1
                aux.append(fact)
            self.resultado = aux
        else:
            return print('Función "run" no disponible si alguno de los números ingresados es negativo')
