n=int(input("cantidad de numeros: "))
for i in range(1,n+1):
    numero=int(input("Ingresar numero: "))
    factorial=1
    for j in range(1,numero+1):
        factorial=factorial*j
    print("El factorial del numero ",numero, " es ",factorial)