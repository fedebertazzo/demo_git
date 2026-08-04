from clase_seleccion import SeleccionFutbol
from clase_jugador import Jugador

#FUNCION ESCRIBIR EN ARCHIVO
def escribir_archivo(nombre_archivo,texto):
    archivo = open(nombre_archivo,"a",encoding="utf-8")
    archivo.write(texto)
    archivo.close()

#FUNCION LEER EN ARCHIVO
def leer_archivo(nombre_archivo,texto):
    archivo = open(nombre_archivo,"r",encoding="utf-8")
    contenido=archivo.readlines(texto)
    # TAREA:Con la lista de la variable "contenido", armo la lista de convocados de la seleccion
    archivo.close()

lionel_messi = Jugador("Lionel","Messi","Delantero")
rodri_depaul = Jugador("Rodrigo", "De Paul", "Mediocampista")

sel_argentina = SeleccionFutbol("Argentina", "Lionel Scaloni", 3,"H")
#Lea el archivo de convocados y los muestre con el método "mostrar_plantel"

# TAREA #2: Hacer un menú similar al siguiente:
# 1 - Mostrar plantel
# 2 - Convocar jugador
# 3 - Quitar a jugador por lesión

n=0
while n < 4:
    print("Convoque un jugador: ")
    nombre=input("Nombre del jugador: ")
    apellido=input("Apellido del jugador: ")
    pos = input("Posicion: ")

    jugador_nuevo=Jugador(nombre,apellido,pos)
    sel_argentina.convocar(jugador_nuevo)
    escribir_archivo("argentina_convocados.txt",f"{jugador_nuevo.nombre},{jugador_nuevo.apellido},{jugador_nuevo.posicion}\n")
    print("..........")
    n +=1