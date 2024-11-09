palabra_secreta="chupacabra"
palabra = input("Ingresa una palabra: ")
while palabra != palabra_secreta:
    palabra = input("Ingresa una palabra: ")
    if palabra == palabra_secreta:
        break
print("Has dejado el bucle con éxito.")
    