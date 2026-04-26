# --- GRUPO 4 ---

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
while formato != "Fisico" and formato != "Digital":
    formato = input(Fore.BLUE + "ERROR, reingrese nuevamente el formato de juego que desea (Fisico/Digital): ")
genero = input(Fore.BLUE + "Ingrese el genero de juego que prefiere (Terror/Accion/Aventura): ")
while genero != "Terror" and genero != "Accion" and genero != "Aventura":
    genero = input(Fore.BLUE + "ERROR, reingrese nuevamente el genero del juego que desea (Terror/Accion/Aventura): ")
while True:
    edad_texto = input("Ingrese su edad: ")
    
    if edad_texto.strip() == "":
        print("ERROR... no puede estar vacío")
        continue
    
    if not edad_texto.isdigit():
        print("ERROR... debe ser un número")
        continue
    
    edad = int(edad_texto)

    if edad < 5 or edad > 90:
        print("ERROR... la edad debe estar entre 5 y 90 años")
        continue

    break
almacenamiento = int(input(Fore.BLUE + "Ingrese su capacidad de almacenamiento en GB: "))
while almacenamiento <= 0:
    almacenamiento = int(input("Error... el almacenamiento no puede ser menor o igual a 0, Reingrese nuevamente: "))
presupuesto = int(input(Fore.BLUE + "Ingrese su presupuesto: "))
while presupuesto <= 0:
    presupuesto = int(input("Error... El presupuesto no puede ser menor o igual a 0, reingrese nuevamente: "))
jugadores = int(input(Fore.BLUE + "Cantidad de jugadores: "))
while jugadores <= 0:
    print(Fore.RED + "Error: La cantidad de jugadores debe ser al menos 1.")
    jugadores = int(input(Fore.BLUE + "Ingrese la cantidad de jugadores nuevamente: "))
cantidad = int(input(Fore.BLUE + "Cantidad de juegos que desea comprar: "))
while cantidad <= 0:
    print(Fore.RED + "Error: Debe comprar al menos 1 juego.")
    cantidad = int(input(Fore.BLUE + "Ingrese la cantidad de juegos nuevamente: "))
acepta_terminos = input(Fore.BLUE + "¿Acepta los términos y condiciones? (S/N): ")
while acepta_terminos != "S" and acepta_terminos != "s" and acepta_terminos != "N" and acepta_terminos != "n":
    print(Fore.RED + "Error: Entrada no reconocida. Debe ingresar S o N.")
    acepta_terminos = input(Fore.BLUE + "Intente nuevamente (S/N): ")
if acepta_terminos != "S":
    print(Fore.RED + "No puede continuar sin aceptar los términos.")
    exit()

precio_juego = 10000
total_p = cantidad * precio_juego

if plataforma == "Playstation":

    print(Fore.WHITE + "=" * 50)
    print(Fore.CYAN + "     RECOMENDACIONES PARA PLAYSTATION")
    print(Fore.WHITE + "=" * 50)

    if genero == "Terror" and (edad >= 18 or jugadores >= 2):
        print(Fore.CYAN + "Nota: Contenido de terror habilitado para tu perfil.")

    if almacenamiento >= 1000 and (presupuesto >= 100000 or cantidad >= 2):
        print(Fore.CYAN + "Nota: Tu configuracion permite acceder a titulos de alta gama o compras multiples.")

    if (genero == "Accion" or genero == "Aventura") and edad >= 18:
        print(Fore.CYAN + "Nota: Tenes acceso completo al catalogo de " + genero + " para adultos.")

    if not (edad < 18 and genero == "Terror"):
        print(Fore.CYAN + "Nota: Tu combinacion de edad y genero no presenta restricciones criticas.")

    if 10000 <= presupuesto <= 80000:
        print(Fore.CYAN + "Nota: Presupuesto medio, ideal para titulos indie o juegos en oferta.")
    elif 80001 <= presupuesto <= 150000:
        print(Fore.CYAN + "Nota: Buen presupuesto, podes acceder a la mayoria de titulos del mercado.")
    elif presupuesto > 150000:
        print(Fore.CYAN + "Nota: Presupuesto alto, tenes acceso a cualquier titulo AAA disponible.")

    if formato == "Digital":

        # --- TERROR ---
        if genero == "Terror" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad == 1:
            print(Fore.YELLOW + "Un buen juego de Playstation para ti seria Resident Evil 5, se acomoda a "
            "tus necesidades y cumple perfectamente con tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif genero == "Terror" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 2:
            print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria la saga completa "
            "del Resident Evil")
        elif genero == "Terror" and edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Algunos juegos para jugar con tus amigos seria Back 4 Blood, Phasmophobia, Dying Light 2: Stay Human,"
            " estos cumpliran con tus especificaciones totalmente")
        elif genero == "Terror" and edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un buen juego de Playstation para ti seria Resident Evil Village, se acomoda a tus necesidades y cumple "
            "perfectamente con tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif genero == "Terror" and edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria The Dark Pictures Anthology:"
            " House of Ashes, World War Z y Friday the 13th: The Game")
        elif genero == "Terror" and not edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Little Nightmares")
        elif genero == "Terror" and not edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Luigi's Mansion 3")
        elif genero == "Terror" and not edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Spooky's Jump Scare Mansion")
        elif genero == "Terror" and not edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria The Dark Pictures "
            "Anthology: Little Hope")

        # --- ACCION ---
        elif genero == "Accion" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad == 1:
            print(Fore.YELLOW + "Un buen juego de Playstation para ti seria Spider-Man: Miles Morales, se acomoda a tus necesidades y "
            "cumple perfectamente con tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif genero == "Accion" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 2:
            print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria Ratchet & Clank: Rift"
            " Apart y Sackboy: A Big Adventure")
        elif genero == "Accion" and edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Algunos juegos para jugar con tus amigos seria Kingdom Hearts III y Minecraft, cumpliran con tus "
            "especificaciones totalmente")
        elif genero == "Accion" and edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un buen juego de Playstation para ti seria Uncharted: The Lost Legacy, se acomoda a tus necesidades"
            " y cumple perfectamente con tu presupuesto y almacenamiento")
        elif genero == "Accion" and edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria Crash Bandicoot 4: It's About Time")
        elif genero == "Accion" and not edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Lego Marvel Super Heroes 2")
        elif genero == "Accion" and not edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Knack 2")
        elif genero == "Accion" and not edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Horizon Zero Dawn")
        elif genero == "Accion" and not edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Plants vs. "
            "Zombies: Battle for Neighborville")

        # --- AVENTURA ---
        elif genero == "Aventura" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad == 1:
            print(Fore.YELLOW + "Un buen juego de Playstation para ti seria The Last of Us Part II, se acomoda a tus necesidades y "
            "cumple perfectamente con tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif genero == "Aventura" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 2:
            print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria God of War Ragnarok y Ghost of Tsushima")
        elif genero == "Aventura" and edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Algunos juegos para jugar con tus amigos seria It Takes Two y A Way Out, estos cumpliran con tus "
            "especificaciones totalmente")
        elif genero == "Aventura" and edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un buen juego de Playstation para ti seria Firewatch, se acomoda a tus necesidades y cumple perfectamente "
            "con tu presupuesto y almacenamiento")
        elif genero == "Aventura" and edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un buen juego de Playstation para ti seria Ghost of Tsushima, se acomoda a tus necesidades y cumple"
            " perfectamente con tu presupuesto, ademas de ser unicamente apto para +18 años")
        elif genero == "Aventura" and not edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria The Legend of "
            "Zelda: Breath of the Wild")
        elif genero == "Aventura" and not edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Crash Bandicoot N. Sane Trilogy")
        elif genero == "Aventura" and not edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Astro's Playroom")
        elif genero == "Aventura" and not edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Sackboy: A Big Adventure")

    if formato == "Fisico":

        # --- TERROR ---
        if genero == "Terror" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad == 1:
            print(Fore.YELLOW + "Un buen juego de Playstation para ti seria Resident Evil 2 Remake, se acomoda a tus necesidades y "
            "cumple perfectamente con tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif genero == "Terror" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 2:
            print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria la saga de Silent Hill y Dead Space")
        elif genero == "Terror" and edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Algunos juegos para jugar con tus amigos seria Until Dawn y The Dark Pictures Anthology, estos cumpliran "
            "con tus especificaciones totalmente")
        elif genero == "Terror" and edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un buen juego de Playstation para ti seria Outlast, se acomoda a tus necesidades y cumple perfectamente con"
            " tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif genero == "Terror" and edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria Alien Isolation y Observer")
        elif genero == "Terror" and not edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Little Nightmares II")
        elif genero == "Terror" and not edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Luigi's Mansion 3")
        elif genero == "Terror" and not edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Five Nights at "
            "Freddy's: Security Breach")
        elif genero == "Terror" and not edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Ghostbusters: "
            "The Video Game Remastered")

        # --- ACCION ---
        elif genero == "Accion" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad == 1:
            print(Fore.YELLOW + "Un buen juego de Playstation para ti seria God of War, se acomoda a tus necesidades y cumple perfectamente "
            "con tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif genero == "Accion" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 2:
            print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria la saga de Devil May Cry y Sekiro:"
            " Shadows Die Twice")
        elif genero == "Accion" and edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Algunos juegos para jugar con tus amigos seria Mortal Kombat 11 y Tekken 7, estos cumpliran con tus especificaciones"
            " totalmente")
        elif genero == "Accion" and edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un buen juego de Playstation para ti seria Jak and Daxter: The Precursor Legacy, se acomoda a tus necesidades y "
            "cumple perfectamente con tu presupuesto y almacenamiento")
        elif genero == "Accion" and edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria Doom Eternal y Wolfenstein II: The New Colossus")
        elif genero == "Accion" and not edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Spider-Man para PS4")
        elif genero == "Accion" and not edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Rayman Legends")
        elif genero == "Accion" and not edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Sonic Mania")
        elif genero == "Accion" and not edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Lego City Undercover")

        # --- AVENTURA ---
        elif genero == "Aventura" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad == 1:
            print(Fore.YELLOW + "Un buen juego de Playstation para ti seria Red Dead Redemption 2, se acomoda a tus necesidades y cumple "
            "perfectamente con tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif genero == "Aventura" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 2:
            print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria la saga de Uncharted y Horizon Forbidden West")
        elif genero == "Aventura" and edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Algunos juegos para jugar con tus amigos seria It Takes Two y A Way Out, estos cumpliran con tus especificaciones totalmente")
        elif genero == "Aventura" and edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un buen juego de Playstation para ti seria Journey, se acomoda a tus necesidades y cumple perfectamente con "
            "tu presupuesto y almacenamiento")
        elif genero == "Aventura" and edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria Control y Outer Wilds")
        elif genero == "Aventura" and not edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Minecraft")
        elif genero == "Aventura" and not edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Spyro Reignited Trilogy")
        elif genero == "Aventura" and not edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Ratchet & Clank")
        elif genero == "Aventura" and not edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
            print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Astro's Playroom")

# --- BLOQUE PC ---
if plataforma == "PC":

    print(Fore.WHITE + "=" * 50)
    print(Fore.CYAN + "          RECOMENDACIONES PARA PC")
    print(Fore.WHITE + "=" * 50)

    if genero == "Terror" and edad < 16:
        print(Fore.RED + "Lo sentimos " + nick + ", Terror es para mayores de 16.")
        genero = input(Fore.BLUE + "Escriba el nuevo Género: ")
    
    if genero == "Accion" and edad < 13:
        print(Fore.RED + "Lo sentimos "+ nick +", Acción es para mayores de 13.")
        genero = input(Fore.BLUE + "Escriba el nuevo Género: ")

    if presupuesto < 2000:
        print(Fore.RED + "Error: Presupuesto insuficiente.")
        presupuesto = int(input(Fore.WHITE + "Reingrese presupuesto (mínimo 2000): "))

    if almacenamiento < 100:
        print(Fore.RED + "Error: Almacenamiento insuficiente.")
        almacenamiento = int(input(Fore.WHITE + "Reingrese almacenamiento (minimo 100GB): "))    

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

if plataforma == "Mobile":

    print(Fore.WHITE + "=" * 50)
    print(Fore.CYAN + "        RECOMENDACIONES PARA MOBILE")
    print(Fore.WHITE + "=" * 50)

    # --- TERROR ---
    if genero == "Terror" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad == 1:
        print(Fore.YELLOW + "Un buen juego de Mobile para ti seria Eyes: Scary Thriller, se acomoda a tus necesidades y cumple perfectamente con "
        "tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
    elif genero == "Terror" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 2:
        print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria Granny y Identity V")
    elif genero == "Terror" and edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Algunos juegos para jugar con tus amigos seria Dead by Daylight Mobile y Phasmophobia, estos cumpliran con tus "
        "especificaciones totalmente")
    elif genero == "Terror" and edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Un buen juego de Mobile para ti seria Five Nights at Freddy's, se acomoda a tus necesidades y cumple perfectamente"
        " con tu presupuesto y almacenamiento")
    elif genero == "Terror" and edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria Detention y The Room")
    elif genero == "Terror" and not edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Luigi's Mansion")
    elif genero == "Terror" and not edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Little Nightmares")
    elif genero == "Terror" and not edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Spooky's Jump Scare Mansion")
    elif genero == "Terror" and not edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Poppy Playtime")

    # --- ACCION ---
    elif genero == "Accion" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad == 1:
        print(Fore.YELLOW + "Un buen juego de Mobile para ti seria Call of Duty Mobile, se acomoda a tus necesidades y cumple perfectamente con "
        "tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
    elif genero == "Accion" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 2:
        print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria PUBG Mobile y Free Fire MAX")
    elif genero == "Accion" and edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Algunos juegos para jugar con tus amigos seria Brawl Stars y Mobile Legends, estos cumpliran con tus especificaciones "
        "totalmente")
    elif genero == "Accion" and edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Un buen juego de Mobile para ti seria Dead Cells, se acomoda a tus necesidades y cumple perfectamente con tu presupuesto "
        "y almacenamiento")
    elif genero == "Accion" and edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria Shadowgun Legends y Modern Combat 5")
    elif genero == "Accion" and not edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Fortnite Mobile")
    elif genero == "Accion" and not edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Clash Royale")
    elif genero == "Accion" and not edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Subway Surfers")
    elif genero == "Accion" and not edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Temple Run 2")

    # --- AVENTURA ---
    elif genero == "Aventura" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad == 1:
        print(Fore.YELLOW + "Un buen juego de Mobile para ti seria Genshin Impact, se acomoda a tus necesidades y cumple perfectamente con tu "
        "presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
    elif genero == "Aventura" and edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 2:
        print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria Alto's Odyssey y Pascal's Wager")
    elif genero == "Aventura" and edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Algunos juegos para jugar con tus amigos seria Minecraft y Among Us, estos cumpliran con tus especificaciones totalmente")
    elif genero == "Aventura" and edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Un buen juego de Mobile para ti seria Monument Valley, se acomoda a tus necesidades y cumple perfectamente con tu"
        " presupuesto y almacenamiento")
    elif genero == "Aventura" and edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Algunos juegos que te podria recomendar en base a tus especificaciones seria Oceanhorn y Oxenfree")
    elif genero == "Aventura" and not edad >= 18 and almacenamiento >= 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Minecraft")
    elif genero == "Aventura" and not edad >= 18 and almacenamiento >= 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Angry Birds 2")
    elif genero == "Aventura" and not edad >= 18 and almacenamiento < 1000 and presupuesto >= 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Stardew Valley")
    elif genero == "Aventura" and not edad >= 18 and almacenamiento < 1000 and presupuesto < 100000 and jugadores >= 1 and cantidad >= 1:
        print(Fore.YELLOW + "Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Cut the Rope Remastered")


# --- RESUMEN FINAL ---
if total_p <= presupuesto:
    print(Fore.GREEN + "Perfecto, te alcanza para la compra")
else:
    print(Fore.RED + "Desgraciadamente no te alcanza")

print(Fore.WHITE + "=" * 50)
print(Fore.CYAN + "        RESUMEN DE TU PEDIDO")
print(Fore.WHITE + "=" * 50)
print(Fore.GREEN + "Jugador:            " + nick)
print(Fore.GREEN + "Plataforma:         " + plataforma)
print(Fore.GREEN + "Genero:             " + genero)
print(Fore.GREEN + "Formato:            " + formato)
print(Fore.GREEN + "Cantidad de juegos: " + str(cantidad))
print(Fore.GREEN + "Jugadores:          " + str(jugadores))
print(Fore.GREEN + "Almacenamiento:     " + str(almacenamiento) + " GB")
print(Fore.GREEN + "Total de tu compra: $" + str(total_p))
print(Fore.GREEN + "Mail de envio:      " + mail)
print(Fore.WHITE + "=" * 50)

print(Fore.GREEN + "Gracias por usar el sistema de recomendaciones, " + nick + "!")

resena = input(Fore.BLUE + "Desea dejar una reseña? (si/no): ")
if resena == "si":
    print(Fore.GREEN + "Muchas gracias por tu reseña, vuelva pronto!")
elif resena == "no":
    print(Fore.GREEN + "Muchas gracias, vuelva pronto!")
