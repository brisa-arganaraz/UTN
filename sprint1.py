from colorama import *
init()

# --- DATOS INICIALES ---
Nick = input(Fore.BLUE + "Ingrese su Nick de jugador: ")
print(Fore.GREEN + f"Hola {Nick}, te pedire tu mail para enviarte el recibo.")
Mail = input(Fore.BLUE + "Ingrese su Mail: ")

print(Fore.GREEN + "Cada juego cuesta 10000")

Plataforma = input(Fore.BLUE + "Plataforma (Playstation/PC/Mobile): ")
Formato = input("Formato (Fisico/Digital): ")
Genero = input("Genero (Terror/Accion/Aventura): ")
Edad = int(input("Edad: "))
Almacenamiento = int(input("Almacenamiento en GB: "))
Presupuesto = int(input("Presupuesto: "))
Jugadores = int(input("Cantidad de jugadores: "))
Cantidad = int(input("Cantidad de juegos: "))
AceptaTerminos = input("¿Acepta términos? (S/N): ")

# --- VALIDACIONES ---
if AceptaTerminos != "S":
    print(Fore.RED + "No puede continuar.")
    exit()

# Restricciones por edad
if Genero == "Terror" and Edad < 16:
    print(Fore.RED + "Terror es +16")
    Genero = input("Nuevo genero: ")

if Genero == "Accion" and Edad < 13:
    print(Fore.RED + "Accion es +13")
    Genero = input("Nuevo genero: ")

# Validaciones con while
while Almacenamiento < 100:
    Almacenamiento = int(input("Minimo 100GB: "))

while Presupuesto < 2000:
    Presupuesto = int(input("Minimo 2000: "))

# Tipo de presupuesto
if Presupuesto > 8000:
    Tipo = "Alto"
elif Presupuesto > 5000:
    Tipo = "Medio"
else:
    Tipo = "Bajo"

# --- RECOMENDACIONES ---

# PC
if Plataforma == "PC":
    if Genero == "Aventura":
        if Tipo == "Bajo":
            print("Recomendacion: Hollow Knight")
        elif Tipo == "Medio":
            print("Recomendacion: It Takes Two")
        else:
            print("Recomendacion: GTA V")

    elif Genero == "Accion":
        if Tipo == "Bajo":
            print("Recomendacion: Counter Strike 2")
        else:
            print("Recomendacion: Cyberpunk 2077")

    elif Genero == "Terror":
        if Tipo == "Bajo":
            print("Recomendacion: Outlast")
        else:
            print("Recomendacion: Phasmophobia")

# PLAYSTATION
elif Plataforma == "Playstation":
    if Genero == "Terror":
        print("Recomendacion: Resident Evil")
    elif Genero == "Accion":
        print("Recomendacion: God of War")
    elif Genero == "Aventura":
        print("Recomendacion: The Last of Us")

# MOBILE
elif Plataforma == "Mobile":
    if Genero == "Terror":
        print("Recomendacion: Eyes Horror Game")
    elif Genero == "Accion":
        print("Recomendacion: Call of Duty Mobile")
    elif Genero == "Aventura":
        print("Recomendacion: Genshin Impact")

# --- COMPRA ---
Precio = 10000
Total = Precio * Cantidad

if Total <= Presupuesto:
    print(Fore.GREEN + "Te alcanza para la compra")
else:
    print(Fore.RED + "No te alcanza")

# --- FINAL ---
Reseña = input("Desea dejar una reseña? (si/no): ")
print("Gracias por usar el sistema,", Nick)
