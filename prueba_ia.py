import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk

class Selección:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.jugadores = []

class Juego:
    def __init__(self):
        self.selecciones = []

    def agregar_seleccion(self, seleccion):
        self.selecciones.append(Seleccion(leccionar_nombre(), leccionar_cantidad()))

    def mostrar_selecciones(self):
        for i, seleccion in enumerate(self.selecciones):
            ctk.Frame(self, corner_radius=10, bg_color="blue", fg_color="white", width=400, height=100).pack(side=ctk.TOP, padx=10, pady=10)
            ctk.Label(self, text=seleccion.nombre, font=("Arial", 12), fg="white", bg_color="blue", corner_radius=5).pack(pady=10)
            ctk.Label(self, text=f"Cantidad: {seleccion.cantidad}", font=("Arial", 12), fg="white", bg_color="blue", 
corner_radius=5).pack(pady=10)

    def mostrar_jugadores(self):
        for i, seleccion in enumerate(self.selecciones):
            ctk.Label(self, text=f"Selección {i+1}: {seleccion.nombre}", font=("Arial", 12), fg="black", bg_color="white", 
corner_radius=10).pack(pady=10)
            ctk.Label(self, text="Jugadores:", font=("Arial", 12), fg="black", bg_color="white", corner_radius=10).pack(pady=10)
            ctk.Frame(self, corner_radius=10, bg_color="white", fg_color="black", width=300, height=100).pack(side=ctk.TOP, padx=10, pady=10)
            ctk.Label(self, text="Nombre", font=("Arial", 12), fg="black", bg_color="white", corner_radius=5).pack(side=ctk.LEFT, padx=10)
            ctk.Entry(self, font=("Arial", 12), width=30).pack(side=ctk.LEFT, padx=10)
            ctk.Label(self, text="Posición", font=("Arial", 12), fg="black", bg_color="white", corner_radius=5).pack(side=ctk.LEFT, padx=10)
            ctk.Entry(self, font=("Arial", 12), width=30).pack(side=ctk.LEFT, padx=10)
            ctk.Button(self, text="Agregar", command=lambda seleccion=seleccion: agregar_jugador(seleccion)).pack(side=ctk.LEFT, padx=10)

    def agregar_jugador(self, seleccion):
        nombre = leccionar_nombre()
        posicion = leccionar_posicion()
        seleccion.jugadores.append((nombre, posicion))

    def mostrar_jugadores_seleccion(self, seleccion):
        ctk.Label(self, text=f"Selección {seleccion.nombre}", font=("Arial", 12), fg="black", bg_color="white", corner_radius=10).pack(pady=10)
        ctk.Label(self, text="Jugadores:", font=("Arial", 12), fg="black", bg_color="white", corner_radius=10).pack(pady=10)
        ctk.Frame(self, corner_radius=10, bg_color="white", fg_color="black", width=300, height=100).pack(side=ctk.TOP, padx=10, pady=10)
        for i, (nombre, posicion) in enumerate(seleccion.jugadores):
            ctk.Label(self, text=f"{i+1}. {nombre} - {posicion}", font=("Arial", 12), fg="black", bg_color="white", 
corner_radius=5).pack(pady=10)

def leccionar_nombre():
    return ctk.Entry(ctk.Tk(), font=("Arial", 12), width=30).get()

def leccionar_posicion():
    return ctk.Entry(ctk.Tk(), font=("Arial", 12), width=30).get()

def agregar_jugador(seleccion):
    nombre = leccionar_nombre()
    posicion = leccionar_posicion()
    seleccion.jugadores.append((nombre, posicion))

def main():
    root = ctk.CTk()
    root.title("Selecciones de Fútbol")

    juego = Juego()

    agregar_seleccion = ctk.CTkButton(root, text="Agregar Selección", command=lambda: juego.agregar_seleccion(juego))
    agregar_seleccion.pack(pady=10)

    mostrar_selecciones = ctk.CTkButton(root, text="Mostrar Selecciones", command=lambda: juego.mostrar_selecciones())
    mostrar_selecciones.pack(pady=10)

    mostrar_jugadores_seleccion = ctk.CTkButton(root, text="Mostrar Jugadores Seleccion", command=lambda: 
juego.mostrar_jugadores_seleccion(juego))
    mostrar_jugadores_seleccion.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
# """

# Este código crea una ventana con tres botones: "Agregar Selección", "Mostrar Selecciones" y "Mostrar Jugadores Seleccion". Cuando se hace clic 
# en el botón "Agregar Selección", se crea una nueva selección y se muestra en la ventana. Al hacer clic en el botón "Mostrar Selecciones", se 
# muestran todas las selecciones creadas y se muestra el número de jugadores en cada selección. Al hacer clic en el botón "Mostrar Jugadores 
# Seleccion", se muestra el nombre y la posición de cada jugador en la selección seleccionada."""