a=float(input("Ingrese lado a:"))
b=float(input("Ingrese lado b:"))
c=float(input("Ingrese lado c:"))

p=(a+b+c)/2
area=(p*(p-a)*(p-b)*(p-c))**0.5
if (p>a) and (p>b) and (p>c):
    print(area)
else:
    print("Error de culo")

    
