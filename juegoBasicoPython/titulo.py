#Es un juego automatico por turnos, hay dos bandos (el del usuario y el enemigo), hay cinco enemigos con el que el usuario lucha
#atacan una vez por bando, los enemigos atacan uno por vez en orden de id, el usuario siempre ataca al que tiene mas vida, y el juego acaba
#uno de los equipos se queden sin personajes, se debe mostrar en consola el estado de los personajes luego de cada ataque cada personaje tiene
#  tres atributos: vida,ataque y defensa
#  atributos del usuario: vida (entre 1000 y 2000), ataque(entre 100 y 200), defensa (entre 50 y 75) 
#  atributos de enemigos: vida (entre 500 y 1000), ataque(entre 0 y 100), defensa (entre 0 y 50)
#al finalizar la partida se devuelve el estado de los personajes en orden

#pasos que tengo que hacer:
#1. crear las clases personajes
#2. hacer funciones de asignacion de atributos
#3. hacer funciones que compruben la vida de los enemigos y devuelva al enemigo con mayor vida
from os import pathsep
import random
class Personaje(object):
    def __init__(self,vida,ataque,defensa,id,flag):
        self.id = id;
        self.vida = vida;
        self.ataque = ataque;
        self.defensa = defensa;
        self.flag=flag;
    def __definirVida__(self,limite1,limite2):
        self.vida= random.randint(limite1,limite2)
    def __definirAtaque__(self,limite1,limite2):
        self.ataque= random.randint(limite1,limite2)
    def __definirDefensa__(self,limite1,limite2):
        self.defensa= random.randint(limite1,limite2)
    def __recibeElAtaque__(self,ataqueRecibido):
        ataqueFinal= ataqueRecibido - self.defensa
        if  0 > ataqueFinal:
            ataqueFinal= 0
        else:
            self.vida = self.vida-ataqueFinal
            if 0>= self.vida:
                ataqueFinal= -1 # este -1 nos va a ayudar a saber si el personaje se quedo sin vida o no 
                self.vida=0
        return self

def crearEnemigo(id):
    nuevo= Personaje(0,0,0,id,1)
    nuevo.__definirDefensa__(0,50)
    nuevo.__definirVida__(500,1000)
    nuevo.__definirAtaque__(0,100)
    return nuevo

def listaEnemigos(cantidadEnemigos):
    listaEnemigos = []
    for i in range(0,cantidadEnemigos):
        enemigo= crearEnemigo(i)
        listaEnemigos.append(enemigo)
    return listaEnemigos
def definirUsuario():
    id=-1
    usuario= Personaje(0,0,0,id,1) #el usuario va a ser el unico personaje con id -1 para simplificar su busqueda de ser necesario
    usuario.__definirDefensa__(50,75)
    usuario.__definirAtaque__(100,200)
    usuario.__definirVida__(1000,2000)
    return usuario

def mostrarPersonaje(usuario):
    print("\nID: " + str(usuario.id))
    print("\nVIDA: " + str(usuario.vida))
    print("\nDEFENSA: "+ str(usuario.defensa))
    print("\nATAQUE: "+ str(usuario.ataque))

def mostrarListaEnemigos(listaEnemigos):
    for pers in listaEnemigos:
        print("\n---------------------------")
        mostrarPersonaje(pers)
        print("\n--------------------------")

def posicionQueInsertar(lista, personaje):
    i=0
    flag=0
    
    while i!=len(lista) and flag == 0:
        
        if personaje.vida >lista[i].vida:
            i=i+1
        else: 
            flag=1
    rta=i
    return rta


def ordenarLista(lista):
    listaAux=[]
    pos=0
    for per in lista:
       if len(listaAux)==0:
           listaAux.append(per)
       else:
            pos= posicionQueInsertar(listaAux,per)
            listaAux.insert(pos,per)
    return listaAux

def atacarEnemigo(listaEnemigos, usuario,cant):
    rta= "n"
    
    while rta!="s":
        rta= input("\nIngrese (s) para realizar su ataque: ")
        if rta!="s":
            print("\nRespuesta invalida")
        else:             
         ataque= usuario.ataque
         listaEnemigos[cant]=listaEnemigos[cant].__recibeElAtaque__(ataque)
         print("\nLa vida de su enemigo es de : "+ str(listaEnemigos[cant].vida))


def cantVivos(listaEnemigos):

    i=0
    rta=0
    while len(listaEnemigos)>i:
        if listaEnemigos[i].vida>0:
            rta=rta+1
        i=i+1
    return rta

def atacarUsuario(enemigo,usuario):
     
         ataque= enemigo.ataque
         usuario.__recibeElAtaque__(ataque)
         print("\nLa vida del usuario es: "+ str(usuario.vida))

#def enemigoQueAtaca(listaEnemigos,pos):
def posPrimerEnemigo(listaEnemigos):
    rta=0
    i=0
    while rta!=0 and len(listaEnemigos)>i:
        if listaEnemigos[i].vida>0:
            rta=i
        else:
            i=i+1
    return rta

def juego(usuario,listaEnemigos):
    fin=0
    cantEnemigos= 5
    i=0
    while cantEnemigos>0 and usuario.vida>0:
        #ataque del usuario: 
        print("\nUsuario:")
        mostrarPersonaje(usuario)
        print("\n*******************************")
        mostrarListaEnemigos(listaEnemigos)
        print("\n*******************************")
        atacarEnemigo(listaEnemigos,usuario,1)
        #ordenar lista
        listaEnemigos= ordenarLista(listaEnemigos)
        #cuenta los enemigos que hay
        cantEnemigos= cantVivos(listaEnemigos)
        if cantEnemigos!=0:
            if i>=cantEnemigos:
                i=posPrimerEnemigo(listaEnemigos)
            atacarUsuario(listaEnemigos[i],usuario)
            i=i+1

        else:
            fin= 1

    return fin
            

aux=[]
aux= listaEnemigos(5)
listaAux=[]
aux= ordenarLista(aux)
usuario= definirUsuario()

fin= juego(usuario,aux)

if fin == 1:
    print("\nGano el usuario") 
else:
    print("\nGano el enemigo")


