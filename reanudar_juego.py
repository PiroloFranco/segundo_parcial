import pygame
import time

def reanudar_juego():

    pygame.init()

    ANCHO = 1000
    ALTO = 800
    BLANCO = (255, 255, 255)
    GRIS = (143, 143, 143)
    NEGRO = (0, 0, 0)

    VENTANA = pygame.display.set_mode((ANCHO, ALTO))
    FUENTE = pygame.font.SysFont(None, 48)
    CUADRADO_1 = pygame.Rect(395, 425, 45, 40)
    CUADRADO_2 = pygame.Rect(495, 425, 55, 40)
    bandera_juego = True

    while bandera_juego:

        VENTANA.fill(BLANCO)

        texto = FUENTE.render("Desea seguir jugando?",True,NEGRO)
        texto_1 = FUENTE.render("Si",True,NEGRO)
        texto_2 = FUENTE.render("No",True,NEGRO)

        VENTANA.blit(texto,(300, 350))
        VENTANA.blit(texto_1,(400,430))
        VENTANA.blit(texto_2,(500,430))

        pygame.draw.rect(VENTANA, BLANCO , CUADRADO_1,3)
        pygame.draw.rect(VENTANA, BLANCO , CUADRADO_2,3)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                bandera_juego = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if CUADRADO_1.collidepoint(evento.pos):
                    texto_1 = FUENTE.render("Si", True, GRIS)
                    VENTANA.blit(texto_1, (400, 430))
                    pygame.display.update()
                    time.sleep(0.2)
                    return True
                if CUADRADO_2.collidepoint(evento.pos):
                    texto_2 = FUENTE.render("No", True, GRIS)
                    VENTANA.blit(texto_2,(500,430))
                    pygame.display.update()
                    time.sleep(0.2)
                    return False

        pygame.display.update()
    pygame.quit()

reanudar_juego()
