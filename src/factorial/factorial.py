#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
#este programa calcula los factoriales comprendidos entre la variable "desde" y el número 60.
def factorial(desde): 
    res=[]
    for i in range(desde, 61):
        fact = 1
        while(i > 1): 
            fact *= i 
            i -= 1
        res.append(fact)
    return res #devuelve una lista con los resultados de los factoriales
    
if len(sys.argv) == 1:
   print("Debe informar un número!")
   sys.exit()
else:
    num=int(sys.argv[1])
#en este ciclo se muestran los resultados correspondientes a cada número
for numero in (factorial(num)):
    print(f"El factorial de {num}! es {numero}") 
    num += 1

