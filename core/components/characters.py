from .components import Tiles,SpriteMobile,Muro
from core.db.conexion import Conexion as cn
from core.config import LVLMAX,MOD
from math import floor,ceil
import pygame as py
from numpy import random

class Ente():
    def __init__(self,hoja,tile) -> None:
        self.sprite = Tiles(hoja,tile)


class NPC(Ente):
    def __init__(self,hoja,tile) -> None:
        super().__init__(hoja,tile)

    #Acciones de NPC
    def interact(self) -> None:
        pass


class Character(SpriteMobile):
    def __init__(self, hoja, tile, position, classId, lvl) -> None:
        super().__init__(hoja,tile,position)
        self.classId = classId

        self.LVL = int(lvl)
        self.expMax = 100
        self.setMOD()
        self.setExpMax()
        self.direction = str('left')
        self.accion = str('stand')

        self.setCharacterClass()
        self.setPrimaryStats()
        self.setSecondaryStats()

        self.statsPrincipales = {
            'STR' : self.STR,
            'DEF' : self.DEF,
            'CON' : self.CON,
            'DEX' : self.DEX
        }

        self.statsSecundarios = {
            'HPMAX' : self.HPMAX,
            'HP' : self.HP,
            'ENEMAX' : self.ENEMAX,
            'ENE' : self.ENE,
            'DMG' : self.DMG,
            'PDEF' : self.PDEF,
            'BLO' : self.BLO,
            'AGI' : self.AGI,
            'SPE' : self.SPE,
            'CRIT' : self.CRIT,
            'PCRIT' : self.PCRIT
        }


        print(self.statsPrincipales,self.statsSecundarios,{'LVL':self.LVL, 'VEL':self.velocidad})

    #seteo clase del personaje
    def setCharacterClass(self) -> None:
        self.data = cn().getDatosById('CLASES',self.classId)

    #seteo de atributos principales        
    def setPrimaryStats(self) -> None:
        self.CLASS_NAME = self.data['CLASE']
        self.STR = self.data['STR']
        self.DEF = self.data['DEF']
        self.CON = self.data['CON']
        self.DEX = self.data['DEX']
        self.MIN_LVL = self.data['LVL']

    #seteo de atributos secuandarios
    def setSecondaryStats(self) -> None:
        '''
        self.HPMAX = self.setHPMAX()
        self.HP = ceil(self.HPMAX)
        self.ENEMAX = ceil(self.DEX*self.MOD)
        self.ENE = ceil(self.ENEMAX)
        self.DMG = ceil(self.STR*self.MOD)
        self.PDEF = ceil(self.DEF*self.MOD)
        self.BLO = ceil(self.DEF*0.3)
        self.AGI = ceil(((self.DEX+self.STR)/2)*self.MOD)
        self.SPE = ceil(self.DEX*self.MOD)
        self.CRIT = ceil(self.DMG*(1+self.MOD))
        self.PCRIT = ceil(self.DEX*self.MOD)
        '''
        self.HPMAX = self.setHPMAX()
        self.HP = ceil(self.HPMAX)
        self.ENEMAX = ceil(self.DEX * MOD * self.LVL)
        self.ENE = ceil(self.ENEMAX)
        self.DMG = ceil(self.STR * MOD * self.LVL)
        self.PDEF = ceil(self.DEF * MOD * self.LVL)
        self.BLO = ceil(self.DEF * MOD * self.LVL)
        self.AGI = ceil(((self.DEX+self.STR)/2)*0.1)
        self.SPE = ceil(self.DEX*0.1)
        self.CRIT = ceil(self.DMG*(1.1))
        self.PCRIT = ceil(self.DEX*0.1)
        self.velocidad = ceil((LVLMAX-self.LVL) - self.DEX / MOD)


    #setea la vida maxima del personaje
    def setHPMAX(self) -> int:
        HPMAX = ceil(self.CON * MOD * self.LVL)
        if HPMAX < 10:
            return 10
        return HPMAX

    #set Modificador para setear atributos
    def setMOD(self) -> None:
        self.MOD = ceil(LVLMAX-self.LVL/MOD)

    #set Experiencia por nivel
    def setExpMax(self) -> None:
        if self.LVL >= 1:
            self.expMax = 100 + (self.LVL*10)

    #dano del personaje
    def atacar(self, target) -> int:
        dmg = self.DMG / target.PDEF
        return ceil(dmg)

    #actualizar estados acciones del jugafdor
    def updateCharacter(self, surface, cursor, sprite = []) -> None:
        self.draw(surface)
        self.handleEvent(cursor, sprite)

    #dibujar personaje
    def draw(self,surface) -> None:
        surface.blit(self.image,self.rect)

        self.debug.fill((255,255,255,128))                         # notice the alpha value in the color
        surface.blit(self.debug, (self.rect.x,self.rect.y))

        '''
        if colicion and self.distancia > 0:
            self.distancia = self.distancia * -1
            print('choco con muro')
            print(f'vel: {self.distancia}')
        elif self.distancia < 0 and colicion == False:
            self.distancia = self.distancia * -1
            print('No choco con muro')
            print(f'vel: {self.distancia}')


        if isinstance( h, (Muro) ) and self.distancia > 0:
            print(f'Distabcia: {self.distancia}')
            print(f'hits {self.hits} \n')
            return False
        elif self.distancia < 0 and isinstance( h, (Muro) ):
            self.distancia = self.distancia * -1
            print('Me aleje del muro')
            return False
        '''

    #eventos de teclado/mouse
    def handleEvent(self, cursor, sprite) -> None:
        pass

class Enemy(Character):
    def __init__(self,id,lvl):
        self.id = id
        super().__init__(self.SPRITE,self.tile,self.classID,lvl)

    def setEnemyData(self):
        con = cn()
        data = con.getDatosById('ENEMIGOS',self.id)
        self.classID = data['ID_CLASE']
        self.NOMBRE = data['NOMBRE']
        self.SPRITE = data['SPRITE']
        self.DIALOGO = data['DIALOGO']
        self.EXP = data['EXP']


class Player(Character):
    def __init__(self, db) -> None:
        self.db= db
        #super().__init__(hoja, tile, position, classId, lvl, exp)
        self.getPlayer()
        tiles = {'X':18, 'Y':588, 'WIDTH':29, 'HEIGHT':47}
        super().__init__('cuerpo/modelo', tiles, (self.stats['X'], self.stats['Y']), self.stats['ID_CLASE'], self.stats['LVL'])


    def getPlayer(self):
        from core.db.conexion import CargarPartida as cp
        pjData = cp(self.db).Cargar()
        self.stats = pjData[0][0].copy()
        self.invt = pjData[1][0].copy()

        self.exp = self.stats['EXP']


    

    def handle_event(self, cursor, sprite) -> None:
        
        event = py.key.get_pressed()
        mouse_event = py.mouse.get_pressed()

        self.accion = 'stand'
        self.distancia = floor(self.SPE)
        distancia = self.distancia
        
                
        if event[py.K_LEFT]:
            self.direction = 'left'
            self.accion = 'move'
        elif event[py.K_RIGHT]:
            self.direction = 'right'
            self.accion = 'move'
        elif event[py.K_UP]:
            self.direction = 'up'
            self.accion = 'move'
        elif event[py.K_DOWN]:
            self.direction = 'down'
            self.accion = 'move'
        elif event[py.K_SPACE]:
            self.accion = 'atack_sword'
            velAtak = ceil((LVLMAX-self.LVL) - self.AGI / MOD)
            distancia = 0
            self.updateSprite(sprite, self.direction, self.accion, distancia, velAtak)

        if event[py.K_i]:
            print('Inventario')
        
        '''
            self.inventario.cambiarEstado()
            if event.text == "i" or event.text == "I":        
        '''
        if mouse_event[0]:
            print('Click izquierdo')
        if mouse_event[1]:
            print('Click centro')
        if mouse_event[2]:
            print('Click derecho')

        if self.accion != 'stand':
            self.updateSprite(sprite, self.direction, self.accion, distancia, self.velocidad)
        else:
            self.updateSprite(sprite, self.direction, self.accion)

class Enemy(Character):
    #def __init__(self,id,lvl):
    def __init__(self, position, classId, lvl):
        self.position = position
        self.tile = {'X':12,'Y':590,'WIDTH':43,'HEIGHT':50}
        self.setEnemyData(classId)
        #super().__init__(self.SPRITE,self.tile,self.classID,lvl)
        super().__init__(f"characters/{self.SPRITE}", self.tile, self.position, self.classID, lvl)


    def setEnemyData(self, id):
        con = cn()
        data = con.getDatosById('ENEMIGOS',id)
        self.classID = data['ID_CLASE']
        self.NOMBRE = data['NOMBRE']
        self.SPRITE = data['SPRITE']
        self.DIALOGO = data['DIALOGO']
        self.EXP = data['EXP']

    def handleEvent(self, cursor, sprite):
        
        self.moveEvent()
        self.distancia = floor(self.SPE)
        distancia = self.distancia
        
                
        if self.move:
            self.updateSprite(sprite, self.direction, self.accion, distancia, self.velocidad)
        else:
            self.updateSprite(sprite, self.direction, self.accion)

        '''
        if event[py.K_SPACE]:
            self.accion = 'atack_sword'
            velAtak = ceil((LVLMAX-self.LVL) - self.AGI / MOD)
            distancia = 0
            self.updateSprite(sprite, self.direction, self.accion, distancia, velAtak)
        '''
            

    def moveEvent(self) -> None:
        move = random.randint(100)
        if move <= 49:
            self.move = False
        else:
            self.move = True
            self.accion = 'move'
            self.setDirection()
            py.time.delay(random.randint(1000,3000))
        print(move)

    def setDirection(self):
        listDirections = ['left','right','up','down']
        self.direccion = listDirections[random.randint(0,len(listDirections)-1)]
