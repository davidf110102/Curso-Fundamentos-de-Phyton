def es_año_bisiesto(año):
    if año % 4 != 0:
        return False
    elif año % 100 != 0:
        return True
    elif año % 400 != 0:
        return False
    else:
        return True

datos_prueba = [1900, 2000, 2016, 1987]
resultados_prueba = [False, True, True, False]

for i in range(len(datos_prueba)):
    año = datos_prueba[i]
    print(año, "-> ", end="")
    resultado = es_año_bisiesto(año)
    if resultado == resultados_prueba[i]:
        print("OK")
    else:
        print("Fallido")
