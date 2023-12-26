def calculate_lcm(num1, num2):
    # Find the greater number
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    
    while True:
        # Check if both numbers are divisible by the greater number
        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break
        greater += 1
    
    return lcm

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and display the LCM
lcm = calculate_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm}")
