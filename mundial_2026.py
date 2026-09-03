from clase_seleccion import SeleccionFutbol
from clase_jugador import Jugador
from manejo_archivos import leer_archivo,escribir_archivo

sel_argentina = SeleccionFutbol("Argentina", "Lionel Scaloni","H")
lista_convocados=leer_archivo("argentina_convocados.txt")
for linea in lista_convocados: #Recorro cada linea del contenido del texto como línea
    info_jugador=linea.split(",") #Separo la linea con los divisores de coma
    jugador_convocado=Jugador(info_jugador[0],info_jugador[1],info_jugador[2].strip()) #Se crea el objeto jugador con los elementos obtenidos
    sel_argentina.convocados.append(jugador_convocado)

selecciones_obj=[]

### TO DO
# Al iniciar el script debe leer las selecciones ya creadas
#Carga de selecciones
selecciones=leer_archivo("selecciones.txt")
for seleccion in selecciones:
    seleccion=seleccion.split(",")
    selecciones_obj.append(SeleccionFutbol(seleccion[0],seleccion[1],seleccion[2].strip()))
# for seleccion in selecciones_obj:
#     print(seleccion)

#Carga de convocados
for seleccion in selecciones_obj:
    jugadores=leer_archivo(seleccion.archivo_convocados)
    for jugador in jugadores:
        info_jugador=jugador.split(",")
        seleccion.convocar(Jugador(info_jugador[0],info_jugador[1],info_jugador[2].strip()))
        



#Bucle principal del menú
salir = False
while salir == False:
    print("""
### Menú de la selección ###
1 - Crear seleccion
2 - Modificar selección
3 - Jugar!!!
4 - Salir
----------------
""")
    opcion_principal=int(input("Seleccione una opción: "))
    if opcion_principal ==1:
        #Crear selección
        nacionalidad=input("Ingrese el pais: ").capitalize()
        for seleccion in selecciones_obj:
            if seleccion.nacionalidad == nacionalidad:
                print(f"La selección {nacionalidad} ya existe")
                break
            else:
                dt=input("Ingrese el DT: ")
                grupo=input("Ingrese el grupo: ").upper()
                nueva_seleccion=SeleccionFutbol(nacionalidad,dt,grupo)
                nueva_seleccion.archivo_convocados=f"{nueva_seleccion.nacionalidad.lower()}_convocados.txt"
                print(f"El archivo de convocados es {nueva_seleccion.archivo_convocados}")
                escribir_archivo("selecciones.txt",f"{nueva_seleccion.nacionalidad},{nueva_seleccion.director_tecnico},{nueva_seleccion.grupo}\n")
                # grupo_equipos.append(nueva_seleccion)
                break
    if opcion_principal == 2:
        #Elegir selección
        selecciones=leer_archivo("selecciones.txt")
        print(selecciones)
        i=1
        for seleccion in selecciones:
            print(f"{i} - {seleccion.split(",")[0].strip()}")
            i+=1
        opcion=(int(input("Elija la selección a modificar: ")))
        print(selecciones[opcion-1])
        seleccion_elegida_str=selecciones[opcion-1]
        for elemento in selecciones_obj:
            
            if seleccion_elegida_str.split(",")[0].capitalize() == elemento.nacionalidad:
                print("Si, existe")
                seleccion_elegida=elemento
                print(seleccion_elegida)
            else:
                # print("Opcion no válida - La selección no existe")
                continue
        

        
        print("""
        ### Menú de la selección ###
        1 - Mostrar plantel
        2 - Convocar jugador
        3 - Quitar a jugador por lesión
        4 - Volver al menú principal
        ----------------
        """)
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            seleccion_elegida.mostrar_plantel()
        elif opcion == 2:
            print("Convoque un jugador: ")
            nombre=input("Nombre del jugador: ")
            apellido=input("Apellido del jugador: ")
            pos = input("Posicion: ")
            jugador_nuevo =Jugador(nombre,apellido,pos)
            seleccion_elegida.convocar(jugador_nuevo)
        elif opcion == 3:
            # sel_argentina.retirar_jugador()
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
            else:
                continue
        elif opcion==4:
            continue
        else:
            print("Opción no válida. Seleccione un número del menú")
            continue
    elif opcion_principal==4:
            salir=True
    # else:
    #     print("Opción no válida. Seleccione un número del menú principal")
    #     continue