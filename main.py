import random
from modulo2 import *

def main():

    opcion = -1
    listaCreada = False
    while opcion != 0:
        menu()
        opcion = selec_op()

        if opcion == 1:

            if listaCreada:
                n = int(input("Indique la cantidad de proyectos a cargar: "))

                for i in range(n):
                    nuevo_proyecto = cargar_proyecto()
                    proyectos.append(nuevo_proyecto)
            else:
                n = int(input("Indique la cantidad de proyectos a cargar: "))
                
                while n < 0:
                    n = int(input("Indique una cantiad valida: "))

                proyectos = n*[None]; listaCreada = True

                for i in range(n):
                    proyectos[i] = cargar_proyecto()
            opcion = -1

        elif opcion == 2:
            if listaCreada == False:
                print("ERROR: No se han encontrado proyectos cargados")
            else:
                ordenamiento_ss(proyectos)
                for i in range(len(proyectos)):
                    print(f"Proyecto {proyectos[i].nombre} Numero: {proyectos[i].numero}")
                
            opcion = -1

if __name__ == "__main__":
    main()

