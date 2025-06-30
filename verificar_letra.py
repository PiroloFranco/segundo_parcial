import pygame
import random

# ----------------- VERIFICAR LETRA -----------------
def verificar_letra(letra, palabra, letras_adivinadas):
    # Agregar la letra a letras_adivinadas si no estaba
    # Retornar True si la letra está en la palabra, False si no

    #Paso las letras y las palabras a minuscula para evitar conflictos  
    letra = letra.lower()
    palabra = palabra.lower()

    #Realizo la verificacion de la letra y ademas valido que la letra sea un caracter valido y que no sea distinto de 1. si falla devuelve un mensaje de error
    if not (letra.isalpha() and len(letra) == 1):
        return "ERROR: Por favor, ingrese un caracter valido"
    
    #Hago una verificacion para comprobar que la letra ingresada no fue utilizada y la añado a la variable. En caso de de haber una letra repetida devolverá un mensaje de error 
    if letra in letras_adivinadas:
        return "ERROR: Ya se ingresó esa letra, proba con otra"
    else:
        letras_adivinadas.add(letra)

    #Verifico finalmente si la letra esta dentro de la palabra
    if letra in palabra:
        return True #La letra esta dentro de la palabra
    else:
        return False #La letra no esta dentro de la palabra
