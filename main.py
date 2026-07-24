from interfaz import mostrar_menu, mostrar_datos, mostrar_resultados
from utilidades import solicitar_datos
from calculos import interes_simple, interes_compuesto, comparar_inversiones, valor_futuro
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
    "Valor futuro" 
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
            interes_simple()
        elif opcion_principal == 2:
            interes_compuesto()
        elif opcion_principal == 3:
            comparar_inversiones()
        elif opcion_principal == 4:
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. ")
if __name__ == "__main__":
    main()