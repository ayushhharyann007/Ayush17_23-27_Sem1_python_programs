def floordivision(x,y):
    return x // y

def exponent (x , y):
    return x**y

    print("1. floordivision")
    print("2. exponent")

    choice = input("Enter choice (1/2): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
     
    if choice in ("1", "2"):
     if choice == "1":
        result = floordivision(num1, num2)
        operation = "//"
     elif choice == "2":
        result = exponent(num1, num2)
        operation = "**"   

        print(f"\nResult: {num1} {operation} {num2} = {result}")

