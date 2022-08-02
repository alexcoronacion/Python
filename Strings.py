a="Hello, World!"
print(a[1])

for x in "banana":
    print(x)
print(len(a))

txt="the best things in life are free!"
print("free" in txt)

txt="the best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

b="Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b.upper())
print(b.lower())

a=" Hello, World! "
print(a.strip())

print(a.split(","))

age=36
txt="My name is John, and I am {}"
print(txt.format(age))

quantity=3
itemno=537
price=49.95
myorder="I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,itemno,price))

myorder="I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity,itemno,price))

thislist=["apple","banana","cherry"]
print(thislist)

print(len(thislist))

print(thislist)
thislist.append("orange")
print(thislist)
thislist.insert(1,"kiwi")

for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1

