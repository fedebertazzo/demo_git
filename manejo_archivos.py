def escribir_archivo(nombre_archivo,texto):
    archivo = open(nombre_archivo,"w",encoding="utf-8")
    archivo.write(texto)
    archivo.close()


lionel_messi = Jugador("Lionel","Messi","Delantero")

escribir_archivo("argentina_convocados.txt",f"{lionel_messi.nombre},{lionel_messi.apellido}, {lionel_messi.posición}")