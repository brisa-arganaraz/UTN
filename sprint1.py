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

if Plataforma == "Playstation":
    if Formato == "Digital":
        if Genero == "Terror" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >=1 and Cantidad == 1:
            print("Un buen juego de Playstation para ti seria Resident Evil 5, se acomoda a a tu necesidades y cumple perfectamente con tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif Genero == "Terror" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad >=2:
            print("Algunos juegos que te podria recomendarar en base a tus especificaciones seria la saga completa del Resident Evil")
        elif Genero == "Terro" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad >=1:
            print("Algunos juegos para jugar con tus amigos seria Back 4 Blood, Phasmophobia, Dying Light 2: Stay Human, estos cumpliran con tus especificaciones totalmente")
        elif Genero == "Terror" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad >=1:
            print("Un buen juego de Playstation para ti seria Resident Evil Village, se acomoda a a tu necesidades y cumple perfectamente con tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
