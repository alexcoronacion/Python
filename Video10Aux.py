
n=int(input("Ingrese la cantidad de numeros: "))

for i in range(1,(n+1)):
    numero=int(input("\nIngrese Numero: "))
    factorial=1
    for j in range(1,(numero+1)):
        factorial=factorial*j
    print("\nEl factorial del numero ",numero," es : ",factorial)
                        