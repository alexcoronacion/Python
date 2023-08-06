""" numero=int(input("Ingrese numero: "))
maximo=numero
for n in range(2,11):
    numero=int(input("ingrese numero: "))
    if numero>maximo:
        maximo=numero
print("Maximo: ",maximo) """

""" for i in range(1,10):
    print("Tabla del ",i)
    for j in range(1,11):
        producto=i*j
        printt(i,"por",j,"=",producto) """
        
""" 
numero=int(input("Ingresar numero: "))
maximo=numero
for n in range(2,11):
    numero=int(input("Ingresar numero: "))
    if numero>maximo:
        maximo=numero
print("Maximo: ",maximo)

 """
""" 
suma=0
cant=0
numero=int(input("Ingrese numero: "))

while numero>0:
    numero=int(input("Ingrese numero: "))
    cant=cant+1
    suma=suma+numero
print
media=suma/cant
print("La media de los ",cant," es: ",media)
  """
""" 
año=1980
if año%4!=0:
    print("No es bisiesto")
elif año%4==0 and año%100!=0:
    print("Es bisiesto")
elif año%4==0 and año%100==0 and año%400!=0:
    print("No es bisiesto")
elif año%4==0 and año%100==0 and año%400==0:
    print("Es bisiesto")

"""  """
año=int(input("ingrese numero:"))
if not año%4:
    if not año%100:
        if not año%400:
            print("Es bisiesto")
        else:
            print("No es bisiesto")
    else:
        print("Es bisiesto")
else:
    print("No es bisiesto")
            
 """
""" 
def es_bisiesto(año):
    return not año%4 and (año%100 or not año%400)
 """
""" for año in range(2023,2073):
    if es_bisiesto(año):
        print(año,end=' ')
 """"""  """

    