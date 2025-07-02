# ----------------- VERIFICAR LETRA -----------------
# def verificar_cada_letra(letra, palabra, letras_adivinadas):
#     # Agregar la letra a letras_adivinadas si no estaba
#     # Retornar True si la letra está en la palabra, False si no
def verificar_cada_letra(letra, palabra, letras_adivinadas):
    #Paso las letras y las palabras a mayuscula para evitar conflictos  
    letra = letra.upper()
    palabra = palabra.upper()
    mensaje_error = "" 

     #Realizo la verificacion de la letra y ademas valido que la letra sea un caracter valido y que no sea distinto de 1. si falla devuelve un mensaje de error
    if not (letra.isalpha() and len(letra) == 1):
        mensaje_error = "ERROR: Ingresá una sola letra válida (A-Z)"
        return mensaje_error

    # Valido si la letra pasada por parametro se encuentra en la lista de letras adivinadas, de ser así retorno un mensaje de error para que intente con otra letra
    if letra in letras_adivinadas:
        mensaje_error = "ERROR: Ya adivinaste esa letra, intentá con otra"
        return mensaje_error

    # Si la letra está en la palabra la añado a la lista de letras adivinadas y retorno true
    if letra in palabra:
        letras_adivinadas.append(letra)
        return True
    
    # Si no la letra no se encuentra en la lista y tampoco está en la palabra, retorno false
    return False
