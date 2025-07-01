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
import random

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
    match errores:
        case 1:
            CABEZA = pygame.draw.circle(VENTANA, NEGRO, (352, 430), 20, 4)
        case 2:
            CABEZA = pygame.draw.circle(VENTANA, NEGRO, (352, 430), 20, 4)
            CUERPO = pygame.draw.rect(VENTANA, NEGRO, (350, 450, 4, 50))
        case 3:
            CABEZA = pygame.draw.circle(VENTANA, NEGRO, (352, 430), 20, 4)
            CUERPO = pygame.draw.rect(VENTANA, NEGRO, (350, 450, 4, 50))
            PIERNA_IZQUIERDA = pygame.draw.line(VENTANA, NEGRO, (350, 500),(330, 540), 4)
        case 4:
            CABEZA = pygame.draw.circle(VENTANA, NEGRO, (352, 430), 20, 4)
            CUERPO = pygame.draw.rect(VENTANA, NEGRO, (350, 450, 4, 50))
            PIERNA_IZQUIERDA = pygame.draw.line(VENTANA, NEGRO, (350, 500),(330, 540), 4)
            PIERNA_DERECHA = pygame.draw.line(VENTANA, NEGRO, (352, 500), (372, 540), 4)
        case 5:
            CABEZA = pygame.draw.circle(VENTANA, NEGRO, (352, 430), 20, 4)
            CUERPO = pygame.draw.rect(VENTANA, NEGRO, (350, 450, 4, 50))
            PIERNA_IZQUIERDA = pygame.draw.line(VENTANA, NEGRO, (350, 500),(330, 540), 4)
            PIERNA_DERECHA = pygame.draw.line(VENTANA, NEGRO, (352, 500), (372, 540), 4)
            BRAZO_IZQUIERDO = pygame.draw.line(VENTANA, NEGRO, (352, 460), (332, 470), 4)
        case 6:
            CABEZA = pygame.draw.circle(VENTANA, NEGRO, (352, 430), 20, 4)
            CUERPO = pygame.draw.rect(VENTANA, NEGRO, (350, 450, 4, 50))
            PIERNA_IZQUIERDA = pygame.draw.line(VENTANA, NEGRO, (350, 500),(330, 540), 4)
            PIERNA_DERECHA = pygame.draw.line(VENTANA, NEGRO, (352, 500), (372, 540), 4)
            BRAZO_IZQUIERDO = pygame.draw.line(VENTANA, NEGRO, (352, 460), (332, 470), 4)
            BRAZO_DERECHO = pygame.draw.line(VENTANA, NEGRO, (352, 460), (372, 470), 4)
        
# ----------------- DIBUJAR JUEGO EN PANTALLA -----------------
def dibujar_juego(palabra, letras_adivinadas, errores):
    # Llenar fondo, mostrar palabra oculta, letras ingresadas y dibujar estructura y cuerpo
    pass

# ----------------- VERIFICAR LETRA -----------------
def verificar_letra(letra, palabra, letras_adivinadas):
    # Agregar la letra a letras_adivinadas si no estaba
    # Retornar True si la letra está en la palabra, False si no
    pass

# ----------------- SONIDO -----------------
# pygame.mixer.init()  # Inicializa el motor de sonido
# sonido_error = pygame.mixer.Sound("error.wav")  # Asegurate de tener este archivo

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
    
    # 3. Crear un bucle while que termine al cerrar el juego o al ganar/perder
    while bandera_juego:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                bandera_juego = False

    # 4. Dentro del bucle:
    #   - Capturar eventos (teclas)
            if evento.type == pygame.KEYDOWN:
                letra = evento.unicode.upper()

    #   - Verificar letras
        # try:
        #     verificar_letra(letra,palabra_elegida,letras_adivinadas)  
        # except as :

    #   - Incrementar errores si corresponde
            if not verificar_letra(letra,palabra_elegida,letras_adivinadas):
                    errores += 1
                    
    #   - Dibujar estado del juego en pantalla
            dibujar_estructura()
            dibujar_cuerpo(errores)
            dibujar_juego(palabra_elegida,letras_adivinadas,errores)

    #   - Verificar condiciones de fin (victoria o derrota)
            if len(letras_adivinadas) == len(palabra_elegida):
                print("adjuntar sonido ganador")
                break
            
            if max_errores == errores:
                print("adjuntar sonido perdedor")
                break
    #   - Actualizar pantalla
        pygame.display.update()

    #   - Controlar FPS
        reloj.tick(30)

    pygame.quit()

# Instrucción: este bloque debe ser completado por el estudiante según las consignas
# No ejecutar el juego automáticamente: solo se invoca desde consola o importación
# Descomentar la línea siguiente para probar el juego terminado:
jugar()
