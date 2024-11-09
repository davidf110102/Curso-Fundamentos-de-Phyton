# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3
print("Paso 3:", beatles)
for miembro in ["Stu Sutcliffe", "Pete Best"]:
    nuevo_miembro = input(f"Agrega a {miembro}: ")
    beatles.append(nuevo_miembro)
    
# paso 4
del beatles[-1]
del beatles[-1]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))

