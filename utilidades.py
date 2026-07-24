def solicitar_datos(nombre_principal):

    valor_principal = float(input(f"Ingrese el {nombre_principal}: "))
    tasa_interes = float(input("Ingrese el porcentaje de la tasa de interés: "))
    tiempo = float(input("Ingrese el tiempo en años: "))

    return valor_principal, tasa_interes, tiempo