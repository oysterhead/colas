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

    def concat(self, otracola):
        colaAuxiliar = Cola()
        for _ in range(self.tamano()):
            colaAuxiliar.agregar(self.primero())
            self.agregar(self.primero())
            self.avanzar()
        for _ in range(c2.tamano()):
            colaAuxiliar.agregar(c2.primero())
            c2.agregar(c2.primero())
            c2.avanzar()
        return colaAuxiliar

c1 = Cola()
c2 = Cola()
c1.agregar(1);c1.agregar(4);c1.agregar(8)
c2.agregar(4);c2.agregar(2);c2.agregar(7)
print("Primer Cola: ", c1.imprimir())
print("Segunda Cola: ", c2.imprimir())
concatenada = c1.concat(c2)
print ("Cola Concatenada: ", concatenada.imprimir())
print("Luego del Encolamiento - Primer Cola: ", c1.imprimir())
print("Luego del Encolamiento - Segunda Cola: ", c2.imprimir())