import pygame as py
py.font.init()

#CARACTERISTICAS DEL JUEGO
exp = 1
drop = 1
expMax = 5
#NOMBRE DDBB
nombreDB = "JuegoDB"
#LVL MAXIMO
LVLMAX = 80
#MODIFICADOR
MOD = 1.5

#DIMENSION PANTALLA
pantallaAncho = 1200
pantallaAlto = 610

#VENTANA PRINCIPAL DEL JUEGO
ventana = py.display.set_mode((pantallaAncho,pantallaAlto))

#DIRECTORIO DE LAS TABLAS
dirTablas = "./core/db/tablas/"
#DIRECTORIO DE LOS DATOS
dirDatos = "./core/db/datos/"
#DIRECTORIO DE LAS TABLAS CUSTOM
dirTablasCustom = "./core/db/tablas/custom/"
#DIRECTORIO DE LOS DATOS CUSTOM
dirDatosCustom = "./core/db/datos/custom/"
#DIRECTORIO DE LOS MAPAS
dirMapas = "./core/components/maps/"
#DIRECTORIO DE TABLA NUEVO USUARIO
dirUserTabla = "./core/db/tablaUser/"
#DIRECTORIO DE PARTIDAS GUARDADAS
dirSave = "./save/"

#SPRITES
#DIRECTORIO DE LAS ARMADURAS
dirArmaduras = "./img/armaduras/"
#DIRECTORIO DE LAS ARMAS
dirArmas = "./img/armas/"
#DIRECTORIO DE LOS ICONOS
dirIconos = "./img/iconos/"
#DIRECTORIO DE TERRENO
dirTerreno = "./img/terreno/"


#Colors
#1F2687
colorBG = py.Color(31,35,135)
#3559EB
colorComponent = py.Color(53,89,235)
#2676D4
colorComponentChild = py.Color(38,118,212)
#3126D4
colorButton = py.Color(49,38,212)
#2CBFF6
colorComponentClick = py.Color(44,191,246)
#702CF6
colorComponentOver = py.Color(112,44,246)
#colorHPBar #DB381F
colorHPBar = py.Color(219,56,31)
#colorENEBar #4189F5
colorENEBar = py.Color(65,137,245)
#colorEXPBar #DBC135
colorEXPBar = py.Color(219,193,53)
#colorBlack #000000
colorBlack = py.Color(0,0,0)
#colorBlack #6E6F6A
colorBlackMiddleDarkPluss = py.Color(110,111,106)
#colorBlackMiddleDark #948F85
colorBlackMiddleDark = py.Color(148,143,133)
#colorBlackMiddle #7D7D7D
colorBlackMiddle = py.Color(125,125,125)
#colorBlackMiddleLight #878594
colorBlackMiddleLight = py.Color(135,133,145)
#colorBlack #FFFFFF
colorWhite = py.Color(255,255,255)


#FUENTES 
#Titulo juego
fuenteTituloJuego = py.font.SysFont('Cascadia Code', 75)
#CONSOLA
fuenteConsol = py.font.SysFont('Cascadia Code', 25)
#BOTONES
fuenteButtons = py.font.SysFont('Bahnschrift SemiBold', 30)
#STATS
fuenteStats = py.font.SysFont('Bahnschrift SemiBold', 15)