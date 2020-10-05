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
        self.items.insert(0,item)

    def avanzar(self):
        #Extrae (hace avanzar) la cola. Es decir SACA al primer elemento de la fila.-
        return self.items.pop()

    def tamano(self):
        #Metodo que nos devuelve el tamaño que tenga la Cola (es decir, la cantidad de elementos)
        return len(self.items)
    
    def mostrar(self):
        #Metodo para dar formato al texto que sale en pantalla.-
        return '{}'.format(self.items)

cola = Cola()
print(cola.estaVacia())
cola.agregar('Maca')
cola.agregar('Seba')
print(cola.mostrar())
print(cola.tamano())
cola.avanzar()
cola.agregar('Sergio')
print(cola.mostrar())
cola.avanzar()
print(cola.mostrar())
cola.agregar('Ema')
print(cola.mostrar())
#Vamos a subir a GIT.-