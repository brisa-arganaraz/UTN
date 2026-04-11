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

if Genero == "Terror" and not Edad >= 16:
    print("Lo sentimos", Nick, ", los juegos de Terror son para mayores de 16 años. No podemos hacerte una recomendacion.")

elif Genero == "Accion" and not Edad >= 13:
    print("Lo sentimos", Nick, ", los juegos de Accion son para mayores de 13 años. No podemos hacerte una recomendacion.")

elif Genero == "Aventura" and not Edad >= 10:
    print("Lo sentimos", Nick, ", los juegos de Aventura son para mayores de 10 años. No podemos hacerte una recomendacion.")


if Plataforma == "PC":
    
    
    if Genero == "Aventura":

        if Jugadores == 1 and Presupuesto >= 1000 and Edad >= 10:
           Fore.RESET + print("Recomendación 1: Hollow Knight.")
        
        if Jugadores >= 2 and Presupuesto >= 3000 and Edad >= 10:
            print("Recomendación 2: It Takes Two.")
            
        if Almacenamiento >= 100 and Presupuesto >= 5000 and Edad >= 18:
            print("Recomendación 3: Grand Theft Auto V.")

    if Genero == "Accion":

        if Jugadores >= 1 and Presupuesto >= 500 and Edad >= 13:
            print("Recomendación 1: Counter-Strike 2.")

        if Jugadores == 1 and Edad >= 18 and Presupuesto >= 8000:
            print("Recomendación 2: Cyberpunk 2077.")

        if Jugadores >= 4 and Presupuesto >= 4000:
            print("Recomendación 3: Left 4 Dead 2.")

            print("Recomendación 3: Resident Evil 4 Remake.")

