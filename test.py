from core.components.components import Panel,BarraInferriro
from core.components.characters import Player
from core.config import pantallaAncho,pantallaAlto,colorBlackMiddleDark,colorBlackMiddleLight,colorBlackMiddle
import pygame
'''
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

pj = Player('Ushoa')

EXPactual = pj.exp
EXPmax = pj.expMax
HPactual = pj.HP
HPmax = pj.HPMAX
ENEactual = pj.ENE
ENEmax = pj.ENEMAX




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



    barraInferior.update(EXPactual, EXPmax, ENEactual, ENEmax, HPactual, HPmax)
    mapa.update()
    #pygame.draw.rect(contENE, BLANCO, (10, 10, 50, 50), border_radius = 90)
    
    # Actualiza el contenido de la pantalla.
    pygame.display.flip()

pygame.quit()

'''
import pygame

from pygame.locals import * 
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

font = pygame.font.SysFont("arial", 32); 
font_height = font.get_linesize()

while True:

    for event in pygame.event.get(): 
        if event.type == QUIT: exit()

    screen.fill((255, 255, 255))

    pressed_key_text = []

    pressed_keys = pygame.key.get_pressed()

    y = font_height

    for key_constant, pressed in enumerate(pressed_keys): 
        if pressed:

            key_name = pygame.key.name(key_constant)

            text_surface = font.render(f"{key_name} pressed: {key_constant}", True, (0,0,0)) 
            key = pressed_keys.index(1)
            print(key)
            print(pressed_keys[key_constant])
            screen.blit(text_surface, (8, y))
            y = font_height

    pygame.display.update()