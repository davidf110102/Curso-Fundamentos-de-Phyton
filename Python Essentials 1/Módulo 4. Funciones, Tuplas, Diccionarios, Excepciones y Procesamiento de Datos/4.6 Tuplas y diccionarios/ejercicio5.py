school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
        break   
    if name in school_class:
        school_class[name].append(score)
    else:
        school_class[name] = [score]
        
for name in sorted(school_class.keys()):
    adding = sum(school_class[name])
    counter = len(school_class[name])
    print(name, ":", adding / counter)
