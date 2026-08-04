from clase_seleccion import SeleccionFutbol
from clase_jugador import Jugador

#FUNCION ESCRIBIR EN ARCHIVO
def escribir_archivo(nombre_archivo,texto):
    archivo = open(nombre_archivo,"a",encoding="utf-8")
    archivo.write(texto)
    archivo.close()

#FUNCION LEER EN ARCHIVO
# TAREA:Con la lista de la variable "contenido", armo la lista de convocados de la seleccion
def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo,"r",encoding="utf-8") #Abre el archivo en modo lectura
    contenido=archivo.readlines() #Lee todo el contenido y lo almacena como lista
    # print(contenido)
    archivo.close() #Cierre del archivo
    return contenido #Devuelve la lista contenido al llamar a la función


sel_argentina = SeleccionFutbol("Argentina", "Lionel Scaloni", 3,"H")
lista_convocados=leer_archivo("argentina_convocados.txt")
for linea in lista_convocados: #Recorro cada linea del contenido del texto como línea
    info_jugador=linea.split(",") #Separo la linea con los divisores de coma
    jugador_convocado=Jugador(info_jugador[0],info_jugador[1],info_jugador[2].strip()) #Se crea el objeto jugador con los elementos obtenidos
    sel_argentina.convocados.append(jugador_convocado)
sel_argentina.mostrar_plantel() #Mostrar el plantel convocado al iniciar el script


# TAREA #2: Hacer un menú similar al siguiente:
# 1 - Mostrar plantel
# 2 - Convocar jugador
# 3 - Quitar a jugador por lesión

# n=0
# while n < 4:
#     print("Convoque un jugador: ")
#     nombre=input("Nombre del jugador: ")
#     apellido=input("Apellido del jugador: ")
#     pos = input("Posicion: ")

#     jugador_nuevo=Jugador(nombre,apellido,pos)
#     sel_argentina.convocar(jugador_nuevo)
#     escribir_archivo("argentina_convocados.txt",f"{jugador_nuevo.nombre},{jugador_nuevo.apellido},{jugador_nuevo.posicion}\n")
#     print("..........")
#     n +=1