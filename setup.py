from core.components.components import Cursor as cr
from core.components.menu_principal import MenuPrincipal
from core.config import ventana,colorBG
from pygame import event,time,quit,QUIT,KEYDOWN,K_ESCAPE,display,init
import sys 


fps = time.Clock()
cursor = cr()
menuPrincipal = MenuPrincipal(ventana)
pjData = None
mapa = None
personaje = None

init()

while True:
    ventana.fill(colorBG)
    cursor.update()

    for Event in event.get():
        input_event = Event
    
    if input_event.type == QUIT:
        quit()
        sys.exit()
        
    #LLAMADAS A FUNCIONALIDADES DEL JUEGO {

    if menuPrincipal.getStarted() != True:

        menuPrincipal.update(cursor,input_event)
    
    elif not mapa and not personaje:
    
        if pjData != None:
            
            if not isinstance(pjData,tuple):

                from core.components.characters import Player as pr
                tiles = {'X':18, 'Y':588, 'WIDTH':29, 'HEIGHT':47}
                personaje = pr(pjData, fps)


                from core.components.map import Map
                mapa = Map(ventana,personaje.stats['MAPA_X'],personaje.stats['MAPA_Y'],fps)
                mapa.setPlayer(personaje)
                
                from core.components.components import BarraInferriro as BI
                barraInferiro = BI(ventana)

        elif pjData == None:
    
            pjData = menuPrincipal.opcionSecundaria.data
    
    else:

        mapa.draw(cursor,input_event)
        barraInferiro.update(personaje.exp,personaje.expMax,personaje.HP,personaje.HPMAX,personaje.ENE,personaje.ENEMAX)
        
    if input_event.type == KEYDOWN and input_event.key == K_ESCAPE:

        quit()
        sys.exit()
    
    # }

    event.clear()
    fps.tick(60)
    display.set_caption(f'Juego en "2D"{fps}')
    display.flip()
    display.update()