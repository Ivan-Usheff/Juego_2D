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

    stage.update(cursor, input_event)
    
    # }

    event.clear()
    fps.tick(60)
    display.set_caption(f'Juego en "2D"{fps}')
    display.flip()
    display.update()