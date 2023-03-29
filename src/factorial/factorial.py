#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(desde): 
    res=[]
    for i in range(desde, 61):
        fact = 1
        while(i > 1): 
            fact *= i 
            i -= 1
        res.append(fact)
    return res
    
if len(sys.argv) == 1:
   print("Debe informar un número!")
   sys.exit()
else:
    num=int(sys.argv[1])

for numero in (factorial(num)):
    print(f"El factorial de {num}! es {numero}") 
    num += 1

