import pygame as py
import sys
from .components import TextBoton,Panel,OpcionSecundaria,Input
from core.config import colorComponentChild,colorBlack,fuenteTituloJuego,fuenteButtons
from core.db.conexion import CargarPartida


class ButtonStart(OpcionSecundaria):
    def __init__(self,surface: Panel) -> None:
        super().__init__(surface)
        self.bInput = Input(self.surface,45,45,740,60)
        bCreate = TextBoton(self.surface,350,360,160,50,'Crear',fuenteButtons,colorBlack,self.functionCreate)

        self.subcomps = [self.bInput,bCreate]
        self.n = 0


    def functionCreate(self) -> None:
        try:
            con = CargarPartida(self.bInput.texto)
            if self.n<1:
                con.Crear()
                self.n+=1
                self.data = self.bInput.texto
        except:
            print('Inserte un Nombre')
        self.start = True


class ButtonLoad(OpcionSecundaria):
    def __init__(self,surface: Panel) -> None:
        super().__init__(surface)
        self.saves = []

        self.createButtons()
        
        self.subcomps = self.saves


    def createButtons(self) -> None:
        con = CargarPartida()
        x = 45
        y = 30
        for s in con.partidas:
            self.saves.append(TextBoton(self.surface,x,y,160,50,s,fuenteButtons,colorBlack,self.getStarted))
            y+=80

    def getStarted(self) -> None:
        for player in self.subcomps:
            if player.getCliqued():
                self.data = player.text
        self.start = True


class ButtonQuit(OpcionSecundaria):
    def __init__(self,surface: Panel):
        super().__init__(surface)
        acept = TextBoton(self.surface,200,50,160,50,'Yes',fuenteButtons,colorBlack,self.functionQuit)
        deny = TextBoton(self.surface,380,50,160,50,'No',fuenteButtons,colorBlack,self.functionDeny)

        self.subcomps = [acept,deny]


    def functionDeny(self) -> None:
        print('Cerrar este panel')

    def functionQuit(self) -> None:
        py.quit()
        sys.exit()


class MenuPrincipal:
    def __init__(self,surface: Panel) -> None:
        self.surface = surface
        self.textSurface = fuenteTituloJuego.render('Juego 2D', True, (0, 0, 0))
        self.canvas = Panel(surface,50,120,250,430,colorComponentChild)

        self.buttonStart = TextBoton(self.canvas,45,30,160,50,'Start',fuenteButtons,colorBlack,self.functionStart)
        self.buttonLoad = TextBoton(self.canvas,45,110,160,50,'Load',fuenteButtons,colorBlack,self.functionSaves)
        self.buttonConfig = TextBoton(self.canvas,45,190,160,50,'Config',fuenteButtons,colorBlack)
        self.buttonCredits = TextBoton(self.canvas,45,270,160,50,'Credits',fuenteButtons,colorBlack)
        self.buttonQuit = TextBoton(self.canvas,45,350,160,50,'Quit',fuenteButtons,colorBlack,self.functionQuit)

        self.canvasChild = Panel(self.surface,330,120,820,430)
        self.opcionSecundaria = None
    
    def update(self,cursor, input_event, _event) -> None:
        self.surface.blit(self.textSurface,(500,50))
        self.canvas.update()
        self.buttonStart.update(cursor, input_event)
        self.buttonLoad.update(cursor)
        self.buttonConfig.update(cursor)
        self.buttonCredits.update(cursor)
        self.buttonQuit.update(cursor)
        self.showSecundario(cursor,input_event,_event)

    def showSecundario(self,cursor,input_event,_event) -> None:
        if self.opcionSecundaria != None:
            self.opcionSecundaria.update(cursor,input_event,_event)

    def functionQuit(self) -> None:
        self.opcionSecundaria = ButtonQuit(self.canvasChild)

    def functionStart(self) -> None:
        self.opcionSecundaria = ButtonStart(self.canvasChild)

    def functionSaves(self) -> None:
        self.opcionSecundaria = ButtonLoad(self.canvasChild)
    
    def getStarted(self) -> bool:
        if self.opcionSecundaria != None:
            return self.opcionSecundaria.start
        return False
