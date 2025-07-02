# === PROYECTO FINAL - JUEGO DEL AHORCADO EN PYGAME ===
# Instrucciones:
# - Usar funciones, listas, diccionarios y archivos.
# - No usar clases ni programación orientada a objetos.
# - El juego debe leer palabras desde un archivo de texto externo (palabras.txt).
# - Mostrar la palabra oculta en pantalla, los intentos y las letras ingresadas.
# - Dibujar el muñeco del ahorcado a medida que se cometen errores (cabeza, cuerpo, brazos, piernas).
# - Mostrar mensaje final al ganar o perder.
# - Organizar el código con funciones bien nombradas.
# - El código debe estar comentado línea por línea.
# - Solo las partes del cuerpo deben contar como errores, no el soporte del ahorcado.

import pygame
import pygame.mixer as mixer
import random
import personaje
from verificar_cada_letra import verificar_cada_letra
from crear_cuerpo import dibujar_cuerpo_por_parte

pygame.init()

# ----------------- CONFIGURACIÓN DE PANTALLA -----------------
ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
#completar con nombre del equipo
pygame.display.set_caption("Juego del Ahorcado")

# ----------------- COLORES  se pueden modificar por los que elija el equipo-----------------
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (4, 255, 0)

# ----------------- FUENTE -----------------
FUENTE = pygame.font.SysFont(None, 48)

#-------------------Modelo de funciones, se deberan realizar en un archivo aparte
# Las funciones del personaje deben ser creadas y completadas por el equipo en un archivo aparte
# -------------------

# ----------------- CARGAR PALABRAS DESDE ARCHIVO -----------------
def cargar_palabras():
    try:
        with open("palabras.txt", "r") as archivo:
            lista_palabras = archivo.readlines()
            lista_palabras = [palabra.strip() for palabra in lista_palabras]
        return lista_palabras
    except FileNotFoundError as e:
        print("ERROR: Archivo no encontrado", e)
        return []    
    # Leer las palabras desde un archivo de texto y devolver una lista
    # Asegurate de tener un archivo llamado palabras.txt con una palabra por línea

# ----------------- ELEGIR PALABRA AL AZAR -----------------
def elegir_palabra(lista_palabras):
    palabra_aleatoria = random.choice(lista_palabras)
    palabra = palabra_aleatoria.upper()
    return palabra

# ----------------- DIBUJAR ESTRUCTURA DEL AHORCADO -----------------
def dibujar_estructura():
    # Dibuja la base, palo y cuerda del ahorcado (no cuenta como error)
    """
        Esta función crea la estructura típica del juego del Ahorcado
        No recibe ningún parametro y se dibujan en la pantalla las siguientes estructuras
        "Base - Palo - Palo Diagonal - VIGA - SOGA"
        Todas estas partes conforman la estructura y se dibujan una vez llamada la función 
        No retorna nigun valor o variable
    """
    #BASE
    BASE_COORDENADAS = pygame.draw.rect(VENTANA, NEGRO, (205, 600, 100, 4))
    #PALO
    PALO_COORDENADAS = pygame.draw.rect(VENTANA, NEGRO, (250, 350, 4, 250))
    #DIAGONAL
    DIAGONAL_COORDENADAS =pygame.draw.line(VENTANA, NEGRO, (251, 410),(320, 352), 4)    
    #VIGA
    VIGA = pygame.draw.rect(VENTANA, NEGRO, (250, 350, 100, 4))
    #SOGA
    SOGA = pygame.draw.rect(VENTANA, NEGRO, (350, 350, 4, 60))

# ----------------- DIBUJAR PARTES DEL CUERPO -----------------
def dibujar_cuerpo(errores):
    """
        Esta función recibe un parametro "errores" del tipo "int"
        Crea uno o más dibujos que se renderizara en base al número pasado por parametro
        Cada dibujo corresponde a una parte del cuerpo y al número de errores que reciba, un máximo de 6:
        1° Cabeza
        2° Cuerpo
        3° Pierna Izquierda
        4° Pierna Derecha
        5° Brazo Izquierdo
        6° Brazo Derecho
    """
    # Dibujar cabeza, tronco, brazos y piernas en base a la cantidad de errores
    dibujar_cuerpo_por_parte(errores)
        
# ----------------- DIBUJAR JUEGO EN PANTALLA -----------------
def dibujar_juego(palabra, letras_adivinadas, errores):
    # Llenar fondo, mostrar palabra oculta, letras ingresadas y dibujar estructura y cuerpo
    # Se renderiza el fondo
    VENTANA.fill(BLANCO)
    # Se dibuja la estructura del ahorcado
    dibujar_estructura()
    # Se renderiza la palabra elegida
    acumulador_X = 500
    contador_letras = 0
    # Recorro cada letra de la palabra elegida al azar
    for i in palabra:
        # Dibujo los guiones en base a la cantidad de letras que haya, utilizo un "acumulador" para ir dejando dibujando desde n posición x e ir aumentandola dejando un espacio en blanco, el 2 corresponde al width de los guiones
        pygame.draw.line(VENTANA, NEGRO, (acumulador_X, 485), (acumulador_X + 20, 485), 2 )
        # Evaluo si es la primer letra de la palabra con un contador o si es la última de la palabra para dibujarlas inicialmente
        if contador_letras == 0 or contador_letras == len(palabra):
            letra = FUENTE.render(i, True, NEGRO)
            # Reutilizo ese acumuador de X para dibujar por encima del guion la letra inicial y última
            VENTANA.blit(letra, (acumulador_X,450))
            # Voy sumando el contador hasta llegar a el largo de la palabra elegida
            contador_letras += 1
        # Evaluo si la letra que estoy recorriendo se encuentra dentro de las letras adivinadas y la dibujo por encima del guion con el acumulador de X, 
        if i in letras_adivinadas:
            letra = FUENTE.render(i, True, NEGRO)
            VENTANA.blit(letra, (acumulador_X,450))
        # Como mencione anteriormente, voy sumando 20 que es el largo del guion + 5 que es la "separación entre cada guion dibujado
        acumulador_X += 25
        contador_letras += 1


    # Se dibujan las partes del cuerpo por n cantidad de errores
    dibujar_cuerpo(errores)

# ----------------- VERIFICAR LETRA -----------------
def verificar_letra(letra, palabra, letras_adivinadas):
    # Agregar la letra a letras_adivinadas si no estaba
    # Retornar True si la letra está en la palabra, False si no
    verificar_cada_letra(letra, palabra, letras_adivinadas)

# ----------------- SONIDO -----------------
pygame.mixer.init()  # Inicializa el motor de sonido
sonido_error = pygame.mixer.Sound("error.wav")  # Asegurate de tener este archivo
sonido_grito = pygame.mixer.Sound("grito.wav")
sonido_victoria = pygame.mixer.Sound("win.wav")
mixer.music.set_volume(0.4)

# ----------------- BUCLE PRINCIPAL -----------------
def jugar():
    # 1. Cargar palabras desde archivo y elegir una al azar
    palabra_elegida = elegir_palabra(cargar_palabras()) 

    # 2. Inicializar estructuras necesarias: letras_adivinadas, errores, reloj, banderas
    letras_adivinadas = []
    errores = 0
    max_errores = 6
    bandera_juego = True 
    reloj = pygame.time.Clock()
    mensaje_adivino = None
    mensaje_error = None

    sonido_muerte_reproducido = False
    sonido_victoria_reproducido = False
    
    dict_personaje = personaje.crear_personaje(ANCHO/2,ALTO-200,200,200)
    # 3. Crear un bucle while que termine al cerrar el juego o al ganar/perder
    while bandera_juego:
        letra_presionada = ""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                bandera_juego = False

    # 4. Dentro del bucle:
    #   - Capturar eventos (teclas)
            if evento.type == pygame.KEYDOWN:
                if errores == max_errores or set(letras_adivinadas) == set(palabra_acortada) :
                    break
                else:
                    letra_presionada = evento.unicode.upper()
                    resultado = verificar_cada_letra(letra_presionada, palabra_elegida, letras_adivinadas)
                    # Se incrementan errores si corresponde
                    if resultado == True:   
                        mensaje_adivino = FUENTE.render("¡Correcto!, adivinaste una letra", True, NEGRO)
                        mensaje_error = None
                    elif resultado == False:
                        sonido_error.play()
                        errores += 1
                        mensaje_error = FUENTE.render("Incorrecto, no has adivinado ninguna letra", True, ROJO)
                        mensaje_adivino = None
                    else:
                        mensaje_error = FUENTE.render(resultado, True, ROJO)
                        mensaje_adivino = None

        movimiento_usuario = pygame.key.get_pressed() #Variable que almacena las teclas que toca el usuario
                
        #Verifica si se mueve a la izquierda    
        if movimiento_usuario[pygame.K_LEFT]: 
            #Si se mueve a la izquierda tiene que moverse 10 pixeles hacia la izquierda
            pixeles_a_mover_X = -10
            #Actualizo el personaje llamando a la funcion
            personaje.actualizar_personaje(dict_personaje, pixeles_a_mover_X)
            #Verifica para donde esta mirando el personaje, para cambiar su orientacion
            if dict_personaje['mirando_derecha'] == True:
                #Si estaba mirando a la derecha entonces se da vuelta el personaje
                dict_personaje['surface'] = pygame.transform.flip(dict_personaje['surface'], True, False)
                #En caso de que mire a la izquierda se actualiza el esta parte del diccionario a False 
                dict_personaje['mirando_derecha'] = False

        if movimiento_usuario[pygame.K_RIGHT]:
            pixeles_a_mover_X = +10
            personaje.actualizar_personaje(dict_personaje, pixeles_a_mover_X)
            if dict_personaje['mirando_derecha'] == False:
                dict_personaje['surface'] = pygame.transform.flip(dict_personaje['surface'], True, False)
                dict_personaje['mirando_derecha'] = True


                
    #   - Dibujar estado del juego en pantalla
        # Utilizo el condicional para que se muestre el cuerpo completo dibujado y no se reinicie
        if errores < 6:
            dibujar_juego(palabra_elegida,letras_adivinadas,errores)
        else:
            dibujar_juego(palabra_elegida,letras_adivinadas,max_errores)

        # Se actualizan los mensajes de letras adivinadas o errores que pueda tener al teclear el jugador
        if mensaje_adivino:
            VENTANA.blit(mensaje_adivino, (200,200))
        elif mensaje_error:
            VENTANA.blit(mensaje_error, (200,200))

    #   - Verificar condiciones de fin (victoria o derrota)
        # Creo una lista de las letras de la palabra elgida
        p_elegida = list(palabra_elegida)
        # # Elimino la primer letra de la lista
        p_elegida.pop(0)
        # # Eliminio la ultima letra de la lista
        p_elegida.pop(-1)
        # Vuelvo a unir la palabra pero ahora sin esa primer y ultiima letra
        palabra_acortada = "".join(p_elegida)
        # Evaluo si no hay elementos duplicados y si son iguales, de ser así, el jugador adivinó todas las letras
        if set(letras_adivinadas) == set(palabra_acortada):
            mensaje_adivino = FUENTE.render("¡Has ganado, felicidades!", True, VERDE) 
            VENTANA.blit(mensaje_adivino, (200,200))

            #Agrego sonido de victoria
            if sonido_victoria and not sonido_victoria_reproducido: #Verifico que este cargado el sonido y que no se haya reproducido.
                sonido_victoria.play() # Reproduce el sonido
                sonido_victoria_reproducido = True # Marca que ya sono y que no va a volver a reproducirse
        if max_errores == errores and not sonido_muerte_reproducido:
            mensaje_error = FUENTE.render("No has adivinado la palabra, suerte la próxima", True, ROJO) 
            VENTANA.blit(mensaje_error, (200,200))

            #Agrego sonido de derrota(Grito)
            if sonido_grito and not sonido_muerte_reproducido:
                sonido_grito.play()
                sonido_muerte_reproducido = True

        personaje.actualizar_pantalla(dict_personaje, VENTANA)
    #   - Actualizar pantalla
        pygame.display.update()

    #   - Controlar FPS
        reloj.tick(30)

    pygame.quit()

# Instrucción: este bloque debe ser completado por el estudiante según las consignas
# No ejecutar el juego automáticamente: solo se invoca desde consola o importación
# Descomentar la línea siguiente para probar el juego terminado:
jugar()
