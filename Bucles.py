i=1
while i<6:
    print(i)
    if i ==3:
        break;
    i+=1

i=0
while i< 6:
    i+=1
    if i ==3:
        continue
    print(i)

frutas=["manzana","platano","cherry"]
for x in frutas:
    print(x)
    if x == "platano":
        break

for x in "banana":
    print(x)

for x in range(6):
    print(x)
i=2
for x in range(3*i,0,-1):
    print(x)

for x in range(6):
    print(x)
else:
    print("Final")

for x in range(6):
    if x==1:break
    print(x)
else:
    print("Fial")

