import os,sys,importlib
from core.config import dirMapas,dirTerreno,colorBlack,pantallaAncho,pantallaAlto
from core.librerias.functions import relativeImportPath
from .maps import mapa_mundi
from core.db.conexion import Conexion
from .components import Tiles,SpriteStand,Panel,Muro
from .characters import Enemy

class Map:
    def __init__(self,surface,x=2,y=2):
        self.x = x # x del mapamundi
        self.y = y # y del mapamundi
        self.characters = {}
        self.allSprites = []
        self.setMapProps()
        self.setSurface(surface)
  

    #setea las propiedades del mapa: nombre, caracteristicas, etc...
    def setMapProps(self) -> None:
        print(dirMapas+mapa_mundi.mm[self.x][self.y])
        self.__module = relativeImportPath(dirMapas+mapa_mundi.mm[self.x][self.y]+'.py')
        self.map = self.__module.mapa
        self.nombre = self.__module.nombre
        self.characters = self.__module.characters
        self.miniMap = self.__module.mundi
        self.setMap()
        self.createCharacters()

    #setea el mapa con sus Sprites
    def setMap(self) -> None:
        for f in range(len(self.map)):
            for c in range(len(self.map[f])):
                con = Conexion()
                try:
                    dataTile = con.getDatosById('TILES',self.map[f][c])
                    if self.map[f][c] == 0:
                        tile = Muro('terreno/TILES',dataTile)
                    else:
                        tile = Tiles('terreno/TILES',dataTile)
                    tile.rect.x=c*25
                    tile.rect.y=f*25
                    self.map[f][c]=tile
                    self.allSprites.append(tile)
                except:
                    pass

    #dibuja el terreno del mapa
    def drawMap(self) -> None:
        for f in range(len(self.map)):
            for c in range(len(self.map[f])):
                self.surface.blit(self.map[f][c].image,(self.map[f][c].rect.x,self.map[f][c].rect.y))
                self.map[f][c].rect.x
                self.map[f][c].rect.y


    #propiedades de la superficie donde se dibuja el mapa
    def setSurface(self,surface) -> None:
        _height = len(self.map) * 25
        _widht = len(self.map[0]) * 25
        _x = pantallaAncho/2 - _widht/2
        _y = pantallaAlto/2 - _height/2
        self.surface = Panel(surface,_x,2,_widht,_height,colorBlack)
    
    #dibujar la superficie
    def drawSurface(self) -> None:
        self.surface.update()


    #setea las propiedades de todos los personajes del mapa
    def setCharacters(self) -> None:
        for ch in self.characters:
            ch['sprite'] = SpriteStand(f"characters/{ch['hoja']}",ch['tile'],ch['position'])
            self.allSprites.append(ch['sprite'])

    #dibujo los personajes en la ventana
    def drawCharacters(self, cursor, sprite) -> None:
        for ch in self.characters:
            #self.surface.blit(ch['sprite'].sprite.image,ch['sprite'].sprite.rect)
            self.surface.blit(ch['sprite'].image,ch['sprite'].rect)
            ch['sprite'].updateCharacter(self.surface, cursor, self.allSprites)


    #crear characters
    def createCharacters(self) -> object:
        for ch in self.characters:
            if ch['type'] == 'npc':
                ch['sprite'] = self.createNPC(ch)
            if ch['type'] == 'enemy':
                ch['sprite'] = self.createEnemy(ch)
            self.allSprites.append(ch['sprite'])

    #setea self.characters['sprite'] como un NPC
    def createNPC(self,character) -> object:
        return SpriteStand(f"characters/{character['hoja']}",character['tile'],character['position'])

    #setea self.characters['sprite'] como un Enemy
    def createEnemy(self,character) -> object:
        return Enemy(character['position'],character['class_id'],character['lvl'])
        #return Enemy(f"characters/{character['class_id']}",character['position'],character['lvl'])


    #setear sprite del jugador
    def setPlayer(self,player) -> None:
        self.player = player
        self.player.surfaceSprite = self.surface


    #cambio de mapa cuando el jugador llega al limite de surface
    def changeMap(self) -> None:
        change = False
        if self.player.rect.x <= 0:
            change = True
            self.y = self.y - 1
            self.player.rect.x = self.surface.width - 50
        elif self.player.rect.y <= 0:
            change = True
            self.x = self.x - 1
            self.player.rect.y = self.surface.height - 50
        elif self.player.rect.x >= self.surface.width - self.player.rect.width:
            change = True
            self.y = self.y + 1
            self.player.rect.x = 50
        elif self.player.rect.y >= self.surface.height - self.player.rect.height:
            change = True
            self.x = self.x + 1
            self.player.rect.y = 50

        if change:
            del self.__module
            self.allSprites = []
            self.setMapProps()


    #dibuja el sprite del jugador
    def drawPlayer(self, cursor, event) -> None:
        self.player.updateCharacter(self.surface, cursor, self.allSprites)
        #self.player.handleEvent(cursor)


    #dibuja todo lo que contenga el mapa
    def draw(self,cursor=None,event=None) -> None:
        self.drawSurface()
        self.drawMap()
        self.drawCharacters(cursor,self.allSprites)
        self.drawPlayer(cursor, event)
        self.changeMap()

    def getStarted(self) -> bool:
        return False