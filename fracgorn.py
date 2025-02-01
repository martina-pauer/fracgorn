#!/usr/bin/python3

'''
    Genera texto aleatorio de 140 caracteres
    sin requerir interet usando modulo random,
    condicionales, bucles y una logica del juego
    cara o cruz de lanzar una moneda y ver en que
    lado cae.
'''

import random

# Definicion de abecedario de donde tomar las letras
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Defino vocales para diferenciarlas de consonantes
vocales = 'aeiou'
# Defino consonantes como no vocales
consonantes = ''
# pre-computo para obtener letras consonantes desde las vocales y abecedario para ahorrar 280 veces el poder de computo al generar
for letra in alphabet:
    if not letra in vocales:
        # Solo agrego si la letra no es vocal al conjunto de consonantes
        consonantes += letra
# Signos de puntuacion para pausas de texto
separar = ',.;'
# Seleccion aleatoria y adaptada a requisitos de la lengua del texto
texto = ''
# Control de la cantidad de caracteres para que no haya problemas de texto muy largo
caracteres = 0
for caracter in range(140):
    # Cada una o dos vocales sigue una consonante y viceversa
    for vocal in range(random.randint(1, 2)):
        # Agrego letra al texto seleccionando solo dentro de las que son vocales
        if caracteres < 140:
            # Agrego solo si al hacerlo no se generan mas de la cantidad de caracteres permitida
                texto += random.choice(vocales)
            # Cuento caracter agregado
                caracteres += 1
    # Cada uno de estos bucles anidados se puede ejecutar hasta 280 veces (se repite 140 veces ejecutar dos veces el bucle)
    for consonante in range(random.randint(1, 2)):
        # Agrego letra al texto usando selector aleatorio de conjunto de valores pre-computado 'consonantes'
        if caracteres < 140:
            # Agrego solo si al hacerlo no supera la cantidad de caracteres
            texto += random.choice(consonantes)
            # Cuento caracter agregado
            caracteres += 1
        # Agrego un espacio necesario cada 1 a 7 caracteres (si la cantidad es multiplo de eso)
    if (caracteres % random.randint(1, 7) == 0) and (caracteres < 140) and (caracteres > 1):
        # Agrego solo si al hacerlo no supera limite de caracteres cada 7 caracteres
        texto += ' '
    elif (caracteres % random.randint(3, 21) == 0) and (caracteres < 140) and (caracteres > 1):
        # Agrego signo de puntuacion aleatorio con espacio si de forma aleatorias
        texto += (random.choice(separar) + ' ' + random.choice(vocales))
    elif (caracteres % 20 == 0) and (caracteres < 140):
        # Cada 20 caracteres agrego nueva linea
        texto += '\n'
# Muestro el texto generado
print(texto)
