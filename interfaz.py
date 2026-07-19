ANCHO=40

def mostrar_menu():

    print("=" * ANCHO)
    print("CALCULADORA FINANCIERA".center(ANCHO))
    print("=" * ANCHO)
    print()
    print("1. Interés simple")
    print("2. Interés compuesto")
    print("3. Comparar inversiones")
    print("4. Salir")

    opcion=int(input("Seleccione la opción que desea realizar: "))
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

def mostrar_resultados(capital, interes, monto_final):

    print("=" * ANCHO)
    print("RESULTADOS".center(ANCHO))
    print("=" * ANCHO)
    print(f"\nCapital inicial: ${capital:,.2f}")
    print(f"Interés generado: ${interes:,.2f}")
    print(f"Monto final: ${monto_final:,.2f}")
    
    input("\nPresione Enter para volver al menú...")