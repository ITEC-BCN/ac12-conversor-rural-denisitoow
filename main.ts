function actualizar_movimiento () {
    if (menu_abierto) {
        controller.moveSprite(jugador, 0, 0)
    } else {
        controller.moveSprite(jugador, velocidad_x, velocidad_y)
    }
}
function actualizar_interaccion_npc () {
    if (controller.A.isPressed() && jugador.overlapsWith(npc) && !(menu_abierto)) {
        crear_menu()
        pause(500)
    }
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (!(menu_abierto)) {
        animation.runImageAnimation(
        jugador,
        assets.animation`animado_arriba`,
        300,
        true
        )
    }
})
function convertir_a_lena_patatas (kg_patatas: number) {
    return Math.round(kg_patatas / 1.5 * PATATA_LENA * 100) / 100
}
function crear_menu () {
    menu_abierto = true
    my_menu2 = miniMenu.createMenu(
    miniMenu.createMenuItem("Gallinas", assets.image`pollo`),
    miniMenu.createMenuItem("Patatas", assets.image`papas`),
    miniMenu.createMenuItem("Cabras", assets.image`cabra`),
    miniMenu.createMenuItem("Huevos", assets.image`huevo`),
    miniMenu.createMenuItem("Caballos", assets.image`caballo`),
    miniMenu.createMenuItem("Tabla de precios", assets.image`precios`),
    miniMenu.createMenuItem("Salir", assets.image`salir`)
    )
    my_menu2.setDimensions(120, 100)
    my_menu2.setPosition(80, 60)
    my_menu2.setTitle("Conversor Rural")
    my_menu2.onButtonPressed(controller.A, function (selection, selectedIndex) {
        my_menu2.close()
        menu_option = selectedIndex
    })
}
function empujar_atras () {
    jugador.vx = 0
    jugador.vy = -150
    pause(200)
    jugador.vy = 0
}
function validar_animal_entero (cantidad: number, nombre_animal: string) {
    if (cantidad <= 0) {
        game.splash("Error!", "La cantidad debe ser mayor que 0")
        return false
    }
    if (cantidad != Math.floor(cantidad)) {
        game.splash("Error!", "No puedes pedir medio " + nombre_animal + "!")
        return false
    }
    return true
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (!(menu_abierto)) {
        animation.runImageAnimation(
        jugador,
        assets.animation`animado_izq`,
        300,
        true
        )
    }
})
function convertir_a_lena_gallinas (cantidad_gallinas: number) {
    return Math.round(cantidad_gallinas * GALLINA_LENA * 100) / 100
}
function procesar_gallinas () {
    menu_abierto = false
    my_menu2 = null
cantidad6 = game.askForNumber("Cuantas gallinas quieres?", 2)
    if (validar_animal_entero(cantidad6, "gallina")) {
        mostrar_resultado(cantidad6, "gallinas", convertir_a_lena_gallinas(cantidad6))
    }
    pause(800)
    empujar_atras()
}
function procesar_opciones_menu () {
    if (menu_option != -1) {
        gestionar_opcion_menu(menu_option)
menu_option = -1
    }
}
function mostrar_resultado (cantidad2: number, producto: string, lena_necesaria: number) {
    game.splash("" + cantidad2 + " " + producto + " =", "" + lena_necesaria + " kg de lena")
}
function validar_cantidad_positiva (cantidad3: number) {
    if (cantidad3 <= 0) {
        game.splash("Error!", "La cantidad debe ser mayor que 0")
        return false
    }
    return true
}
function convertir_a_lena_caballos (cantidad_caballos: number) {
    return Math.round(cantidad_caballos * CABALLO_LENA * 100) / 100
}
function convertir_a_lena_cabras (cantidad_cabras: number) {
    return Math.round(cantidad_cabras * CABRA_LENA * 100) / 100
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (!(menu_abierto)) {
        animation.runImageAnimation(
        jugador,
        assets.animation`animado_der`,
        300,
        true
        )
    }
})
function procesar_salida () {
    menu_abierto = false
    my_menu2 = null
game.splash("Hasta pronto!", "Gracias por venir al mercado")
    menu_option = -1
    pause(800)
    empujar_atras()
}
function procesar_cabras () {
    menu_abierto = false
    my_menu2 = null
cantidad32 = game.askForNumber("Cuantas cabras quieres?", 2)
    if (validar_animal_entero(cantidad32, "cabra")) {
        mostrar_resultado(cantidad32, "cabras", convertir_a_lena_cabras(cantidad32))
    }
    pause(800)
    empujar_atras()
}
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    if (!(menu_abierto)) {
        animation.runImageAnimation(
        jugador,
        assets.animation`animado_abajo`,
        300,
        true
        )
    }
})
function procesar_patatas () {
    menu_abierto = false
    my_menu2 = null
cantidad22 = game.askForNumber("Cuantos kg de patatas?", 2)
    if (validar_cantidad_positiva(cantidad22)) {
        mostrar_resultado(cantidad22, "kg de patatas", convertir_a_lena_patatas(cantidad22))
    }
    pause(800)
    empujar_atras()
}
function convertir_a_lena_huevos (cantidad_huevos: number) {
    return Math.round(cantidad_huevos / 12 * HUEVOS_LENA * 100) / 100
}
function actualizar_texto_npc () {
    if (jugador.overlapsWith(npc) && !(menu_abierto)) {
        npc.sayText("Pulsa A para abrir el conversor", 500, false)
    } else {
        npc.sayText("", 0, false)
    }
}
function procesar_caballos () {
    menu_abierto = false
    my_menu2 = null
cantidad5 = game.askForNumber("Cuantos caballos quieres?", 2)
    if (validar_animal_entero(cantidad5, "caballo")) {
        mostrar_resultado(cantidad5, "caballos", convertir_a_lena_caballos(cantidad5))
    }
    pause(800)
    empujar_atras()
}
function mostrar_tabla_precios () {
    menu_abierto = false
    my_menu2 = null
let texto = "TABLA DE PRECIOS\n\n"
texto = "" + texto + `
        1 Gallina = 6 kg lena
        `
    texto = "" + texto + `
        1.5 kg Patatas = 2 kg lena
        `
    texto = "" + texto + "1 Cabra = 5 kg lena\n"
    texto = "" + texto + `
        12 Huevos = 3 kg lena
        `
    texto = "" + texto + "1 Caballo = 12 kg lena"
    game.showLongText(texto, DialogLayout.Center)
    pause(800)
    empujar_atras()
}
function procesar_huevos () {
    menu_abierto = false
    my_menu2 = null
cantidad4 = game.askForNumber("Cuantos huevos quieres?", 2)
    if (validar_cantidad_positiva(cantidad4)) {
        mostrar_resultado(cantidad4, "huevos", convertir_a_lena_huevos(cantidad4))
    }
    pause(800)
    empujar_atras()
}
let cantidad4 = 0
let cantidad5 = 0
let cantidad22 = 0
let cantidad32 = 0
let cantidad6 = 0
let menu_abierto = false
let npc: Sprite = null
let jugador: Sprite = null
let CABALLO_LENA = 0
let HUEVOS_LENA = 0
let CABRA_LENA = 0
let PATATA_LENA = 0
let GALLINA_LENA = 0
let velocidad_y = 0
let velocidad_x = 0
let my_menu2 : miniMenu.MenuSprite = null
let menu_option = 0
menu_option = -1
velocidad_x = 100
velocidad_y = 100
GALLINA_LENA = 6
PATATA_LENA = 2
CABRA_LENA = 5
HUEVOS_LENA = 3
CABALLO_LENA = 12
jugador = sprites.create(assets.image`jugador`, SpriteKind.Player)
npc = sprites.create(assets.image`npc`, SpriteKind.Enemy)
npc.setPosition(80, 90)
jugador.setStayInScreen(true)
controller.moveSprite(jugador, velocidad_x, velocidad_y)
scene.setBackgroundImage(assets.image`fondo`)
game.showLongText("Bienvenido al CONVERSOR RURAL de Alcubilla de Avellaneda", DialogLayout.Bottom)
function gestionar_opcion_menu(opcion: any) {
    if (opcion == 0) {
        procesar_gallinas()
    } else if (opcion == 1) {
        procesar_patatas()
    } else if (opcion == 2) {
        procesar_cabras()
    } else if (opcion == 3) {
        procesar_huevos()
    } else if (opcion == 4) {
        procesar_caballos()
    } else if (opcion == 5) {
        mostrar_tabla_precios()
    } else if (opcion == 6) {
        procesar_salida()
    }
    
}
game.onUpdate(function () {
    actualizar_interaccion_npc()
    actualizar_texto_npc()
    actualizar_movimiento()
    procesar_opciones_menu()
})
