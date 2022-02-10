from core.components.components import Panel,Barra,BarraStats,BarraInferriro
from core.config import pantallaAncho,pantallaAlto,colorBlackMiddleDark,colorBlackMiddleLight,colorBlackMiddle
import pygame

#Tamaño de pantalla
ANCHO = 1200
ALTO = 610

#FPS
FPS = 30

# Paleta de colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)
H_FA2F2F = (250,47,47)
VERDE= (0,255,0)
AZUL = (0,0,255)
H_50D2FE = (94,210,254)


# Inicialización de Pygame, creación de la ventana, título y control de reloj.
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Trabajando con sprites")
clock = pygame.time.Clock()

#cl = Circulo(pantalla, 50, 50, 50, 50, colorBlack, 90)

barraInferior = BarraInferriro(pantalla)
mapa = Panel(pantalla, pantallaAncho/2 - 800/2, 2, 800, 525, colorBlackMiddle)

EXPactual = 239
EXPmax = 1000
HPactual = 100
HPmax = 268
ENEactual = 65
ENEmax = 3267




# Bucle de juego
ejecutando = True
while ejecutando:
    # Es lo que especifica la velocidad del bucle de juego
    clock.tick(FPS)
    # Eventos
    for event in pygame.event.get():
        # Se cierra y termina el bucle
        if event.type == pygame.QUIT:
            ejecutando = False
        
    event = pygame.key.get_pressed()

    if event[pygame.K_LEFT]:
        HPactual -= 5
    elif event[pygame.K_RIGHT]:
        HPactual += 5
    elif event[pygame.K_UP]:
        HPmax += 5
    elif event[pygame.K_DOWN]:
        HPmax -= 5
        

    # Fondo de pantalla, dibujo de sprites y formas geométricas.
    pantalla.fill(AZUL)
    barraInferior.update(ENEactual, ENEmax, EXPactual, EXPmax, HPactual, HPmax)
    mapa.update()
    #pygame.draw.rect(contENE, BLANCO, (10, 10, 50, 50), border_radius = 90)
    
    # Actualiza el contenido de la pantalla.
    pygame.display.flip()

pygame.quit()
