fruits=["apple","banana","cherry"]

for x in fruits:
    print(x)
    if x=="banana":
        break

for x in fruits:
    if x=="banana":
        break
    print(x)

for x in fruits:
    if x=="banana":
        continue
    print(x)


for x in range(6):
    print(x)

for y in range(2,6):
    print(y)

for x in range(2,30,3):
    print(x)

for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x==3:break
    print(x)
else:
    print("Finally finished!")

adj=["red","big","tasty"]
fruits=["apple","banana","cherry"]

for x in adj:
    for y in fruits:
        print(x,y)

def my_function():
    print("Hello from a function")
my_function()

def my_name(fname):
    print(fname+ " Refsnes")

x=input("Ingrese su nombre: ")
my_name(x)

def my_funtion(*kids):
    print("La niña mas pequeña es "+kids[0])

my_funtion("Emil","Tobias","Linus")

def my_function02(child3,child2,child1):
    print("La niña mas pequeña es "+child3)

my_function02(child1="Emil",child2="Tobias",child3="Linus")


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")