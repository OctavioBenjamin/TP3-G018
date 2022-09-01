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
                ordenamiento_ss_alf(proyectos)
                for i in range(len(proyectos)):
                    print(f"Proyecto {proyectos[i].nombre} Numero: {proyectos[i].numero}")
                
            opcion = -1
        
        elif opcion == 3:
            seguir = 1
            while seguir == 1:
                num_filtro = int(input("Ingrese el numero de proyecto para actualizar: "))
                ordenamiento_ss_num(proyectos)
                
                if binary_search(proyectos, num_filtro) == -1:
                    print(f"¡Error! No se ha encontrado ningun proyecto con el numero {filtro}")
                else:
                    nuevas_lineas = int(input("Cantidad de lineas a actualizar: "))
                    proyectos[binary_search(proyectos, num_filtro)].lineas = nuevas_lineas
                    nuevo_dd = int(input("Ingrese dia de actulización:  "))
                    nuevo_mm = int(input("Ingrese mes de actualizacion: "))
                    nuevo_yy = int(input("Ingrese año de actualización: "))
                    proyectos[binary_search(proyectos, num_filtro)].actualizacion = str(f"{nuevo_dd}-{nuevo_mm}-{nuevo_yy}")
                
                seguir = int(input("Si desea seguir actualizando seleccione 1.\nSi desea volver al menu seleccione 0.\n "))
                while 1 < seguir < 0:
                    print("¡Error! Debe de seleccionar una opcion valida.")
                    seguir = int(input("Si desea seguir actualizando seleccione 1.\nSi desea volver al menu seleccione 0.\n "))

        elif opcion == 4:
            # Cantidad de lineas por lenguaje
            len_filtro = int(input("Ingrese el lenguaje que desea buscar: "))
            cant_lineas = 0
            resultados = []
            for i in range(len(proyectos)):
                if proyectos[i].lenguaje ==  len_filtro:
                    cant_lineas += proyectos[i].lineas
                    resultados.append(proyectos[i])
            
            if len(resultados) > 0:
                print(f"Se encontraron {len(resultados)} proyectos en {lenguajes[len_filtro]}")
                for i in range(len(resultados)):
                    ordenamiento_ss_num(resultados)
                    print(f"{resultados[i].nombre}: Proyecto numero {resultados[i].numero} con {resultados[i].lineas} lineas codigo")    
            
            else:
                print("¡ERROR! No se encontraron resultados")

        elif opcion == 5:
            if len(proyectos) == 0:
                print("¡ERROR! No se han encontrado proyectos cargados")
            else:
                años_conteo = 22*[0]
                # Calcular la cantida de proyectos por año de actualizacion
                # Mostrar los años que solo tengan algun proyecto
                año_pivot = None
                
                for i in range(22):
                    año_pivot = str(proyectos[i].año)
                    año_indice = int(año_pivot[-2]+año_pivot[-1])
                    años_conteo[año_indice] += 1
                
                for i in range(22):
                    if años_conteo[i] > 0:
                        print(f"Se encontraron {años_conteo[i]} proyecto/s en {años[i]}")
                    
        elif opcion == 6:
            #Filtrar por lenguajes ordenados alfabeticamente
            if len(proyectos) == 0:
                print("¡ERROR! No se han encontrado proyectos cargados")
            else:
                len_filtro = int(input("Ingrese el lenguaje que desea buscar: "))
                proyectos_busqueda = []

                for i in range(len(proyectos)):
                    if proyectos[i].lenguaje == len_filtro:
                        proyectos_busqueda.append(proyectos[i])
            
            if len(proyectos_busqueda) == 0:
                print(f"No se han encontrado proyectos con {lenguajes[len_filtro]}")
            else:
                ordenamiento_ss_alf(proyectos_busqueda)
                print(f"Se encontraron {len(proyectos_busqueda)} proyectos.")
                for i in range(len(proyectos_busqueda)):
                    print(f"Proyecto {proyectos_busqueda[i].titulo} Numero {proyectos_busqueda[i].numero}")


                
            


            

if __name__ == "__main__":
    main()

