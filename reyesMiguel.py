juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
}

inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}


def menu():
    print("========== Menu ==========")
    print("1. Stock por plataforma.")
    print("2. Búsqueda de juegos por rango de precio.")
    print("3. Actualizar precio de juego.")
    print("4. Agregar juego.")
    print("5. Eliminar juego.")
    print("6. Salir.")
    print("=========================================")

def selectOpcion():
    try:
        opc = input(int("Ingrese una opción: "))
    
        if opc is not [1, 2, 3, 4, 5, 6]:
            print("Ingrese una opción valida.")
            return 0

    except ValueError:
        print("Ingrese una opción valida.")
    
    return selectOpcion

def stock(plataforma, juegos):
    plataformaBuscar = input("Ingrese una plataforma: ")
    plataformaBuscar = plataformaBuscar.lower
    
    for plataforma in juegos:
        if plataformaBuscar == plataforma:
            print(juegos[0])

def busquedaPrecio(pMin, pMax, juegos, inventario):
    pMin = input("Ingrese un precio minimo: ")
    pMax = input("Ingrese un precio maximo: ")
    rango = len(inventario)
    
    juegosRango = []
    juegosRangoSinStock = []
    # for i in range(rango):
    pass
                

def validarCodigo(codigo: str) -> bool:
    if codigo != " ":
        return True
    elif codigo not in juegos or codigo not in inventario:
        return True
    else:
        return False
    
def validarTitulo(titulo: str) -> bool:
    if titulo == "" or titulo == " ":
        return False
    else:
        return True
    
def validarGenero(genero: str) -> bool:
    if genero == "" or genero == " ":
        return False
    else:
        return True
    
def validarPlataforma(plataforma: str) -> bool:
    if plataforma == "" or plataforma == " ":
        return False
    else:
        return True
    
def validarClasificacion(clasificacion: str) -> bool:
    if clasificacion not in ["E", "T", "M"]:
        return False
    else:
        return True
    
def validarMultiplayer(multiplayer: str) -> bool:
    multiplayer = multiplayer.lower
    
    if multiplayer == "s":
        return True
    elif multiplayer == "n":
        return False
    # En caso de que el valor sea invalido.
    else:
        return 0
        
    
def validarEditor(editor: str) -> bool:
    if editor == "" or editor == " ":
        return False
    else:
        return True

def validarPrecio(precio: int) -> bool:
    if precio < 0:
        return False
    else:
        return True
    
def validarStock(stock: int) -> bool:
    if stock <= 0:
        return True
    else:
        return False

def agregarJuego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario):
    juegos.append(codigo)
    juegos.append(titulo)
    juegos.append(plataforma)
    juegos.append(genero)
    juegos.append(clasificacion)
    juegos.append(multiplayer)
    juegos.append(editor)
    inventario.append(precio)
    inventario.append(stock)
    
def buscarCodigo():
    pass

def eliminarJuego(codigoEliminar, juegos, inventario) -> bool:
    juegoEliminar = input("Ingrese el codigo del juego que desea eliminar")
    juegoEliminar = juegoEliminar.lower
    codigoEliminar = buscarCodigo(juegoEliminar)
    codigoEliminar = codigoEliminar.lower
    
    
    if juegoEliminar == codigoEliminar:
        juegos.pop[juegoEliminar]
        inventario.pop[juegoEliminar]
        return True
    else:
        return False

# Programa principal
while True:
    menu()
    opcion = selectOpcion()
    
    match opcion:
        case 1:

            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            codigo = input("Ingrese el codigo del juego:")
            validarCodigo(codigo)
            if validarCodigo == False:
                print("Error. Codigo invalido.")
            else:
                continue
    
            titulo = input("Ingrese el titulo del juego: ")
            validarTitulo(titulo)
            if validarTitulo == False:
                print("Error. Titulo invalido")
            else:
                continue
    
            plataforma = input("Ingrese la plataforma del juego: ")
            validarPlataforma(plataforma)
            if validarPlataforma == False:
                print("Error. Plataforma invalida.")
            else:
                continue
    
            genero = input("Ingrese el genero del juego: ")
            validarGenero(genero)
            if validarGenero == False:
                print("Error. Genero invalido.")
            else:
                continue
    
            clasificacion = input("Ingrese la clasificación del juego [E, T o M]: ")
            validarClasificacion(clasificacion)
            if validarClasificacion == False:
                print("Error. Clasificación invalida.")
            else:
                continue
            
            multiplayer = input("El juego es multiplayer? [s o n]: ")
            validarMultiplayer(multiplayer)
            if validarMultiplayer == False:
                print("Error. Valor multiplayer invalido.")
            else:
                continue
            
            editor = input("Ingrese el nombre del editor: ")
            validarEditor(editor)
            if validarEditor == False:
                print("Error. Editor ingresado invalido.")
            else:
                continue
    
            precio = int(input("Ingrese el precio del juego: "))
            validarPrecio(precio)
            if validarPrecio == False:
                print("Error. Precio ingresado es invalido.")
            else:
                continue
            
            stockJuego = int(input("Ingrese el stock del juego: "))
            validarStock(stockJuego)
            if validarStock == False:
                print("Error. Stock ingresado es invalido.")
            else:
                continue
            
            agregarJuego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stockJuego)
            
        case 5:
            eliminarJuego()
            if eliminarJuego == True:
                print("Juego eliminado.")
            else:
                print("El codigo no existe.")
                
        case 6:
            print("Programa finalizado.")
            break
        case _:
            print("Ingrese una opción valida.")