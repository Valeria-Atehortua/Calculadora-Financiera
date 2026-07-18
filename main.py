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

def interes_simple():
    print("Elegiste interés simple")

    capital = float(input("Ingrese el capital inicial: "))
    tasa_interes = float(input("Ingrese el porcentaje de la tasa de interés: "))
    tiempo = float(input("Ingrese el tiempo en años: "))

    print("=" * ANCHO)
    print("DATOS INGRESADOS".center(ANCHO))
    print("=" * ANCHO)
    
    print(f"Capital: ${capital:,.2f}")
    print(f"Tasa: {tasa_interes:,.2f}%")
    print(f"Tiempo: {tiempo} años")

    tasa_interes /= 100
    interes = capital * tasa_interes * tiempo
    monto_final = capital + interes

    print("=" * ANCHO)
    print("RESULTADOS".center(ANCHO))
    print("=" * ANCHO)
    print(f"\nCapital inicial: ${capital:,.2f}")
    print(f"Interés generado: ${interes:,.2f}")
    print(f"Monto final: ${monto_final:,.2f}")
    
    input("\nPresione Enter para volver al menú...")

def interes_compuesto():
    print("Elegiste interés compuesto")

    capital = float(input("Ingrese el capital inicial: "))
    tasa_interes = float(input("Ingrese el porcentaje de la tasa de interés: "))
    tiempo = float(input("Ingrese el tiempo en años: "))

    print("=" * ANCHO)
    print("DATOS INGRESADOS".center(ANCHO))
    print("=" * ANCHO)
    
    print(f"Capital: ${capital:,.2f}")
    print(f"Tasa: {tasa_interes:,.2f}%")
    print(f"Tiempo: {tiempo} años")

    tasa_interes /= 100
    monto_final = capital * (1 + tasa_interes) ** tiempo
    interes = monto_final - capital

    print("=" * ANCHO)
    print("RESULTADOS".center(ANCHO))
    print("=" * ANCHO)
    print(f"\nCapital inicial: ${capital:,.2f}")
    print(f"Interés generado: ${interes:,.2f}")
    print(f"Monto final: ${monto_final:,.2f}")
    
    input("\nPresione Enter para volver al menú...")

def main():
    while True:
        opcion=mostrar_menu()
        if opcion == 1:
            interes_simple()
        elif opcion==2:
            interes_compuesto()
        elif opcion==3:
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. ")

if __name__ == "__main__":
    main()