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
    
    def intercambiar(self, otraCola):
        colaAuxiliar = Cola()
        for _ in range(self.tamano()): #Pasamos el contenido de la cola 1 -> cola auxiliar
            colaAuxiliar.agregar(self.avanzar())
        for _ in range(otraCola.tamano()): #Pasamos el contenido de la Cola 2 -> a la cola 1
            self.agregar(otraCola.avanzar())
        for _ in range(colaAuxiliar.tamano()): #Pasamos el contenido de la colaAuxiliar -> cola 2
            otraCola.agregar(colaAuxiliar.avanzar())
        return colaAuxiliar

cola1 = Cola ()
cola2 = Cola ()
cola1.agregar(1);cola1.agregar(4);cola1.agregar(8)
cola2.agregar(4);cola2.agregar(2);cola2.agregar(7)
print("Primer Cola: ", cola1.imprimir())
print("Segunda Cola: ", cola2.imprimir())
cola_intercambiada = cola1.intercambiar(cola2)
print("Cola 1 intercambiada: ", cola1.imprimir())
print("Cola 2 intercambiada: ", cola2.imprimir())