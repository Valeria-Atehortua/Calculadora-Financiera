from interfaz import mostrar_menu, mostrar_datos, mostrar_resultados
from utilidades import solicitar_datos
from calculos import interes_simple, interes_compuesto

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            interes_simple()
        elif opcion == 2:
            interes_compuesto()
        elif opcion == 3:
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. ")

if __name__ == "__main__":
    main()