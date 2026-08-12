from interfaz import mostrar_datos, mostrar_resultados, mostrar_menu_tipo_interes, mostrar_tabla_amortizacion
from utilidades import solicitar_datos
ANCHO = 40
MESES_ANUALES = 12
PORCENTAJE = 100
def calcular_interes_simple(capital, tasa_interes, tiempo):

    tasa_interes /= PORCENTAJE
    interes = capital * tasa_interes * tiempo
    monto_final = capital + interes

    return interes, monto_final

def calcular_interes_compuesto(capital, tasa_interes, tiempo):
    tasa_interes /= PORCENTAJE
    monto_final = capital * (1 + tasa_interes) ** tiempo
    interes = monto_final - capital

    return interes, monto_final

def interes_simple():
    print("Elegiste interés simple")

    valor_principal, tasa_interes, tiempo = solicitar_datos("Capital inicial")
    mostrar_datos("Capital inicial", valor_principal, tasa_interes, tiempo)
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
    mostrar_datos("Capital inicial", valor_principal, tasa_interes, tiempo)
    interes, monto_final = calcular_interes_compuesto(
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

def obtener_monto_final():
    tipo = mostrar_menu_tipo_interes()
    capital, tasa_interes, tiempo = solicitar_datos("Capital inicial")
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
    mostrar_datos("Capital inicial", valor_principal, tasa_interes, tiempo)
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
    tasa_interes /= PORCENTAJE
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

def calcular_amortizacion_frances(monto, tasa, tiempo):
    tabla = []
    tasa /= PORCENTAJE

    tasa_mensual = tasa / MESES_ANUALES
    numero_cuotas = int(tiempo * MESES_ANUALES)

    if tasa_mensual == 0:
        cuota = monto / numero_cuotas
    else:
        factor = (1 + tasa_mensual) ** numero_cuotas

        cuota = monto * (
            tasa_mensual * factor
        ) / (
            factor - 1
        )

    saldo = monto

    total_pagado = 0
    total_intereses = 0
    for numero_cuota in range(1, numero_cuotas + 1):
        interes = saldo * tasa_mensual
        abono_capital = cuota - interes
        saldo -= abono_capital

        cuota_actual = {
            "Número de cuota": numero_cuota,
            "Pago": cuota,
            "Interés": interes,
            "Abono a capital": abono_capital,
            "Saldo": saldo
        }
        tabla.append(cuota_actual)
        total_pagado += cuota
        total_intereses += interes
    return tabla, total_pagado, total_intereses

def amortizacion_frances():
    print("Elegiste amortización francesa")
    monto_prestamo, tasa_interes, tiempo = solicitar_datos("Monto del préstamo")
    mostrar_datos("Monto del préstamo", monto_prestamo, tasa_interes, tiempo)

    tabla, total_pagado, total_intereses = calcular_amortizacion_frances(
    monto_prestamo,
    tasa_interes,
    tiempo
    )
    mostrar_tabla_amortizacion(tabla)
    
    resultados = {
    "Total pagado": total_pagado,
    "Total intereses": total_intereses
    }
    mostrar_resultados(resultados)

