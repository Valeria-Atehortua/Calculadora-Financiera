from interfaz import mostrar_datos, mostrar_resultados, mostrar_menu_tipo_interes
from utilidades import solicitar_datos
ANCHO = 40
def calcular_interes_simple(capital, tasa_interes, tiempo):

    tasa_interes /= 100
    interes = capital * tasa_interes * tiempo
    monto_final = capital + interes

    return interes, monto_final

def calcular_interes_compuesto(capital, tasa_interes, tiempo):
    tasa_interes /= 100
    monto_final = capital * (1 + tasa_interes) ** tiempo
    interes = monto_final - capital

    return interes, monto_final

def interes_simple():
    print("Elegiste interés simple")

    valor_principal, tasa_interes, tiempo = solicitar_datos("Capital inicial")
    mostrar_datos(valor_principal, tasa_interes, tiempo)
    interes, monto_final = calcular_interes_simple(
        valor_principal,
        tasa_interes,
        tiempo
        )
    resultados = {
            "Capital inicial": valor_principal,
            "Interés generado": interes,
            "Monto final": monto_final
        }
    
    mostrar_resultados(resultados)

def interes_compuesto():
    print("Elegiste interés compuesto")

    valor_principal, tasa_interes, tiempo = solicitar_datos("Capital inicial")
    mostrar_datos(valor_principal, tasa_interes, tiempo)
    interes, monto_final = calcular_interes_compuesto(
        valor_principal,
        tasa_interes,
        tiempo
        )
    resultados = {
            "Capital inicial": valor_principal,
            "Interés generado": tasa_interes,
            "Monto final": monto_final
            }
    
    mostrar_resultados(resultados)

def obtener_monto_final():
    tipo = mostrar_menu_tipo_interes()
    capital, tasa_interes, tiempo = solicitar_datos()
    if tipo == 1:
        _, monto_final = calcular_interes_simple(capital, tasa_interes, tiempo)
    else: 
        _, monto_final = calcular_interes_compuesto(capital, tasa_interes, tiempo)
    return monto_final

def comparar_inversiones():
    print("=" * ANCHO)
    print("INVERSIÓN 1".center(ANCHO))
    print("=" * ANCHO)

    monto_final1 = obtener_monto_final()

    print()

    print("=" * ANCHO)
    print("INVERSIÓN 2".center(ANCHO))
    print("=" * ANCHO)

    monto_final2 = obtener_monto_final()
    diferencia = abs(monto_final1 - monto_final2)

    if monto_final1 > monto_final2:
        print("La inversión 1 genera un monto final mayor.")
    elif monto_final1 < monto_final2: 
        print("La inversión 2 genera un monto final mayor.")
    else:
        print("Las dos inversiones generan el mismo monto final.")
    print(f"Diferencia: ${diferencia:,.2f}")

def valor_futuro():
    print("Elegiste valor futuro")
    
    valor_principal, tasa_interes, tiempo = solicitar_datos("Capital inicial")
    mostrar_datos(valor_principal, tasa_interes, tiempo)
    _, monto_final = calcular_interes_compuesto(
        valor_principal,
        tasa_interes,
        tiempo
        )
    resultados = {
            "Capital invertido": valor_principal,
            "Valor futuro": monto_final
            }
    
    mostrar_resultados(resultados)

def calcular_valor_presente(valor_futuro, tasa_interes, tiempo):
    tasa_interes /= 100
    valor_presente = valor_futuro / (1 + tasa_interes) ** tiempo 

    return valor_presente

def valor_presente():
    print("Elegiste valor presente")
        
    valor_principal, tasa_interes, tiempo = solicitar_datos("Valor futuro deseado")
    mostrar_datos("Valor futuro deseado", valor_principal, tasa_interes, tiempo)
    valor_futuro = valor_principal
    valor_presente = calcular_valor_presente(
        valor_futuro,
        tasa_interes,
        tiempo
        )
    resultados = {
            "Valor futuro": valor_futuro,
            "Valor presente": valor_presente
            }
    
    mostrar_resultados(resultados)