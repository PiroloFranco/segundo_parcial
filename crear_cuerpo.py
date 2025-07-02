import pygame
ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
NEGRO = (0, 0, 0)

def dibujar_cabeza():
    return pygame.draw.circle(VENTANA, NEGRO, (352, 430), 20, 4)
def dibujar_cuerpo():
    return pygame.draw.rect(VENTANA, NEGRO, (350, 450, 4, 50))
def dibujar_pierna_izquierda():
    return pygame.draw.line(VENTANA, NEGRO, (350, 500),(330, 540), 4)
def dibujar_pierna_derecha():
    return pygame.draw.line(VENTANA, NEGRO, (352, 500), (372, 540), 4)
def dibujar_brazo_izquierdo():
    return pygame.draw.line(VENTANA, NEGRO, (352, 460), (332, 470), 4)
def dibujar_brazo_derecho():
    return pygame.draw.line(VENTANA, NEGRO, (352, 460), (372, 470), 4)

def dibujar_cuerpo_por_parte(numero):
    match numero: 
        case 1:
            dibujar_cabeza()
        case 2:
            dibujar_cabeza()
            dibujar_cuerpo()
        case 3:
            dibujar_cabeza()
            dibujar_cuerpo()
            dibujar_pierna_izquierda()
        case 4:
            dibujar_cabeza()
            dibujar_cuerpo()
            dibujar_pierna_izquierda()
            dibujar_pierna_derecha()
        case 5:
            dibujar_cabeza()
            dibujar_cuerpo()
            dibujar_pierna_izquierda()
            dibujar_pierna_derecha()
            dibujar_brazo_izquierdo()
        case 6:
            dibujar_cabeza()
            dibujar_cuerpo()
            dibujar_pierna_izquierda()
            dibujar_pierna_derecha()
            dibujar_brazo_izquierdo()
            dibujar_brazo_derecho()
