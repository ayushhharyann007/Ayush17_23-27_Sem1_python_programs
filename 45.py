
# Initialize an empty library inventory
library_inventory = {}

# Main menu loop
while True:
    print("\nLibrary Inventory Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Display Inventory")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add Book
    if choice == "1":
        book_title = input("Enter the title of the book: ")
        book_quantity = int(input("Enter the quantity of the book: "))

        # Check if the book is already in the inventory
        if book_title in library_inventory:
            library_inventory[book_title] += book_quantity
        else:
            library_inventory[book_title] = book_quantity

        print(f"{book_quantity} copies of {book_title} added to the inventory.")

    # Remove Book
    elif choice == "2":
        book_title = input("Enter the title of the book you want to remove: ")

        # Check if the book is in the inventory
        if book_title in library_inventory:
            quantity_to_remove = int(input(f"Enter the quantity of {book_title} to remove: "))
            if quantity_to_remove <= library_inventory[book_title]:
                library_inventory[book_title] -= quantity_to_remove
                print(f"{quantity_to_remove} copies of {book_title} removed from the inventory.")
                if library_inventory[book_title] == 0:
                    del library_inventory[book_title]
            else:
                print(f"Error: Not enough copies of {book_title} in the inventory.")
        else:
            print(f"Error: {book_title} is not in the inventory.")

    # Display Inventory
    elif choice == "3":
        if not library_inventory:
            print("The inventory is empty.")
        else:
            print("\nLibrary Inventory:")
            for title, quantity in library_inventory.items():
                print(f"{title}: {quantity} copies")

    # Exit
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")