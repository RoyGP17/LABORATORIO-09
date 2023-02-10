class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaCircular:
    def __init__(self):
        self.cabeza = None

    def agregar_ultimo(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza

    def eliminar_ultimo(self):
        if self.cabeza is None:
            return "La lista está vacía"
        elif self.cabeza.siguiente == self.cabeza:
            temp = self.cabeza
            self.cabeza = None
            return str(temp.dato) + " se ha eliminado de la lista"
        else:
            temp = self.cabeza
            while temp.siguiente.siguiente != self.cabeza:
                temp = temp.siguiente
            temp2 = temp.siguiente
            temp.siguiente = self.cabeza
            return str(temp2.dato) + " se ha eliminado de la lista"

    def agregar_primero(self, dato):
        nuevo_nodo = Nodo(dato)
        temp = self.cabeza
        nuevo_nodo.siguiente = self.cabeza
        if self.cabeza is not None:
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo
        else:
            nuevo_nodo.siguiente = nuevo_nodo
        self.cabeza = nuevo_nodo

    def eliminar_primero(self):
        if self.cabeza is None:
            return "La lista está vacía"
        elif self.cabeza.siguiente == self.cabeza:
            temp = self.cabeza
            self.cabeza = None
            return str(temp.dato) + " se ha eliminado de la lista"
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp2 = self.cabeza
            self.cabeza = self.cabeza.siguiente
            temp.siguiente = self.cabeza
            return str(temp2.dato) + " se ha eliminado de la lista"

    def mostrar_lista(self):
        if self.cabeza is None:
            return "La lista está vacía"
        else:
            temp = self.cabeza
            lista = []
            while temp.siguiente != self.cabeza:
                lista.append(temp.dato)
                temp = temp.siguiente
            lista.append(temp.dato)
            return lista


def menu():
    lista = ListaEnlazadaCircular()
    opcion = 0
    while opcion != 7:
        print("\n1. Agregar al final")
        print("2. Eliminar al final")
        print("3. Agregar al inicio")
        print("4. Eliminar al inicio")
        print("5. Mostrar lista")
        print("6. Lista Vacía")
        print("7. Salir\n")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            dato = int(input("Ingrese un número a agregar al final: "))
            lista.agregar_ultimo(dato)
        elif opcion == 2:
            print(lista.eliminar_ultimo())
        elif opcion == 3:
            dato = int(input("Ingrese un número a agregar al inicio: "))
            lista.agregar_primero(dato)
        elif opcion == 4:
            print(lista.eliminar_primero())
        elif opcion == 5:
            print(lista.mostrar_lista())
        elif opcion == 6:
            if lista.cabeza is None:
                print("La lista está vacía")
            else:
                print("La lista no está vacía")

menu()