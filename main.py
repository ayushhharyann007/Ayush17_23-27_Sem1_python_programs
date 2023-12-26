import package_creation as mm
from importlib import reload
a=mm.Addition()
print("Addition")
x=int(input("enter a number"))
y=int(input("enter a number"))
a.add(x,y)

a=mm.Subtraction()
print("substractions")
z=int(input("enter a number"))
h=int(input("enter a number"))
a.sub(z,h)

a=mm.Multiplication()
print("substractions")
z=int(input("enter a number"))
h=int(input("enter a number"))
a.multi(z,h)


  