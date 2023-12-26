print("   *   ")
print("  * *  ")
print(" *   * ")
print("*******")
print("*     *")
print("*     *")
rows = 7
cols = 5

pattern = [
    " *** ",
    "*    ",
    "*    ",
    " *** ",
    "    *",
    "    *",
    " *** "
]

for row in pattern:
    print(row)

size = 5

for i in range(size):
    for j in range(size):
        if j == size // 2 or i == size // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


for i in range(5):
    for j in range(5):
        if j == 2 or i == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

size = 5  # You can adjust the size as needed

for i in range(size):
    for j in range(size):
        if i == size // 2 or j == size // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Define the pattern for the letter "N"
pattern = [
    "*    *",
    "**   *",
    "* *  *",
    "*  * *",
    "*   **",
    "*    *"
]

# Print the pattern
for line in pattern:
    print(line)
