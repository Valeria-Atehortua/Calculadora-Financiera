ANCHO=40

def mostrar_menu(titulo, opciones):
    while True:
        print("=" * ANCHO)
        print(titulo.center(ANCHO))
        print("=" * ANCHO)
        print()
        for numero, opcion in enumerate(opciones):
            print(f"{numero + 1}. {opcion}")
        opcion = int(input("\nSeleccione la opción que desea realizar: "))
        if opcion < 1 or opcion > len(opciones):
            print("La opción no es valida.\n")
        else:
            return opcion

def mostrar_menu_tipo_interes():
    while True:
        print("=" * ANCHO)
        print("TIPO DE INTERÉS".center(ANCHO))
        print("=" * ANCHO)
        print()
        print("1. Interés simple")
        print("2. Interés compuesto")
        tipo = int(input("Ingrese la opción deseada: "))
        if tipo != 1 and tipo != 2:
            print("La opción no es valida.")
        else:
            return tipo

def mostrar_datos(capital, tasa_interes, tiempo):

    print("=" * ANCHO)
    print("DATOS INGRESADOS".center(ANCHO))
    print("=" * ANCHO)
    
    print(f"Capital: ${capital:,.2f}")
    print(f"Tasa: {tasa_interes:,.2f}%")
    print(f"Tiempo: {tiempo} años")

def mostrar_resultados(resultados):

    print("=" * ANCHO)
    print("RESULTADOS".center(ANCHO))
    print("=" * ANCHO)
    for etiqueta, valor in resultados.items():
        if isinstance(valor, (int, float)):
            print(f"{etiqueta}: {valor:,.2f}")
        else:
            print(f"{etiqueta}: ${valor}")
    
    input("\nPresione Enter para volver al menú...")