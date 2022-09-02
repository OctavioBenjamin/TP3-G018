__name__ = "modulo2"
from main import *

class Proyecto:

    def __init__(self, num, tit, año, actualizacion, lenguaje,lineas):
        self.numero = num
        self.titulo = tit
        self.año = año
        self.actualizacion = actualizacion
        self.lenguaje = lenguaje
        self.lineas = lineas

lenguajes = ["Python", "Java", "C++", "Javascript", "Shell", "HTML", "Ruby", "Swift", "C#", "VB", "Go"]
años = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

def cargar_proyecto():
    num = int(input("Indicar numero de proyecto: "))
    tit = str(input("Indicar Titulo de proyecto: "))
    dd_actu = str(input("Ingrese el dia de actualizacion (Formato dd): "))
    mm_actu = str(input("Ingrese el mes de actualizacion (Formato mm): ")) 
    yy_actu = str(input("Ingrese el año de actualizacion (Formato yyyy): "))
    fecha_actu = str(f"{dd_actu}-{mm_actu}-{yy_actu}")
    lenguaje = int(input("0:  Python  -   1:  Java\n2:  C++    -   3:  Javascript\n4:  Shell   -   5:  HTML\n6:  Ruby    -   7:  Swift\n8:  C#      -   9:  VB\n10: Go\nIngrese el lenguaje utilizado: "))
    lineas = int(input("Ingrese la cantidad de lineas de codigo: "))
    nuevo_proyecto = Proyecto(num, tit, yy_actu, fecha_actu, lenguaje, lineas)
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

def ordenamiento_ss_num(proyectos):
    long= len(proyectos)

    for i in range(long-1):
        for j in range(i+1, long):
            if proyectos[i].numero > proyectos[j].numero:
                # Intercambiar
                proyectos[i], proyectos[j] = proyectos[j], proyectos[i]
                
def ordenamiento_ss_alf(proyectos):
    long= len(proyectos)

    for i in range(long-1):
        for j in range(i+1, long):
            if proyectos[i].titulo > proyectos[j].titulo:
                # Intercambiar
                proyectos[i], proyectos[j] = proyectos[j], proyectos[i]

def binary_search(v, x):
	# busqueda binaria... asume arreglo ordenado...
	izq, der = 0, len(v) - 1
	while izq <= der:
		mid = (izq + der) // 2
		if x == v[mid]:
			return mid

		elif x < v[mid]:
			der = mid - 1

		else:
			izq = mid + 1
	return -1

