from interfaz import mostrar_menu
from calculos import interes_simple, interes_compuesto, comparar_inversiones, valor_futuro, amortizacion_frances
opciones_principal=[
    "Inversiones",
    "Préstamos",
    "Historial",
    "Salir"
    ]

opciones_inversiones=[
    "Interés simple", 
    "Interés compuesto", 
    "Comparar inversiones",
    "Valor futuro", 
    "Salir"
    ]

opciones_prestamos=[
    "Amortización francesa",
    "Salir"
    ]

def main():
    while True:
        opcion_principal = mostrar_menu("CALCULADORA FINANCIERA", opciones_principal)
        
        if opcion_principal == 1:
            while True:
                opcion_inversiones = mostrar_menu("INVERSIONES", opciones_inversiones)
                if opcion_inversiones == 1:
                    interes_simple()
                elif opcion_inversiones == 2:
                    interes_compuesto()
                elif opcion_inversiones == 3:
                    comparar_inversiones()
                elif opcion_inversiones == 4:
                    valor_futuro()
                elif opcion_inversiones == 5:
                    break


        if opcion_principal == 2:
            while True:
                opcion_prestamos = mostrar_menu("PRÉSTAMOS", opciones_prestamos)
                if opcion_prestamos == 1:
                    amortizacion_frances()
                elif opcion_prestamos == 2:
                    break
        elif opcion_principal == 3:
            interes_compuesto()
        elif opcion_principal == 4:
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. ")
if __name__ == "__main__":
    main()