# lcm of two number 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


if a>b:
    greater= a
else:
    greater = b

while True:
   
    if greater % a == 0 and greater % b == 0:
        lcm = greater
        break
    greater += 1


print(f"The LCM of {a} and {b} is: {lcm}")
   
