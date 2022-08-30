__name__ = "modulo2"
from main import *

class Proyecto:

    def __init__(self, num, tit, actualizacion, lenguaje):
        self.numero = num
        self.titulo = tit
        self.actualizacion = actualizacion
        self.lenguaje = lenguaje

def cargar_proyecto():
    num = int(input("Indicar numero de proyecto: "))
    tit = str(input("Indicar Titulo de proyecto: "))
    dd_actu = str(input("Ingrese el dia de actualizacion (Formato dd): "))
    mm_actu = str(input("Ingrse el mes de actualizacion (Formato mm): ")) 
    yy_actu = str(input("Ingrese el año de actualizacion (Formato yyyy): "))
    fecha_actu = str(f"{dd_actu}-{mm_actu}-{yy_actu}")
    lenguaje = int(input("Ingrese el lenguaje utilizado: \n0:  Python  -   1:  Java\n2:  C++    -   3:  Javascript\n4:  Shell   -   5:  HTML\n6:  Ruby    -   7:  Swift\n8:  C#      -   9:  VB\n10: Go "))
    nuevo_proyecto = Proyecto(num, tit, fecha_actu, lenguaje)
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

