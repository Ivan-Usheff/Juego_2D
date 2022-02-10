from .components.menu_principal import MenuPrincipal

class Stage:
    def __init__(self,window):
        self.window = window
        self.setMenuPrincipal()
        self.pj = ''

    #setea show para que se muestre le menu princiapl al iniciar el juego
    def setMenuPrincipal(self) -> None:
        self.show = MenuPrincipal(self.window)

    #muestra el Menu Principal
    def updateMM(self,cursor,_event) -> None:
        self.show.update(cursor,_event)
        self.getStarted()

    #consulta si en menu principal empieza con el juego
    #y hace swich de la prop show
    def getStarted(self) -> None:
        if self.show.getStarted():
            pjData = self.show.opcionSecundaria.data
            print(pjData)
            self.setGame(pjData)

    #seta el escenario para que empiece el juego
    def setGame(self, pjData) -> None:
        from .db.conexion import CargarPartida as cp
        from .components.map import Map
        from .components.characters import Character as ch
        pjData = cp(pjData)
        self.pj = pjData.Cargar()
        tiles = {'X':18, 'Y':588, 'WIDTH':46, 'HEIGHT':47}
        personaje = ch('cuerpo/modelo',tiles,(self.pj[0][0]['X'],self.pj[0][0]['Y']),self.pj[0][0]['ID_CLASE'],self.pj[0][0]['LVL'])
        self.show = Map(self.window,self.pj[0][0]['MAPA_X'],self.pj[0][0]['MAPA_Y'])
        self.show.setPlayer(personaje)

    #muestra el juego
    def updateGame(self,cursor,_event) -> None:
        self.show.draw(cursor,_event)

    #comprueba la instacia de show y cambia el comportamiento
    def update(self,cursor,_event) -> None:
        if isinstance(self.show, MenuPrincipal):
            self.updateMM(cursor,_event)
        else:
            self.updateGame(cursor,_event)