from core.config import nombreDB,dirTablas,dirDatos,dirUserTabla,dirSave
from os.path import basename,splitext
from os import listdir
from io import open
import sqlite3
from .read import  nombreSinExtencion

class Conexion():
    def __init__(self,db=nombreDB):
        self._conn=sqlite3.connect(f'core/db/{db}')
        self._cursor=self._conn.cursor()

    def close(self): 
        self._conn.close()

    def instalacionDB(self) -> None:
        self.crear_tablas(dirTablas)
        self.insetar_datos()
        self.close()

    def crear_tablas(self,tablas) -> None:
        self.__tablas=listdir(tablas)
        i=0
        for inx in self.__tablas:
            sql=open(tablas+inx).read()
            try:
                self._cursor.execute(str(sql))
                self.__tablas[i]=nombreSinExtencion(inx)
                print(f"Se creo la tabla {self.__tablas[i].upper() } exitosamente")
            except Exception as e:
                print(e)
                print(f"Error, no se creo la Tabla: {self.__tablas[i].upper()}")
            finally:
                pass
            i+=1
    
    def insetar_datos(self) -> None:
        datos=listdir(dirDatos)
        i=0
        escribir=False
        for inx in datos:
            sql=open(dirDatos+inx).read()
            datos[i]=splitext(basename(inx))[0]
            if datos[i] in self.__tablas :
                print('')
                print(f"_________Creando datos de la tabla: {datos[i].upper()}__________")
                char=''
                for e in sql:
                    if(e=='('):
                        escribir=True
                    if(e==';'):
                        escribir=False
                        try:
                            #self._cursor.execute(f"INSERT INTO " + datos[i].upper() + " VALUES " + char)
                            self._cursor.execute(f"INSERT INTO {datos[i].upper()} VALUES {char}")
                            self._conn.commit()
                            print(f'Se agrego: {char}')
                        except Exception as e:
                            print(e)
                            print(f"Error en el registro: {char}")
                        char=''
                    if(escribir):
                        char+=e
            i+=1

    def getAll(self,tabla) -> list:
        self._cursor.execute(f"SELECT * FROM {tabla}")
        datos=self._cursor.fetchall()
        self.close()
        return self.setiarAll(datos,self._cursor.description)

    def getDatos(self,tabla,col,valor,condicion='='):
        sql=f"SELECT * FROM {tabla} WHERE {col} {condicion} '{valor}'"
        #print(sql)
        self._cursor.execute(sql)
        datos=self._cursor.fetchall()
        self.close()
        return self.setiarFila(datos,self._cursor.description)

    def getDatosById(self,tabla,valor,condicion='=') -> list:
        sql=f"SELECT * FROM {tabla} WHERE ID {condicion} {valor}"
        try:
            self._cursor.execute(sql)
        except Exception as e:
            print(f"Error:\n-{e}")
        datos=self._cursor.fetchall()
        self.close()
        return self.setiarFila(datos,self._cursor.description)

    def setiarFila(self,datos,cols) -> list:
        fila={}
        i=0
        for c in cols:
            #print(f'{str(c[0])} = {datos[0][i]}')
            fila[str(c[0])] = datos[0][i]
            i+=1
        return fila

    def setiarAll(self,datos,cols) -> list:
        array=[]
        fila={}
        i=0
        for d in datos:
            for c in cols:
                #print(f'{str(c[0])} = {d[i]}')
                fila[str(c[0])] = d[i]
                i+=1
            i=0
            array.append(fila)
            fila={}
        return array

class CargarPartida(Conexion):
    def __init__(self,nombre=''):
        self.nombre=nombre
        super().__init__()
        self.partidas=[]
        for save in listdir(dirSave):
            self.partidas.append(nombreSinExtencion(save))
    
    def Crear(self) -> None:
        self._conn=sqlite3.connect(f'{dirSave}{self.nombre}')
        self._cursor=self._conn.cursor()
        self.crear_tablas(dirUserTabla)
        self._cursor.execute(f"INSERT OR IGNORE INTO PERSONAJE VALUES ('{self.nombre}',1,0,1,0,0,400,212,2,2)")
        self._cursor.execute("INSERT OR IGNORE INTO INVENTARIO VALUES (0,200,0,0)")
        self._conn.commit()
    
    def Cargar(self) -> tuple:
        self._conn=sqlite3.connect(f'{dirSave}{self.nombre}')
        self._cursor=self._conn.cursor()
        p=self.getAll('PERSONAJE')
        self._conn=sqlite3.connect(f'{dirSave}{self.nombre}')
        self._cursor=self._conn.cursor()
        i=self.getAll('INVENTARIO')
        self.close()
        return (p,i)

    def update(self,tabla,columna,id,valor) -> None:
        self._conn=sqlite3.connect(f'{dirSave}{self.nombre}')
        self._cursor=self._conn.cursor()
        self._cursor.execute(f"UPDATE {tabla} SET {columna} = {valor} WHERE {id} = {valor}")
        self._conn.commit()
