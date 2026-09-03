#FUNCION ESCRIBIR EN ARCHIVO
def escribir_archivo(nombre_archivo,texto):
    archivo = open(nombre_archivo,"a",encoding="utf-8")
    archivo.write(texto)
    archivo.close()

#FUNCION LEER EN ARCHIVO
def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo,"r",encoding="utf-8") #Abre el archivo en modo lectura
    contenido=archivo.readlines() #Lee todo el contenido y lo almacena como lista
    # print(contenido)
    archivo.close() #Cierre del archivo
    return contenido #Devuelve la lista contenido al llamar a la función