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

if Presupuesto > 0 and Presupuesto < 10:
    Presupuesto == "Presupuesto_Bajo"
elif Presupuesto < 30:
        Presupuesto == "Presupuesto_Medio"
else Presupuesto > 30:
      Presupuesto == "Presupuesto_Alto"

Almacenamiento = int(input("Ingrese su capacidad de almacenamiento en GB: "))
while Almacenamiento < 10:
    Almacenamiento = int(input("Error, tiene muy poco Almacenamiento"))

Jugadores = int(input("Cantidad de jugadores: "))
while Jugadores < 0 and Jugadores > 4:
    Jugadores = int(input("Error, reingrese el numero de jugadores (1 y 4): "))
    Jugadores > 0 Jugadores < 2:
    Jugadores == "Single Player"
    Jugadores <= 4:
    Jugadores == "Multi player"

Cantidad = int(input("Cantidad de juegos que desea comprar: "))
Jugadores = int(input("Cantidad de jugadores: "))
if Plataforma == Mobile and Presupuesto == Presupuesto_Minimo and Genero == Accion and Jugadores == single
     print ("Podria interesarte ")
     
     



Seguir = input("Quiere seguir comprando? (si/no): ")
while Seguir != "si" and seguir != "no" :
    Seguir = input("Reingrese opcion (si/no): ")

