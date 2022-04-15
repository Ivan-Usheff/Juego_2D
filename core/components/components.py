from typing import Any
import pygame as py
import sys
import random
from core.config import colorButton, colorComponentClick, colorComponentOver, colorComponent, colorBlackMiddle, colorBlackMiddleLight, colorWhite, fuenteButtons, colorBlack, fuenteStats, colorHPBar, colorENEBar, colorEXPBar, colorBlackMiddleDarkPluss, pantallaAncho, pantallaAlto


class Cursor(py.Rect):
    """
    Se define un cuadrado de 5x5 para el mouse
    """

    def __init__(self):
        py.Rect.__init__(self, 0, 0, 5, 5)

    """
    se actualiza la posicion en X e Y del cuadrado 
    segun la posicion de mouse
    """

    def update(self) -> None:
        self.left, self.top = py.mouse.get_pos()


class Rectangle(py.Rect):
    """
    Creacion de un rectagulo segun los parametros necesarios
    """

    def __init__(self, surface, x, y, width, height, color):
        self.surface = surface
        self.left = x
        self.top = y
        self.width = width
        self.height = height
        self.color = color

        super().__init__(self.surface.x+self.x, self.surface.y+self.y, self.width, self.height)

    def draw(self):
        py.draw.rect(self.surface, self.color, self)

    # methodo para definir el comportamiento del objeto
    def behavior(self, cursor=None) -> None:
        pass

    def update(self, cursor=None, event=None) -> None:
        self.behavior(cursor)
        self.draw()


class Circulo(Rectangle):
    def __init__(self, surface, x, y, width, height, color=colorBlack, border=90, padre=None) -> None:
        super().__init__(surface, x, y, width, height, color)
        self.padre = padre
        self.border = border

    def draw(self):
        if self.padre:
            py.draw.rect(self.surface, self.color, self.padre,
                         border_radius=self.border)
        else:
            py.draw.rect(self.surface, self.color, self,
                         border_radius=self.border)


class Button(Rectangle):
    """
    Boton sencillo que cambia de color al 'Over', 'Click' y vuelve a su color normal
    """

    def __init__(self, surface, x, y, width, height, action=None, color=colorButton):
        super().__init__(surface, x, y, width, height, color)
        self._baseColor = color
        self.action = action
        self._clic = False

    # devuelve true si se hace click
    def getClicked(self) -> bool or None:
        if self._clic == True:
            return True
        else:
            return None

    # cambia a su color normal
    def normalColor(self) -> None:
        self.color = self._baseColor

    # cambia a su color Over
    def colorOver(self) -> None:
        self.color = colorComponentOver

    # cambia a su color Click
    def colorClick(self) -> None:
        self.color = colorComponentClick

    # comportamiento particular
    def behaviorNormal(self) -> None:
        pass

    # comportamiento particular si mouse Over
    def behaviorOver(self) -> None:
        pass

    # comportamiento particular si mouse Click
    def behaviorClick(self) -> None:
        pass

    def do_action(self) -> None:
        if self.action != None:
            self.action()

    # Renderizar algo
    def renderSomething(self):
        pass

    # Comportamiento normal de un boton
    def behavior(self, cursor=None) -> bool or None:
        py.event.pump()
        _colicion = cursor.colliderect(self.rect)
        click = py.mouse.get_pressed()
        if _colicion:
            self.colorOver()
            self.behaviorOver()
            py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
            # if event.type == py.MOUSEBUTTONUP and event.button == 1:
            if click[0]:
                self.do_action()
                self._clic = False
            else:
                # if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                self._clic = True
                self.colorClick()
                self.behaviorClick()
        else:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)
            self.normalColor()
            self.behaviorNormal()
            self._clic = False


class Panel(py.Surface):
    def __init__(self, source, x, y, width, height, color=colorComponent):
        super().__init__((width, height))
        self.source = source
        self.x = x
        self.y = y
        self.dest = (self.x, self.y)
        self.width = width
        self.height = height
        self.color = color
        self.hijos = []
        # self.autoAgregarHijos()

    # Agrega a la cola de hijos del surface recivido
    # siempre que sea un surface de tipo Panel
    def autoAgregarHijos(self) -> None:
        try:
            self.source.addChild(self)
        except Exception as e:
            print(
                f"Source no es de tipo Panel \n-Surface type: {type(self.source)}\n-{e}")

    # Recibe un objeto de tipo Panel y lo agraga a la cola de hijos

    def addChild(self, surface) -> None:
        self.hijos.append(surface)

    # Devuelve True si tien hijos el Panel
    def hasChild(self) -> bool:
        if self.hijos != []:
            return True
        return False

    # Dibuja sus hijos
    def drawChild(self) -> None:
        [h.update() for h in self.hijos]

    # dibja el Panel
    def update(self) -> None:
        self.source.blit(self, self.dest)
        self.fill(self.color)
        self.drawChild()


class TextBoton(py.Rect):
    def __init__(self, surface, x, y, width, height, text, fuente, textColor, action=None, color=colorButton):
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.text = text
        self._baseColor = color
        self.action = action
        py.Rect.__init__(self, self.x, self.y, self.width, self.height)

        self.fuente = fuente
        self.textColor = textColor
        self.texto_show = self.fuente.render(self.text, True, self.textColor)
        self.textX = self.x+(self.width-self.texto_show.get_width())/2
        self.textY = self.y+(self.height-self.texto_show.get_height())/2

        self.rectangulo = py.Rect(
            self.surface.x+self.x, self.surface.y+self.y, self.width, self.height)

    def draw(self) -> None:
        py.draw.rect(self.surface, self.color, self)
        self.surface.blit(self.texto_show, (self.textX, self.textY))

    # cambia a su color normal
    def normalColor(self) -> None:
        self.color = self._baseColor

    # cambia a su color Over
    def colorOver(self) -> None:
        self.color = colorComponentOver

    # cambia a su color Click
    def colorClick(self) -> None:
        self.color = colorComponentClick

    def update(self, cursor, event = None, input_event = None) -> None:
        self.draw()
        self.cursor = cursor
        py.event.pump()
        click = py.mouse.get_pressed()
        colicion = self.cursor.colliderect(self.rectangulo)
        if colicion:
            self.colorOver()
            if click[0]:
                self.colorClick()
                self.do_action()
            else:
                self.colorOver()
        else:
            self.normalColor()

    # ejecuta la accion/funcion dada
    def do_action(self) -> Any:
        if self.action != None:
            self.action()
            return self.action()

    # si coliciona devuelve True
    def getCliqued(self) -> bool:
        click = py.mouse.get_pressed()
        if self.cursor.colliderect(self.rectangulo):
            if click[0]:
                return True
        return False


class Input(py.Rect):
    def __init__(self, stage, x, y, ancho, alto, color=colorBlackMiddle, texto=''):
        py.Rect.__init__(self, x, y, ancho, alto)
        self.stage = stage
        self.ancho = ancho
        self.alto = alto
        self.x = x
        self.y = y
        self.color = py.Color(color)
        self.color_normal = self.color
        self.clic = False
        self.escribir = True

        self.texto = texto
        self.fuente = py.font.SysFont(' ', 35)
        self.texto_show = self.fuente.render(self.texto, True, (255, 255, 255))

        self.rectangulo = py.Rect(
            self.stage.x+self.x, self.stage.y+self.y, self.ancho, self.alto)

    def draw(self):
        py.draw.rect(self.stage, self.color, self)
        self.stage.blit(self.texto_show, (self.x+10, (self.y +
                        (self.alto-self.fuente.size(self.texto)[1])/2)))

    def click(self):
        self.color = colorBlackMiddleLight
        self.clic = True

    def normal(self):
        self.color = self.color_normal
        self.clic = False

    def update(self, cursor, input_event):
        self.mouse_event = py.mouse.get_pressed()
        self.draw()
        self.colicion = cursor.colliderect(self.rectangulo)

        self.changeColor(input_event)
        self.setInput( input_event)

        self.texto_show = self.fuente.render(self.texto, True, colorWhite)

    def changeColor(self, event):
        if self.colicion and event.type == py.MOUSEBUTTONDOWN and self.mouse_event[0]:
            self.click()
        elif not self.colicion and event.type == py.MOUSEBUTTONUP and self.mouse_event[0]:
            self.normal()
        else:
            pass

    def setInput(self, event):
        if self.clic:
            if event.type == py.KEYDOWN and event.key == 8 and self.escribir:
                self.deleteCharater()
                self.deshabilitarEscribir()
            if event.type == py.TEXTINPUT and self.escribir:
                self.inserText(event.text)
                print(self.texto)
                self.deshabilitarEscribir()
            if event.type == py.KEYUP:
                self.habilitarEscribir()

    def deshabilitarEscribir(self):
        self.escribir = False

    def habilitarEscribir(self):
        self.escribir = True

    def deleteCharater(self):
        self.texto = self.texto[:-1]

    def inserText(self, text):
        if len(self.texto) < 10:
            self.texto += text


class OpcionSecundaria:
    def __init__(self, surface,):
        self.surface = surface
        self.subcomps = []
        self.start = False
        self.data = ''

    def update(self, cursor, input_event) -> None:
        self.surface.update()
        for sub in self.subcomps:
            sub.update(cursor, input_event)


class Tiles(py.sprite.Sprite):
    def __init__(self, hoja, tiles):
        super().__init__()
        self.hoja = py.image.load(f"./img/{hoja}.png")
        self.hoja.set_clip(
            py.Rect(tiles['X'], tiles['Y'], tiles['WIDTH'], tiles['HEIGHT']))
        self.image = self.hoja.subsurface(self.hoja.get_clip())
        self.rect = self.image.get_rect()

    def update(self, x, y) -> None:
        self.rect.x += x
        self.rect.y += y


class Muro(Tiles):
    def __init__(self, hoja, tiles):
        super().__init__(hoja, tiles)


class SpriteStand(Tiles):
    def __init__(self, hoja, tile, position):
        super().__init__(hoja, tile)
        self.rect.midbottom = position


class SpriteMobile(Tiles):
    def __init__(self, hoja, tiles, position, tiempo):
        super().__init__(hoja, tiles)
        self.rect.topleft = position
        self.frame = 0

        self.tiempo = tiempo
        self.moveCollDown = 0
        self.atackCollDown = 0
        self.defCollDown = 0
        self.distancia = 0
        self.direccion = ['left', 'right', 'up', 'down']
        self.dir = 'left'


        self.debug = py.Surface(
            (self.rect.width, self.rect.height), py.SRCALPHA)   # per-pixel alpha

        #self.left_states = { indice: (X, Y, WIDHT, HEIGHT) }
        self.moves = {
            'left': {
                'move': {0: (18, 588, 46, 47), 1: (82, 589, 28, 46), 2: (146, 588, 28, 46), 3: (210, 588, 28, 47), 4: (274, 588, 29, 50), 5: (338, 589, 30, 49), 6: (402, 588, 29, 50), 7: (466, 588, 29, 50), 8: (530, 588, 29, 50)},
                'stand': {0: (18, 588, 46, 47)},
                'atack_sword': {0: (18, 847, 46, 47), 1: (82, 847, 28, 46), 2: (146, 847, 28, 46), 3: (210, 847, 28, 47), 4: (274, 847, 29, 50), 5: (338, 847, 30, 49)},
            },
            'right': {
                'move': {0: (17, 716, 29, 50), 1: (81, 717, 29, 43), 2: (145, 716, 29, 49), 3: (209, 716, 29, 49), 4: (273, 716, 29, 50), 5: (338, 717, 28, 49), 6: (401, 716, 29, 50), 7: (465, 716, 29, 50), 8: (530, 716, 28, 50)},
                'stand': {0: (17, 716, 29, 50)},
                'atack_sword': {0: (17, 975, 30, 46), 1: (81, 975, 29, 43), 2: (145, 975, 29, 49), 3: (209, 975, 29, 49), 4: (273, 975, 29, 50), 5: (338, 975, 28, 49)},
            },
            'up': {
                'move': {0: (17, 524, 30, 47), 1: (81, 524, 30, 47), 2: (145, 524, 30, 48), 3: (209, 525, 30, 49), 4: (273, 524, 29, 48), 5: (337, 524, 29, 47), 6: (401, 524, 29, 49), 7: (466, 525, 28, 50), 8: (529, 524, 29, 48)},
                'stand': {0: (17, 524, 30, 47)},
                'atack_sword': {0: (17, 785, 30, 47), 1: (81, 785, 30, 47), 2: (145, 785, 30, 48), 3: (209, 785, 30, 49), 4: (273, 785, 29, 48), 5: (337, 785, 29, 47)},
            },
            'down': {
                'move': {0: (17, 651, 30, 51), 1: (81, 651, 30, 51), 2: (145, 651, 30, 52), 3: (209, 652, 30, 49), 4: (273, 651, 30, 52), 5: (337, 651, 30, 51), 6: (401, 651, 30, 52), 7: (465, 652, 30, 51), 8: (529, 651, 30, 52)},
                'stand': {0: (17, 651, 30, 51)},
                'atack_sword': {0: (17, 911, 30, 51), 1: (81, 911, 30, 51), 2: (145, 911, 30, 52), 3: (209, 911, 30, 49), 4: (273, 911, 30, 52), 5: (337, 911, 30, 51)},
            },
        }

    def get_frame(self, frame_set) -> dict:
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect) -> any:
        if type(clipped_rect) is dict:
            self.hoja.set_clip(py.Rect(self.get_frame(clipped_rect)))
        # else:
        #    self.hoja.set_clip(py.Rect(clipped_rect))
        return clipped_rect

    def moveCollDownFun(self, time) -> bool:
        self.moveCollDown += self.tiempo.get_time()
        print(time)
        if self.moveCollDown >= time:
            self.moveCollDown = 0
            return True
        return False


    def updateSprite(self, sprite, direction, accion, distancia=0, velocidad=None) -> None:
        self.clip(self.moves[direction][accion])
        y = 0
        x = 0

        # if self.velocidad > 0:
        #distancia = distancia * -1

        if accion == 'move':
            if direction == 'up':
                #self.rect.y -= distancia
                y -= distancia
            elif direction == 'left':
                #self.rect.x -= distancia
                x -= distancia
            elif direction == 'right':
                #self.rect.x += distancia
                x += distancia
            elif direction == 'down':
                #self.rect.y += distancia
                y += distancia

        #self.moveCollDownFun(velocidad)

        if self.checkColition(sprite, x, y) == False and velocidad != None and self.moveCollDownFun(velocidad):
            print(velocidad)
            self.update(x, y)

        self.image = self.hoja.subsurface(self.hoja.get_clip())

    def handle_event(self) -> None:
        self.move = random.randint(0, 100)
        self.setDireccion()

        if self.move <= 50:
            while self.distancia < 5:
                self.update(self.dir)
                self.distancia += 1
            self.distancia = 0

    def setDireccion(self) -> None:
        self.dir = random.choice(self.direccion)

    # chequear colicion

    def checkColition(self, sprite, x, y) -> bool:
        colicion = False

        next = py.sprite.Sprite()
        next.rect = py.Rect(self.rect.x+x, self.rect.y+y,
                            self.rect.width, self.rect.height)

        self.hits = py.sprite.spritecollide(next, sprite, False, collided=None)
        for h in self.hits:
            if isinstance(h, (Muro)):
                colicion = True
                break
        return colicion


class Barra:
    def __init__(self, pantalla, x, y, width, height, color) -> None:
        self.pantalla = pantalla
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.largoActual = self.width
        self.update(self.largoActual, self.largoActual)

    def update(self, data, max) -> None:
        self.setLargoActual(data, max)
        self.drawBarra()

    def setLargoActual(self, data, max) -> None:
        percent = int((data * 100)/max)
        self.largoActual = int((self.width * percent) / 100)

    def drawBarra(self) -> None:
        self.barraBack = py.Rect(self.x, self.y, self.width, self.height)
        py.draw.rect(self.pantalla, colorBlack, self.barraBack)
        self.barra = py.Rect(self.x, self.y, self.largoActual, self.height)
        py.draw.rect(self.pantalla, self.color, self.barra)


class BarraStats:
    def __init__(self, **kwargs) -> None:
        # surface, x, y, width, height, color.
        self.kwargs = kwargs
        self.surface = kwargs['surface']
        self.barra = Barra(
            self.surface, kwargs['x'], kwargs['y'], kwargs['width'], kwargs['height'], kwargs['color'])
        self.stat = kwargs['stat']

    def update(self, actual, max) -> None:
        txt = f'{self.stat}: {actual} / {max}'
        textFont = fuenteStats.render(txt, True, colorBlack)
        #textX = self.surface.get_size()[0] / 2 - fuenteStats.size(txt)[0] / 2
        textX = self.kwargs['x']
        textY = self.surface.get_size()[1] * \
            0.25 - fuenteStats.size(txt)[1] / 2
        self.surface.blit(textFont, (textX, textY))
        self.barra.update(actual, max)


class Inventario:
    def __init__(self) -> None:
        pass


class BarraInferriro():
    def __init__(self, surface) -> None:
        self.createSurfaces(surface)
        self.createBarsStats()

    # Creacion surface principal

    def createSurfaces(self, surface) -> None:
        self.ventana = surface
        _widht = 800
        _height = 80
        _x = pantallaAncho/2 - _widht/2
        _y = pantallaAlto - _height - 2
        self.surface = Panel(surface, _x, _y, _widht,
                             _height, colorBlackMiddleDarkPluss)

    # Creacion barras de HP y ENE
    def createBarsStats(self) -> None:
        self.contEXP = Panel(self.ventana, self.surface.x+10,
                             self.surface.y+4, 210, 22, colorBlackMiddle)
        self.contHP = Panel(self.ventana, self.surface.x+10,
                            self.surface.y+29, 210, 22, colorBlackMiddle)
        self.contENE = Panel(self.ventana, self.surface.x+10,
                             self.surface.y+54, 210, 22, colorBlackMiddle)

        self.surface.addChild(self.contEXP)
        self.surface.addChild(self.contHP)
        self.surface.addChild(self.contENE)

        self.barraEXP = BarraStats(
            surface=self.contEXP, x=5, y=12, width=200, height=7, color=colorEXPBar, stat='EXP')
        self.barraHp = BarraStats(
            surface=self.contHP, x=5, y=12, width=200, height=7, color=colorHPBar, stat='HP')
        self.barraEne = BarraStats(
            surface=self.contENE, x=5, y=12, width=200, height=7, color=colorENEBar, stat='ENE')

    # Actualizacion de la clase
    def update(self, EXPactual, EXPmax, HPactual, HPmax, ENEactual, ENEmax) -> None:
        self.updateHPandENE(EXPactual, EXPmax, HPactual, HPmax, ENEactual,ENEmax)

    # Actualizacion de todos los componetes
    def updateHPandENE(self, EXPactual, EXPmax, HPactual, HPmax, ENEactual, ENEmax) -> None:
        self.surface.update()
        self.barraEXP.update(EXPactual, EXPmax)
        self.barraHp.update(HPactual, HPmax)
        self.barraEne.update(ENEactual, ENEmax)
