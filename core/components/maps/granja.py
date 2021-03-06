#nombre del mapa
nombre = 'Granja'

#esquema del mapa 32x21
mapa = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,0,0],
    [0,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,0],
    [0,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,0],
    [0,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,0],
    [0,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0],
    [0,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0],
    [0,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0],
    [0,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0],
    [5,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0],
    [5,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0],
    [5,6,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0],
    [0,6,6,6,6,6,6,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0],
    [0,6,6,6,6,6,6,6,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0],
    [0,6,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0],
    [0,6,6,6,6,6,6,6,6,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0],
    [0,6,6,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,0],
    [0,6,6,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,0],
    [0,6,6,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,0],
    [0,0,6,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,0,0],
    [0,0,0,0,0,0,0,0,0,7,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]


#todos los personajes que estan en el mapa
characters = [
    {
        'type' : 'enemy',
        'nombre' : 'Un Enemigo',
        'class_id' : 1,
        'position' : (212,265),
        'tile' : {'X':0,'Y':448,'WIDTH':62,'HEIGHT':66},
        'lvl' : 1,
        'sprite' : ''
    },
]
            
#mini mapa del mapa
mundi=[
    [0,0,0,0,0],
    [0,6,6,6,0],
    [5,6,6,6,0],
    [0,6,6,6,0],
    [0,0,6,0,0]
]