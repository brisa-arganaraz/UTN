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

        # --- TERROR ---
        if Genero == "Terror" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1:
            print("Un buen juego de Playstation para ti seria Resident Evil 5, se acomoda a " \
            "tus necesidades y cumple perfectamente con tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif Genero == "Terror" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad >= 2:
            print("Algunos juegos que te podria recomendar en base a tus especificaciones seria la saga completa " \
            "del Resident Evil")
        elif Genero == "Terror" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Algunos juegos para jugar con tus amigos seria Back 4 Blood, Phasmophobia, Dying Light 2: Stay Human," \
            " estos cumpliran con tus especificaciones totalmente")
        elif Genero == "Terror" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un buen juego de Playstation para ti seria Resident Evil Village, se acomoda a tus necesidades y cumple " \
            "perfectamente con tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif Genero == "Terror" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Algunos juegos que te podria recomendar en base a tus especificaciones seria The Dark Pictures Anthology:" \
            " House of Ashes, World War Z y Friday the 13th: The Game")
        elif Genero == "Terror" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Little Nightmares")
        elif Genero == "Terror" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Luigi's Mansion 3")
        elif Genero == "Terror" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Spooky's Jump Scare Mansion")
        elif Genero == "Terror" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria The Dark Pictures " \
            "Anthology: Little Hope")

        # --- ACCION ---
        elif Genero == "Accion" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1:
            print("Un buen juego de Playstation para ti seria Spider-Man: Miles Morales, se acomoda a tus necesidades y " \
            "cumple perfectamente con tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif Genero == "Accion" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad >= 2:
            print("Algunos juegos que te podria recomendar en base a tus especificaciones seria Ratchet & Clank: Rift" \
            " Apart y Sackboy: A Big Adventure")
        elif Genero == "Accion" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Algunos juegos para jugar con tus amigos seria Kingdom Hearts III y Minecraft, cumpliran con tus " \
            "especificaciones totalmente")
        elif Genero == "Accion" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un buen juego de Playstation para ti seria Uncharted: The Lost Legacy, se acomoda a tus necesidades" \
            " y cumple perfectamente con tu presupuesto y almacenamiento")
        elif Genero == "Accion" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Algunos juegos que te podria recomendar en base a tus especificaciones seria Crash Bandicoot 4: It's About Time")
        elif Genero == "Accion" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Lego Marvel Super Heroes 2")
        elif Genero == "Accion" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Knack 2")
        elif Genero == "Accion" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Horizon Zero Dawn")
        elif Genero == "Accion" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Plants vs. " \
            "Zombies: Battle for Neighborville")

        # --- AVENTURA ---
        elif Genero == "Aventura" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1:
            print("Un buen juego de Playstation para ti seria The Last of Us Part II, se acomoda a tus necesidades y " \
            "cumple perfectamente con tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif Genero == "Aventura" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad >= 2:
            print("Algunos juegos que te podria recomendar en base a tus especificaciones seria God of War Ragnarok y Ghost of Tsushima")
        elif Genero == "Aventura" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Algunos juegos para jugar con tus amigos seria It Takes Two y A Way Out, estos cumpliran con tus " \
            "especificaciones totalmente")
        elif Genero == "Aventura" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un buen juego de Playstation para ti seria Firewatch, se acomoda a tus necesidades y cumple perfectamente " \
            "con tu presupuesto y almacenamiento")
        elif Genero == "Aventura" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un buen juego de Playstation para ti seria Ghost of Tsushima, se acomoda a tus necesidades y cumple" \
            " perfectamente con tu presupuesto, ademas de ser unicamente apto para +18 años")
        elif Genero == "Aventura" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria The Legend of " \
            "Zelda: Breath of the Wild")
        elif Genero == "Aventura" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Crash Bandicoot N. Sane Trilogy")
        elif Genero == "Aventura" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Astro's Playroom")
        elif Genero == "Aventura" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Sackboy: A Big Adventure")

    if Formato == "Fisico":

        # --- TERROR ---
        if Genero == "Terror" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1:
            print("Un buen juego de Playstation para ti seria Resident Evil 2 Remake, se acomoda a tus necesidades y " \
            "cumple perfectamente con tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif Genero == "Terror" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad >= 2:
            print("Algunos juegos que te podria recomendar en base a tus especificaciones seria la saga de Silent Hill y Dead Space")
        elif Genero == "Terror" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Algunos juegos para jugar con tus amigos seria Until Dawn y The Dark Pictures Anthology, estos cumpliran " \
            "con tus especificaciones totalmente")
        elif Genero == "Terror" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un buen juego de Playstation para ti seria Outlast, se acomoda a tus necesidades y cumple perfectamente con" \
            " tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif Genero == "Terror" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Algunos juegos que te podria recomendar en base a tus especificaciones seria Alien Isolation y Observer")
        elif Genero == "Terror" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Little Nightmares II")
        elif Genero == "Terror" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Luigi's Mansion 3")
        elif Genero == "Terror" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Five Nights at " \
            "Freddy's: Security Breach")
        elif Genero == "Terror" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Ghostbusters: " \
            "The Video Game Remastered")

        # --- ACCION ---
        elif Genero == "Accion" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1:
            print("Un buen juego de Playstation para ti seria God of War, se acomoda a tus necesidades y cumple perfectamente " \
            "con tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif Genero == "Accion" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad >= 2:
            print("Algunos juegos que te podria recomendar en base a tus especificaciones seria la saga de Devil May Cry y Sekiro:" \
            " Shadows Die Twice")
        elif Genero == "Accion" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Algunos juegos para jugar con tus amigos seria Mortal Kombat 11 y Tekken 7, estos cumpliran con tus especificaciones" \
            " totalmente")
        elif Genero == "Accion" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un buen juego de Playstation para ti seria Jak and Daxter: The Precursor Legacy, se acomoda a tus necesidades y " \
            "cumple perfectamente con tu presupuesto y almacenamiento")
        elif Genero == "Accion" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Algunos juegos que te podria recomendar en base a tus especificaciones seria Doom Eternal y Wolfenstein II: The New Colossus")
        elif Genero == "Accion" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Spider-Man para PS4")
        elif Genero == "Accion" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Rayman Legends")
        elif Genero == "Accion" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Sonic Mania")
        elif Genero == "Accion" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Lego City Undercover")

        # --- AVENTURA ---
        elif Genero == "Aventura" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1:
            print("Un buen juego de Playstation para ti seria Red Dead Redemption 2, se acomoda a tus necesidades y cumple " \
            "perfectamente con tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
        elif Genero == "Aventura" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad >= 2:
            print("Algunos juegos que te podria recomendar en base a tus especificaciones seria la saga de Uncharted y Horizon Forbidden West")
        elif Genero == "Aventura" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Algunos juegos para jugar con tus amigos seria It Takes Two y A Way Out, estos cumpliran con tus especificaciones totalmente")
        elif Genero == "Aventura" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un buen juego de Playstation para ti seria Journey, se acomoda a tus necesidades y cumple perfectamente con " \
            "tu presupuesto y almacenamiento")
        elif Genero == "Aventura" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Algunos juegos que te podria recomendar en base a tus especificaciones seria Control y Outer Wilds")
        elif Genero == "Aventura" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Minecraft")
        elif Genero == "Aventura" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Spyro Reignited Trilogy")
        elif Genero == "Aventura" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Ratchet & Clank")
        elif Genero == "Aventura" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
            print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Astro's Playroom")      


# --- FALTA EL DE PC ACA ---


if Plataforma == "Mobile":

    # --- TERROR ---
    if Genero == "Terror" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1:
        print("Un buen juego de Mobile para ti seria Eyes: Scary Thriller, se acomoda a tus necesidades y cumple perfectamente con " \
        "tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
    elif Genero == "Terror" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad >= 2:
        print("Algunos juegos que te podria recomendar en base a tus especificaciones seria Granny y Identity V")
    elif Genero == "Terror" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Algunos juegos para jugar con tus amigos seria Dead by Daylight Mobile y Phasmophobia, estos cumpliran con tus " \
        "especificaciones totalmente")
    elif Genero == "Terror" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Un buen juego de Mobile para ti seria Five Nights at Freddy's, se acomoda a tus necesidades y cumple perfectamente" \
        " con tu presupuesto y almacenamiento")
    elif Genero == "Terror" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Algunos juegos que te podria recomendar en base a tus especificaciones seria Detention y The Room")
    elif Genero == "Terror" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Luigi's Mansion")
    elif Genero == "Terror" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Little Nightmares")
    elif Genero == "Terror" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Spooky's Jump Scare Mansion")
    elif Genero == "Terror" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Poppy Playtime")

    # --- ACCION ---
    elif Genero == "Accion" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1:
        print("Un buen juego de Mobile para ti seria Call of Duty Mobile, se acomoda a tus necesidades y cumple perfectamente con " \
        "tu presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
    elif Genero == "Accion" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad >= 2:
        print("Algunos juegos que te podria recomendar en base a tus especificaciones seria PUBG Mobile y Free Fire MAX")
    elif Genero == "Accion" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Algunos juegos para jugar con tus amigos seria Brawl Stars y Mobile Legends, estos cumpliran con tus especificaciones " \
        "totalmente")
    elif Genero == "Accion" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Un buen juego de Mobile para ti seria Dead Cells, se acomoda a tus necesidades y cumple perfectamente con tu presupuesto " \
        "y almacenamiento")
    elif Genero == "Accion" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Algunos juegos que te podria recomendar en base a tus especificaciones seria Shadowgun Legends y Modern Combat 5")
    elif Genero == "Accion" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Fortnite Mobile")
    elif Genero == "Accion" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Clash Royale")
    elif Genero == "Accion" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Subway Surfers")
    elif Genero == "Accion" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Temple Run 2")

    # --- AVENTURA ---
    elif Genero == "Aventura" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1:
        print("Un buen juego de Mobile para ti seria Genshin Impact, se acomoda a tus necesidades y cumple perfectamente con tu " \
        "presupuesto y almacenamiento, ademas de ser unicamente apto para +18 años")
    elif Genero == "Aventura" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad >= 2:
        print("Algunos juegos que te podria recomendar en base a tus especificaciones seria Alto's Odyssey y Pascal's Wager")
    elif Genero == "Aventura" and Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Algunos juegos para jugar con tus amigos seria Minecraft y Among Us, estos cumpliran con tus especificaciones totalmente")
    elif Genero == "Aventura" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Un buen juego de Mobile para ti seria Monument Valley, se acomoda a tus necesidades y cumple perfectamente con tu" \
        " presupuesto y almacenamiento")
    elif Genero == "Aventura" and Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Algunos juegos que te podria recomendar en base a tus especificaciones seria Oceanhorn y Oxenfree")
    elif Genero == "Aventura" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Minecraft")
    elif Genero == "Aventura" and not Edad >= 18 and Almacenamiento >= 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Angry Birds 2")
    elif Genero == "Aventura" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto >= 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Stardew Valley")
    elif Genero == "Aventura" and not Edad >= 18 and Almacenamiento < 1000 and Presupuesto < 100000 and Jugadores >= 1 and Cantidad == 1 or Cantidad > 2:
        print("Un juego para alguien menor de 18 años y cumpliendo con las demas especificaciones seria Cut the Rope Remastered")
