def add(x,y):
    return x+y
def do_twice(func,x,y):
    return func(func(x,y),func(x,y))

a=5
b=10
print(do_twice(add,a,b))

import random
for i in range(5):
    value=random.randint(1,6)
    print(value)

from math import pi
print(pi)

def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))

celsius = int(input())

def conv(c):
    #your code goes here
    return (9/5)*c+32

fahrenheit = conv(celsius)
print(fahrenheit)
print("7" + 4)