ANCHO=40

def mostrar_menu():

    print("=" * ANCHO)
    print("CALCULADORA FINANCIERA".center(ANCHO))
    print("=" * ANCHO)
    print()
    print("1. Interés simple")
    print("2. Interés compuesto")
    print("3. Salir")

    opcion=int(input("Seleccione la opción que desea realizar: "))
    return opcion

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