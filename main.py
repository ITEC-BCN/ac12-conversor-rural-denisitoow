def on_up_pressed():
    if not (menu_abierto):
        animation.run_image_animation(jugador,
            assets.animation("""
                animado_arriba
                """),
            300,
            True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def convertir_a_lena_patatas(kg_patatas: number):
    return Math.round(kg_patatas / 1.5 * PATATA_LENA * 100) / 100

def crear_menu():
    global menu_abierto, my_menu2
    menu_abierto = True
    my_menu2 = miniMenu.create_menu(miniMenu.create_menu_item("Gallinas", assets.image("""
            pollo
            """)),
        miniMenu.create_menu_item("Patatas", assets.image("""
            papas
            """)),
        miniMenu.create_menu_item("Cabras", assets.image("""
            cabra
            """)),
        miniMenu.create_menu_item("Huevos", assets.image("""
            huevo
            """)),
        miniMenu.create_menu_item("Caballos", assets.image("""
            caballo
            """)),
        miniMenu.create_menu_item("Tabla de precios", assets.image("""
            precios
            """)),
        miniMenu.create_menu_item("Salir", assets.image("""
            salir
            """)))
    my_menu2.set_dimensions(120, 100)
    my_menu2.set_position(80, 60)
    my_menu2.set_title("Conversor Rural")
    
    def on_button_pressed(selection, selectedIndex):
        global menu_option
        my_menu2.close()
        menu_option = selectedIndex
    my_menu2.on_button_pressed(controller.A, on_button_pressed)

def empujar_atras():
    jugador.vx = 0
    jugador.vy = -150
    pause(200)
    jugador.vy = 0

def validar_animal_entero(cantidad: number, nombre_animal: str):
    if cantidad <= 0:
        game.splash("Error!", "La cantidad debe ser mayor que 0")
        return False
    if cantidad != Math.floor(cantidad):
        game.splash("Error!", "No puedes pedir medio " + nombre_animal + "!")
        return False
    return True

def on_left_pressed():
    if not (menu_abierto):
        animation.run_image_animation(jugador,
            assets.animation("""
                animado_izq
                """),
            300,
            True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def convertir_a_lena_gallinas(cantidad_gallinas: number):
    return Math.round(cantidad_gallinas * GALLINA_LENA * 100) / 100

def procesar_gallinas():
    global cantidad6, menu_abierto, my_menu2
    menu_abierto = False
    my_menu2 = None
    cantidad6 = game.ask_for_number("Cuantas gallinas quieres?", 2)
    if validar_animal_entero(cantidad6, "gallina"):
        mostrar_resultado(cantidad6, "gallinas", convertir_a_lena_gallinas(cantidad6))
    pause(800)
    empujar_atras()

def mostrar_resultado(cantidad2: number, producto: str, lena_necesaria: number):
    game.splash("" + str(cantidad2) + " " + producto + " =",
        "" + str(lena_necesaria) + " kg de lena")

def validar_cantidad_positiva(cantidad3: number):
    if cantidad3 <= 0:
        game.splash("Error!", "La cantidad debe ser mayor que 0")
        return False
    return True

def convertir_a_lena_caballos(cantidad_caballos: number):
    return Math.round(cantidad_caballos * CABALLO_LENA * 100) / 100

def convertir_a_lena_cabras(cantidad_cabras: number):
    return Math.round(cantidad_cabras * CABRA_LENA * 100) / 100

def on_right_pressed():
    if not (menu_abierto):
        animation.run_image_animation(jugador,
            assets.animation("""
                animado_der
                """),
            300,
            True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def procesar_salida():
    global menu_abierto, my_menu2, menu_option
    menu_abierto = False
    my_menu2 = None
    game.splash("Hasta pronto!", "Gracias por venir al mercado")
    menu_option = -1
    pause(800)
    empujar_atras()

def procesar_cabras():
    global cantidad32, menu_abierto, my_menu2
    menu_abierto = False
    my_menu2 = None
    cantidad32 = game.ask_for_number("Cuantas cabras quieres?", 2)
    if validar_animal_entero(cantidad32, "cabra"):
        mostrar_resultado(cantidad32, "cabras", convertir_a_lena_cabras(cantidad32))
    pause(800)
    empujar_atras()

def on_down_pressed():
    if not (menu_abierto):
        animation.run_image_animation(jugador,
            assets.animation("""
                animado_abajo
                """),
            300,
            True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def procesar_patatas():
    global cantidad22, menu_abierto, my_menu2
    menu_abierto = False
    my_menu2 = None
    cantidad22 = game.ask_for_number("Cuantos kg de patatas?", 2)
    if validar_cantidad_positiva(cantidad22):
        mostrar_resultado(cantidad22,
            "kg de patatas",
            convertir_a_lena_patatas(cantidad22))
    pause(800)
    empujar_atras()

def convertir_a_lena_huevos(cantidad_huevos: number):
    return Math.round(cantidad_huevos / 12 * HUEVOS_LENA * 100) / 100

def procesar_caballos():
    global cantidad5, menu_abierto, my_menu2
    menu_abierto = False
    my_menu2 = None
    cantidad5 = game.ask_for_number("Cuantos caballos quieres?", 2)
    if validar_animal_entero(cantidad5, "caballo"):
        mostrar_resultado(cantidad5, "caballos", convertir_a_lena_caballos(cantidad5))
    pause(800)
    empujar_atras()

def mostrar_tabla_precios():
    global menu_abierto, my_menu2
    menu_abierto = False
    my_menu2 = None
    texto = "TABLA DE PRECIOS\n\n"
    texto = "" + texto + """
        1 Gallina = 6 kg lena
        """
    texto = "" + texto + """
        1.5 kg Patatas = 2 kg lena
        """
    texto = "" + texto + "1 Cabra = 5 kg lena\n"
    texto = "" + texto + """
        12 Huevos = 3 kg lena
        """
    texto = "" + texto + "1 Caballo = 12 kg lena"
    game.show_long_text(texto, DialogLayout.CENTER)
    pause(800)
    empujar_atras()

def procesar_huevos():
    global cantidad4, menu_abierto, my_menu2
    menu_abierto = False
    my_menu2 = None
    cantidad4 = game.ask_for_number("Cuantos huevos quieres?", 2)
    if validar_cantidad_positiva(cantidad4):
        mostrar_resultado(cantidad4, "huevos", convertir_a_lena_huevos(cantidad4))
    pause(800)
    empujar_atras()

cantidad4 = 0
cantidad5 = 0
cantidad22 = 0
cantidad32 = 0
cantidad6 = 0
menu_abierto = False
jugador: Sprite = None
CABALLO_LENA = 0
HUEVOS_LENA = 0
CABRA_LENA = 0
PATATA_LENA = 0
GALLINA_LENA = 0
menu_option = 0
my_menu2: miniMenu.MenuSprite = None
menu_option = -1
velocidad_x = 100
velocidad_y = 100
GALLINA_LENA = 6
PATATA_LENA = 2
CABRA_LENA = 5
HUEVOS_LENA = 3
CABALLO_LENA = 12
jugador = sprites.create(assets.image("""
    jugador
    """), SpriteKind.player)
npc = sprites.create(assets.image("""
    npc
    """), SpriteKind.enemy)
npc.set_position(80, 90)
jugador.set_stay_in_screen(True)
controller.move_sprite(jugador, velocidad_x, velocidad_y)
scene.set_background_image(assets.image("""
    fondo
    """))
game.show_long_text("Bienvenido al CONVERSOR RURAL de Alcubilla de Avellaneda",
    DialogLayout.BOTTOM)

def gestionar_opcion_menu(opcion: any):
    if opcion == 0:
        procesar_gallinas()
    elif opcion == 1:
        procesar_patatas()
    elif opcion == 2:
        procesar_cabras()
    elif opcion == 3:
        procesar_huevos()
    elif opcion == 4:
        procesar_caballos()
    elif opcion == 5:
        mostrar_tabla_precios()
    elif opcion == 6:
        procesar_salida()

def actualizar_interaccion_npc():
    if controller.A.is_pressed() and jugador.overlaps_with(npc) and not (menu_abierto):
        crear_menu()
        pause(500)

def actualizar_texto_npc():
    if jugador.overlaps_with(npc) and not (menu_abierto):
        npc.say_text("Pulsa A para abrir el conversor", 500, False)
    else:
        npc.say_text("", 0, False)

def actualizar_movimiento():
    if menu_abierto:
        controller.move_sprite(jugador, 0, 0)
    else:
        controller.move_sprite(jugador, velocidad_x, velocidad_y)

def procesar_opciones_menu():
    global menu_option
    if menu_option != -1:
        gestionar_opcion_menu(menu_option)
        menu_option = -1

def on_update():
    actualizar_interaccion_npc()
    actualizar_texto_npc()
    actualizar_movimiento()
    procesar_opciones_menu()

game.on_update(on_update)