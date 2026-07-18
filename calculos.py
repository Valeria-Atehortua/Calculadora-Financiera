from interfaz import mostrar_datos, mostrar_resultados
from utilidades import solicitar_datos

def interes_simple():
    print("Elegiste interés simple")

    capital, tasa_interes, tiempo = solicitar_datos()
    mostrar_datos(capital, tasa_interes, tiempo)

    tasa_interes /= 100
    interes = capital * tasa_interes * tiempo
    monto_final = capital + interes

    mostrar_resultados(capital, interes, monto_final)

def interes_compuesto():
    print("Elegiste interés compuesto")

    capital, tasa_interes, tiempo= solicitar_datos()
    mostrar_datos(capital, tasa_interes, tiempo)

    tasa_interes /= 100
    monto_final = capital * (1 + tasa_interes) ** tiempo
    interes = monto_final - capital

    mostrar_resultados(capital, interes, monto_final)