def mayusculas():
    capletras=[]
    regletras=[]
    mayusculas='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    minusculas='abcdefghijklmnñopqrstuvwxyz'
    for x in mayusculas:
        capletras.append(x)
    for x in minusculas:
        regletras.append(x)
    palabra=input("Ingrese una palabra \n")
    nueva_palabra=[]
    for x in palabra:
        if x in capletras:
            nueva_palabra.append(x)
        elif x not in capletras and x not in regletras:
            nueva_palabra.append(x)
        else:
            conversion=regletras.index(x)
            if x:
                proc=capletras[conversion]
                nueva_palabra.append(proc)
    resultado=''.join(nueva_palabra)
    print(resultado)
    
mayusculas()