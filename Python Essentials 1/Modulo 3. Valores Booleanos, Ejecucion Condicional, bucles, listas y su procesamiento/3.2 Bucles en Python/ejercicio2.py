
largest_number = -999999999

number = int(input("Introduce un número o escribe -1 para detener: "))

while number != -1:
    if number > largest_number:
        largest_number = number
    number = int(input("Introduce un número o escribe -1 para detener: "))

print("El número más grande es:", largest_number)

