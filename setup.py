from core.components.components import Cursor as cr
from core.config import ventana,colorBG
from core.stage import Stage as st
from pygame import event,time,quit,QUIT,display,init
import sys 

init()

fps=time.Clock()
cursor = cr()

stage = st(ventana)



while True:
    ventana.fill(colorBG)
    cursor.update()

    for Event in event.get():
        input_event = Event
    
    if input_event.type == QUIT:
        quit()
        sys.exit()
        
    #LLAMADAS A FUNCIONALIDADES DEL JUEGO {

<<<<<<< HEAD
    stage.update(cursor, input_event)
=======
    if menuPrincipal.getStarted() != True:
        menuPrincipal.update(cursor,_event)
    else:
        if pjData != None:
            if not isinstance(pjData,tuple):

                from core.components.characters import Player as pr
                tiles = {'X':18, 'Y':588, 'WIDTH':29, 'HEIGHT':47}
                #personaje = pr('cuerpo/modelo',tiles,(pjData[0][0]['X'],pjData[0][0]['Y']),pjData[0][0]['ID_CLASE'],pjData[0][0]['LVL'],pjData[0][0]['EXP'])
                personaje = pr(pjData)


                from core.components.map import Map
                mapa = Map(ventana,pjData[0][0]['MAPA_X'],pjData[0][0]['MAPA_Y'])
                mapa.setPlayer(personaje)
                
                from core.components.components import BarraInferriro as BI
                barraInferiro = BI(ventana)

                print(pjData[0][0])
        elif pjData == None:
            pjData = menuPrincipal.opcionSecundaria.data

        if mapa:
            mapa.draw(cursor,_event)
            barraInferiro.update(personaje.exp,personaje.expMax,personaje.HP,personaje.HPMAX,personaje.ENE,personaje.ENEMAX)
            
        if _event.type == KEYDOWN and _event.key == K_ESCAPE:
            quit()
            sys.exit()
>>>>>>> 829db90e465c1c20e0e48e054576335ea2382c59
    
    # }

    event.clear()
    fps.tick(60)
    display.set_caption(f'Juego en "2D"{fps}')
    display.flip()
    display.update()