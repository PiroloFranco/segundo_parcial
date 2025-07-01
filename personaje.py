import pygame

def crear_personaje(x, y, ancho, alto):
    '''    Objetivo: inicializar el personaje y agrupar todas sus propiedades en un solo diccionario

    parametros: 'x' y 'y' para la posicion inicial y el ancho y el alto para el tamaño del personaje
    '''

    #Creo un diccionario vacio para el personaje
    dict_personaje = {}

    #Cargo imagen 
    dict_personaje["surface"] = pygame.image.load('amogus.png')

    #para escalar la imagen acuerdo a la pantalla
    dict_personaje["surface"] = pygame.transform.scale( dict_personaje["surface"] , (ancho,alto))

    #agrego rectangulo para calcular la posicion y tamaño del personaje
    dict_personaje["rect_posicion"] = pygame.Rect(x, y, ancho, alto)

    #segundo rectangulo para calcular si colisiona
    dict_personaje["rect_colision"] = pygame.Rect((x+ancho/2)-10,y+90,40,20)

    #Para saber si el usuario esta mirando derecha o izquierda
    dict_personaje['mirando_derecha'] = True 

    #Guardo la superficie original(es decir sin mirar a otro lado)
    dict_personaje['surface_original'] = dict_personaje['surface']

    #devuelve todo el diccionario
    return dict_personaje

def actualizar_personaje(personaje,incremento_x):
    '''objetivo: Calcular la nueva posicion y actualizar, y verificar si esta colisionando su movimiento o no.
    
    parametros : 'personaje': el diccionario, y 'incremento_x': la cantidad de pasos
    '''

    #Hago una variable para calcular la cantidad de pasos que va a dar
    
    nueva_x = personaje["rect_posicion"].x + incremento_x

    #Si la cantidad de pasos que va a dar esta dentro del borde derecho o izquiero entonces sigue
    if(nueva_x > 0 and nueva_x < 800):

        #Se actualiza la posicion del personaje y se refleja en el proximo fotograma
        personaje["rect_posicion"].x = personaje["rect_posicion"].x + incremento_x

        #Mueve el rectangulo de colision, asi se actualiza con la imagen visual
        personaje["rect_colision"].x = personaje["rect_colision"].x + incremento_x

def actualizar_pantalla(dict_personaje, ventana):
    '''
    objetivo: Actualizar el personaje acorde a la posicion.

    parametros: 'dict_personaje': El diccionario del personaje, y 'ventana': la ventana del juego main
    
    '''
    ventana.blit(dict_personaje["surface"],dict_personaje["rect_posicion"])
