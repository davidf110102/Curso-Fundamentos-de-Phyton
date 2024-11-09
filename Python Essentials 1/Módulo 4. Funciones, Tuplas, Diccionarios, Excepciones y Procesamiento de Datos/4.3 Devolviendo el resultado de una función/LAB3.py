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

def dia_del_año(año, mes, dia):
    if mes < 1 or mes > 12 or dia < 1:
        return None
    dias_mes = dias_en_mes(año, mes)
    if dias_mes is None or dia > dias_mes:
        return None
    total_dias = sum(dias_en_mes(año, m) for m in range(1, mes)) + dia
    return total_dias

print(dia_del_año(2000, 12, 31))
print(dia_del_año(2001, 12, 31))
print(dia_del_año(2020, 2, 29))
print(dia_del_año(2023, 3, 1))
print(dia_del_año(2024, 1, 1))
print(dia_del_año(2024, 13, 1))
print(dia_del_año(2024, 2, 30))

