from colorama import *
init()

Nick = input(Fore.BLUE + "Ingrese su Nick de jugador: ")
print(Fore.GREEN + "Hola", Nick, "a continuacion te pedire que escribas tu Mail para poder recibir un correo con tu recibo y las especificaciones de tu pedido")
Mail = input(Fore.BLUE + "Ingrese su Mail: ")
print(Fore.GREEN + "Perfecto, ahora te ire pidiendo datos que me permitiran brindarte un juego de tu agrado")
Plataforma = input(Fore.BLUE + "Ingrese la plataforma en la cual juega (Playstation/PC/Mobile): ")
Formato = input("Ingrese el formato de juego que desea (Fisico/Digital): ")
Genero = input("Ingrese el Genero de juego que prefiere (Terror/Accion/Aventura): ")
Edad = int(input("Ingrese su edad: "))
Almacenamiento = int(input("Ingrese su capacidad de almacenamiento en GB: "))
Presupuesto = int(input("Ingrese su presupuesto: "))
Jugadores = int(input("Cantidad de jugadores: "))
Cantidad = int(input("Cantidad de juegos que desea comprar: "))
AceptaTerminos = input("¿Acepta los términos y condiciones? (S/N): ")

if not AceptaTerminos == "S":
    print(Fore.RED + "No puede continuar sin aceptar los términos.")

if Plataforma == "PC":

    if Genero == "Terror" and Edad < 16:
        print(Fore.RED + "Lo sentimos " + Nick + ", los juegos de Terror son para mayores de 16.")
        Genero = input(Fore.BLUE + "Escriba el nuevo genero para continuar: ")

    if Genero == "Accion" and Edad < 13:
        print(Fore.RED + "Lo sentimos " + Nick +", los juegos de Accion son para mayores de 13.")
        Genero = input(Fore.BLUE + "Escriba el nuevo genero para continuar: ")

    if Almacenamiento < 100:
        print(Fore.RED + "Error: Espacio insuficiente.")
        Almacenamiento = int(input(Fore.WHITE + "Reingrese almacenamiento (minimo 100GB): "))

    if Presupuesto < 2000:
        print(Fore.RED + "Error: Presupuesto insuficiente.")
        Presupuesto = int(input(Fore.WHITE + "Reingrese presupuesto (minimo 2000): "))

    if Presupuesto >= 2000:
       Tipo_Presupuesto = "Bajo"

    if Presupuesto >= 5000:
       Tipo_Presupuesto = "Medio"

    if Presupuesto >= 8000:
       Tipo_Presupuesto = "Alto"

    print(Fore.CYAN + "Analizando opciones para " + Nick + "..." )

    if Genero == "Aventura":

        if Jugadores == 1 and Tipo_Presupuesto == "Alto" and Edad >= 18 and Almacenamiento >= 100:
            print(Fore.YELLOW + "Recomendacion: Grand Theft Auto V.")
        
        elif Jugadores == 1 and Edad >= 10:
            print(Fore.YELLOW + "Recomendacion: Hollow Knight.")
        
        elif Jugadores >= 2 and Tipo_Presupuesto == "Bajo":
            print(Fore.YELLOW + "Recomendacion: It Takes Two.")

    elif Genero == "Accion":

        if Edad >= 13 and Tipo_Presupuesto == "Alto": 
            print(Fore.YELLOW + "Recomendacion: Counter-Strike 2.")
        
        elif Edad >= 18 and Tipo_Presupuesto == "Alto":
            print(Fore.YELLOW + "Recomendacion: Cyberpunk 2077.")

    elif Genero == "Terror":
        if Jugadores == 1 and Tipo_Presupuesto == "Bajo":
            print(Fore.YELLOW + "Recomendacion: Outlast.")
        elif Jugadores >= 2 and Tipo_Presupuesto == "Medio":
            print(Fore.YELLOW + "Recomendacion: Phasmophobia.")

print(Fore.GREEN + "Gracias por usar el sistema de recomendaciones, " + Nick + "!")
