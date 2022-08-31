__name__ = "modulo2"
from main import *

class Proyecto:

    def __init__(self, num, tit, actualizacion, lenguaje,lineas):
        self.numero = num
        self.titulo = tit
        self.actualizacion = actualizacion
        self.lenguaje = lenguaje
        self.lineas = lineas

def cargar_proyecto():
    num = int(input("Indicar numero de proyecto: "))
    tit = str(input("Indicar Titulo de proyecto: "))
    dd_actu = str(input("Ingrese el dia de actualizacion (Formato dd): "))
    mm_actu = str(input("Ingrese el mes de actualizacion (Formato mm): ")) 
    yy_actu = str(input("Ingrese el año de actualizacion (Formato yyyy): "))
    fecha_actu = str(f"{dd_actu}-{mm_actu}-{yy_actu}")
    lenguaje = int(input("0:  Python  -   1:  Java\n2:  C++    -   3:  Javascript\n4:  Shell   -   5:  HTML\n6:  Ruby    -   7:  Swift\n8:  C#      -   9:  VB\n10: Go\nIngrese el lenguaje utilizado: "))
    lineas = int(input("Ingrese la cantidad de lineas de codigo: "))
    nuevo_proyecto = Proyecto(num, tit, fecha_actu, lenguaje, lineas)
    print("¡PROYECTO CARGADO!\n")
    return nuevo_proyecto

def menu():
    print("""
╔═════════════════════════╗
║  G018 SOFTWARE COMPANY  ║
╠═════════════════════════╣
║1- Cargar Proyectos      ║
║2- Listar Proyectos      ║
║3- Actualizar Proyecto   ║
║4- Resumen de Lenguajes  ║
║5- Resumen por Año       ║
║6- Filtrar Lenguaje      ║
║7- Productividad         ║
║0- Salir                 ║
╚═════════════════════════╝""")

def selec_op():
    op = int(input("Seleccione una opcion: "))
    while 7 > op < 0:
        op = int(input("Seleccione una opcion valida: "))
    return op

def ordenamiento_ss(proyectos):
    long= len(proyectos)

    for i in range(long-1):
        for j in range(i+1, long):
            if proyectos[i].numero > proyectos[j].numero:
                # Intercambiar
                proyectos[i].numero, proyectos[j].numero = proyectos[j].numero, proyectos[i].numero