#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num1, num2):  
    res=[]
    for i in range(num1, num2+1):
        fact = 1
        while(i > 1): 
            fact *= i 
            i -= 1
        res.append(fact)
    return res
    
if len(sys.argv) < 3:
   print("Debe informar dos números!")
   sys.exit()
else:
    numero1=int(sys.argv[1])
    numero2=int(sys.argv[2])
if numero1>3 and numero2<9:
    for numero in (factorial(numero1, numero2)):
        print(f"El factorial de {numero1}! es {numero}") 
        numero1 += 1
else:
    print("Alguno de los numeros ingresados está fuera del rango [4, 8]")
