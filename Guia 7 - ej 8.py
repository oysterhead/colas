import random

class Cola:
    '''Tipo de dato abstracto donde se representa un manejo tipo FiFO (primero en llegar, primero en salir).
    Se implementarán distintos métodos para manejar este TAD a través de listas'''
    def __init__(self):
        #Constructor de la clase Cola
        self.items = []

    def estaVacia(self):
        #Metodo que permite saber si la Cola está vacía o no
        return self.items == []

    def agregar(self, item):
        #Metodo para agregar items a la Cola. Se agregan siempre al final de la cola como se hace en,
        #por ejemplo, una fila (cola) del banco, o del super.-
        self.items.append(item)

    def avanzar(self):
        #Extrae (hace avanzar) la cola. Es decir SACA al primer elemento de la fila.
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
    
    def primero(self):
        return self.items[0]

    def tamano(self):
        #Metodo que nos devuelve el tamaño que tenga la Cola (es decir, la cantidad de elementos)
        return len(self.items)
    
    def imprimir(self):
        #Metodo para dar formato al texto que sale en pantalla.-
        return '{}'.format(self.items)
    
    def jugar(self, nrogente):
        parti = [] #Lista donde vamos a cargar los participantes.-
        while nrogente > 0: #Carga el arreglo con la cantidad de participantes
            parti.append(nrogente)
            nrogente = nrogente - 1

        for i in parti: #Igualo la cantidad de sillas y jugadores
            self.agregar(i)

        while self.tamano() > 1: #Mientras tenga al menos 1 silla, se puede jugar.-
            silla = self.avanzar() #saco una silla
            for i in range(random.randint(1,10)):
                self.agregar(silla)
                self.avanzar()
            self.avanzar()
        return parti


participantes = int(input("Ingrese la cantidad de Personas que van a jugar -> "))
cola = Cola()
juego = cola.jugar(participantes)
print("El ganador del juego es el participante Nro ->" , juego)