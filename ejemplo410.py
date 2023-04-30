def mayuscula():
    mayusletras=[]
    minusletras=[]
    mayusculas='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    minusculas='abcdefghijklmnñopqrstuvwxyz'
    for x in mayusculas:
        mayusletras.append(x)
    for x in minusculas:
        minusletras.append(x)
    
    palabra=input("Ingrese una palabra en minusculas\n")
    nueva_palabra=[]
    
    for x in palabra:
        
        if x not in mayusletras and x not in minusletras:
            nueva_palabra.append(x)
        else:
            conversion=minusletras.index(x)
            if x:
                conv=mayusletras[conversion]
                nueva_palabra.append(conv)
    resultado=''.join(nueva_palabra)
    print(resultado)

mayuscula()