#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Math             // Módulo matematico.
math.sqrt(date) //  Saca la Raiz cuadrada de un 'numero positivo'.
"""

import math


date = int(input("Ingresa un número: "))

counter = 5

#-Mientras que 'date' sea menor que '0', cumplete.
while date < 0:
    print("")
    print("No se puede sacar Raíz Cuadrada a un número negativo")
    print("")
    counter -= 1
    date = int(input("Ingresa un número: "))
    #-Si fallas 5 veces, para el bucle.
    if counter == 0:
        print("")
        print("Lo siento, hiciste muchos intentos")
        break

#-Si 'date' es mayor que '0', sacale la raíz cuadrada.
if date > 0:
    result = math.sqrt(date)
    print("")
    print(f"La raíz cuadrada de {date} es {result}")


