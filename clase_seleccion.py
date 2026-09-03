# from clase_jugador import Jugador
from manejo_archivos import escribir_archivo

class SeleccionFutbol:
    """Clase para las selecciones de fútbol"""
    def __init__(self, nacionalidad, dt,grupo):
        self.nacionalidad = nacionalidad
        self.director_tecnico = dt
        # self.titulos = titulos
        self.archivo_convocados=f"{self.nacionalidad.lower()}_convocados.txt"
        self.convocados = []
        self.puntos=0
        self.grupo=grupo
        # self.cargar_convocados()

    def __str__(self):
        return f"Esta es la seleccion de {self.nacionalidad}, dirigida por {self.director_tecnico}"
    
    #Método Convocar
    def convocar(self, jugador):
        "Incorporar un jugador a la plantilla"
        escribir_archivo(self.archivo_convocados,f"{jugador.nombre},{jugador.apellido},{jugador.posicion}\n")
        self.convocados.append(jugador)


    # # #Método cargar convocados desde txt
    # def cargar_convocados(self):
    #     lista_convocados=leer_archivo("argentina_convocados.txt")
    #     for linea in lista_convocados: #Recorro cada linea del contenido del texto como línea
    #         info_jugador=linea.split(",") #Separo la linea con los divisores de coma
    #         jugador_convocado=Jugador(info_jugador[0],info_jugador[1],info_jugador[2].strip()) #Se crea el objeto jugador con los elementos obtenidos
    #         self.convocados.append(jugador_convocado)

    #Método Mostrar convocados
    def mostrar_plantel(self):
        
        print ("Arqueros:")
        for jugador in self.convocados:
            if jugador.posicion == "Arquero":
                print(f"{jugador.nombre} {jugador.apellido}")
        print ("\nDefensores:")
        for jugador in self.convocados:
            if jugador.posicion == "Defensor":
                print(f"{jugador.nombre} {jugador.apellido}")
        print ("\nMediocampistas:")
        for jugador in self.convocados:
            if jugador.posicion == "Mediocampista":
                print(f"{jugador.nombre} {jugador.apellido}")
        print ("\nDelanteros:")
        for jugador in self.convocados:
            if jugador.posicion == "Delantero":
                print(f"{jugador.nombre} {jugador.apellido}")
    
    def retirar_jugador(self):
        #Por seleccion de jugador
        lista_convocados=leer_archivo("argentina_convocados.txt")
        i=1
        for linea in lista_convocados:
            info_jugador=linea.split(",") #Separo la linea con los divisores de coma
            print(f"{i} - {info_jugador[0]},{info_jugador[1]},{info_jugador[2].strip()}")
            i +=1
        opcion_jugador=int(input("Indique el número del jugador a retirar: "))

        confirmar_retiro=input(f"Desea retirar a {lista_convocados[opcion_jugador-1].split(",")}? (Y/N) ").upper()
        if confirmar_retiro == "Y":
            lista_convocados.pop(opcion_jugador-1)
            print("Retirado!")
            with open("argentina_convocados.txt","w", encoding="utf-8") as archivo:
                for linea in lista_convocados:
                    archivo.write(linea)

    # def juega_con(self, equipo_contrario):
    #     #Usar un random de goles
    #     #La seleccion que mete mas goles suma puntos
