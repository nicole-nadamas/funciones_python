def agregar_notas(lista):
    try:
        nota = 0
        while nota <= 0:
            nota = float(input("ingrese nota"))
        lista.append(nota)
        print(" la nota fue agregada con exito!")
    except:
        print("la nota debe ser un valor numerico decimal o entero")

        