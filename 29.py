# star printing 

def print_hollow_triangle(height):
    for i in range(height):
        for j in range(height * 2 - 1):
            if i == height - 1 or i + j == height - 1 or j - i == height - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

if __name__ == "__main__":
    triangle_height = int(input("Enter the height of the hollow triangle: "))
    print_hollow_triangle(triangle_height)
