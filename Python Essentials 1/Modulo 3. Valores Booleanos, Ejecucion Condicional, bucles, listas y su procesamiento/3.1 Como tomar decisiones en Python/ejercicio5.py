numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

numero_largo=numero1

if numero2 > numero1:
    numero_largo=numero2
if numero3 > numero2:
    numero_largo=numero3

print("El número más grande es:", numero_largo)