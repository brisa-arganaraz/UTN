from colorama import *
init()

nick = input(Fore.BLUE + "Ingrese su Nick de jugador: ")
print(Fore.GREEN + "Hola", nick, "a continuacion te pedire que escribas tu Mail para poder recibir un correo con tu recibo y las especificaciones de tu pedido")
mail = input(Fore.BLUE + "Ingrese su Mail: ")

if "@" not in mail:
    print(Fore.RED + "Mail invalido. Asegurese de incluir '@' en su direccion de correo.")
    mail = input(Fore.BLUE + "Ingrese su Mail nuevamente: ")

print(Fore.GREEN + "Perfecto, ahora te ire pidiendo datos que me permitiran brindarte un juego de tu agrado")
plataforma = input(Fore.BLUE + "Ingrese la plataforma en la cual juega (Playstation/PC/Mobile): ")
formato = input(Fore.BLUE + "Ingrese el formato de juego que desea (Fisico/Digital): ")
genero = input(Fore.BLUE + "Ingrese el Genero de juego que prefiere (Terror/Accion/Aventura): ")
edad = int(input(Fore.BLUE + "Ingrese su edad: "))
almacenamiento = int(input(Fore.BLUE + "Ingrese su capacidad de almacenamiento en GB: "))
presupuesto = int(input(Fore.BLUE + "Ingrese su presupuesto: "))
jugadores = int(input(Fore.BLUE + "Cantidad de jugadores: "))
cantidad = int(input(Fore.BLUE + "Cantidad de juegos que desea comprar: "))
acepta_terminos = input(Fore.BLUE + "¿Acepta los términos y condiciones? (S/N): ")

if acepta_terminos != "S":
    print(Fore.RED + "No puede continuar sin aceptar los términos.")
    exit()

if acepta_terminos != "S":
    print(Fore.RED + "No puede continuar sin aceptar los términos.")

if plataforma == "PC":
    print(Fore.WHITE + "=" * 50)
    print(Fore.CYAN + "          RECOMENDACIONES PARA PC")
    print(Fore.WHITE + "=" * 50)

    if genero == "Terror" and edad < 16:
        print(Fore.RED + "Lo sentimos " + nick + ", Terror es para mayores de 16.")
        genero = input(Fore.BLUE + "Escriba el nuevo Genero: ")
    
    if genero == "Accion" and edad < 13:
        print(Fore.RED + "Lo sentimos "+ nick +", Acción es para mayores de 13.")
        genero = input(Fore.BLUE + "Escriba el nuevo Genero: ")

    if presupuesto < 2000:
        print(Fore.RED + "Error: Presupuesto insuficiente.")
        presupuesto = int(input(Fore.WHITE + "Reingrese presupuesto (mínimo 2000): "))

    if presupuesto >= 8000:
        tipo_presupuesto = "Alto"
    elif presupuesto >= 5000:
        tipo_presupuesto = "Medio"
    else:
        tipo_presupuesto = "Bajo"

    print(Fore.CYAN + "Analizando opciones para " + nick + "..." )

    if genero == "Aventura":
        if jugadores == 1 and tipo_presupuesto == "Alto" and edad >= 18 and almacenamiento >= 100:
            print(Fore.YELLOW + "Recomendacion: Grand Theft Auto V.")
        elif jugadores == 1 and edad >= 10:
            print(Fore.YELLOW + "Recomendacion: Hollow Knight.")
        elif jugadores >= 2:
            print(Fore.YELLOW + "Recomendacion: It Takes Two.")

    elif genero == "Accion":
        if edad >= 18 and tipo_presupuesto == "Alto":
            print(Fore.YELLOW + "Recomendacion: Cyberpunk 2077.")
        elif edad >= 13: 
            print(Fore.YELLOW + "Recomendacion: Counter-Strike 2.")

    elif genero == "Terror":
        if jugadores == 1:
            print(Fore.YELLOW + "Recomendacion: Outlast.")
        elif jugadores >= 2 and tipo_presupuesto != "Bajo":
            print(Fore.YELLOW + "Recomendacion: Phasmophobia.")

print(Fore.GREEN + "Gracias por usar el sistema de recomendaciones, " + nick + "!")
