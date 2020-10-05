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
        return self.items.pop(0)

    def tamano(self):
        #Metodo que nos devuelve el tamaño que tenga la Cola (es decir, la cantidad de elementos)
        return len(self.items)
    
    def imprimir(self):
        #Metodo para dar formato al texto que sale en pantalla.-
        return '{}'.format(self.items)
    
    def vaciarCola(self):
        while not self.estaVacia():
            self.items.pop()
        return self.items

    def darVuelta(self):
        auxiliar = []
        while not self.estaVacia():
            auxiliar.insert(0,self.avanzar())
        return auxiliar
    
    def trasladar(self, otraCola):
        while not self.estaVacia():
            c2.agregar(self.avanzar())
        return c2

cola = Cola()
c2 = Cola()
cola.agregar("Carlos")
cola.agregar("Maria")
cola.agregar("Pedro")
cola.agregar("Catalina")
print(cola.imprimir())
c2 = cola.trasladar(cola)
cola.vaciarCola()
print("Cola original: ", cola.imprimir())
print("Cola trasladada: ", c2.imprimir())
assert cola.estaVacia() == True