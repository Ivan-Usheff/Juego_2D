from pygame import event,time,quit,QUIT,display,init,K_ESCAPE,KEYDOWN,key
import sys 


class Stage:
    def __init__(self,window):
        self.window = window
        from .components.menu_principal import MenuPrincipal
        self.menuPrincipal = MenuPrincipal(self.window)
        self.pjData = None
        self.mapa = None
        self.event = key.get_pressed()


    def updateMenuPrincipal(self, cursor, input_event, event):
        self.menuPrincipal.update(cursor, input_event, event)

        
    def createMapa(self):
        from core.components.map import Map
        self.mapa = Map(self.window,self.pjData[0][0]['MAPA_X'],self.pjData[0][0]['MAPA_Y'])
        self.mapa.setPlayer(self.personaje)

    def createPj(self):
        from core.db.conexion import CargarPartida as cp
        self.pjData = cp(self.pjData).Cargar()
        from core.components.characters import Character as ch
        tiles = {'X':18, 'Y':588, 'WIDTH':29, 'HEIGHT':47}
        self.personaje = ch('cuerpo/modelo',tiles,(self.pjData[0][0]['X'],self.pjData[0][0]['Y']),self.pjData[0][0]['ID_CLASE'],self.pjData[0][0]['LVL'],self.pjData[0][0]['EXP'])

    def createBarraInferiror(self):
        from core.components.components import BarraInferriro as BI
        self.barraInferiro = BI(self.window)

    def createPanelStats(self):
        pass

    def createPanelInventario(self):
        pass



    def updateGame(self, cursor, _event):
        self.mapa.draw(cursor,_event)
        self.barraInferiro.update(self.personaje.exp,self.personaje.expMax,self.personaje.HP,self.personaje.HPMAX,self.personaje.ENE,self.personaje.ENEMAX)

    #seta el escenario para que empiece el juego
    def setGame(self) -> None:
        self.createPj()
        self.createMapa()
        self.createBarraInferiror()
        print(self.pjData[0][0])

    #comprueba la instacia de show y cambia el comportamiento
    def update(self, cursor, input_event) -> None:
        
        if self.menuPrincipal and self.menuPrincipal.getStarted() != True:
            self.updateMenuPrincipal(cursor, input_event, self.event)
        elif self.mapa:
            self.updateGame(cursor,self.event)
        else:
            if self.pjData != None:
                if not isinstance(self.pjData,tuple):
                    self.setGame()
            elif self.pjData == None:
                self.pjData = self.menuPrincipal.opcionSecundaria.data
                
            if self.event[K_ESCAPE]:
                quit()
                sys.exit()
