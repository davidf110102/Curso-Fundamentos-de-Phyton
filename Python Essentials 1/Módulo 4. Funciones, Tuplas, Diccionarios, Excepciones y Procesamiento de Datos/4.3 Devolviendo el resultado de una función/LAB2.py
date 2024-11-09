def es_año_bisiesto(año):
    if año % 4 != 0:
        return False
    elif año % 100 != 0:
        return True
    elif año % 400 != 0:
        return False
    else:
        return True

def dias_en_mes(año, mes):
    if mes < 1 or mes > 12:
        return None
    
    dias_por_mes = [31, 29 if es_año_bisiesto(año) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return dias_por_mes[mes - 1]

años_prueba = [1900, 2000, 2016, 1987]
meses_prueba = [2, 2, 1, 11]
resultados_prueba = [28, 29, 31, 30]

for i in range(len(años_prueba)):
    año = años_prueba[i]
    mes = meses_prueba[i]
    print(año, mes, "->", end="")
    resultado = dias_en_mes(año, mes)
    if resultado == resultados_prueba[i]:
        print("OK")
    else:
        print("Fallido")

