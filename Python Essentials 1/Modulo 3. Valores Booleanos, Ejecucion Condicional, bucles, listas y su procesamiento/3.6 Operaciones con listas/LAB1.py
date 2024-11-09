lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista2 = []
#
for numero in lista:
    if numero not in lista2:
        lista2.append(numero)
    
    
#
print("La lista con elementos únicos:")
print(lista2)

