#single inheritance 
# class Parent:
#     def add(self,x,y):
#         return x+y
    
# class Child(Parent):
#     def getdata(self):
#       self.x=int(input("enter the value of x"))
#       self.y=int(input("enter the value of y"))
     
# obj1 = Child()
# obj1.getdata()
# result = obj1.add(obj1.x, obj1.y)
# print("Sum of the values:", result)  





# class Area:
#     def add(self,a,):
#         return a**2
    
# class Square(Area):
#     def getdata(self):
#       self.a=int(input("enter the side a"))
      
     
# obj1 = Square()
# obj1.getdata()
# result = obj1.add(obj1.a)
# print("Area of the square:", result)       


# class Area:
#     def add(self,a,b):
#         return a*b
    
# class Rectangle(Area):
#     def getdata(self):
#       self.a=int(input("enter the side a"))
#       self.b=int(input("enter the side b"))
     
# obj1 = Rectangle()
# obj1.getdata()
# result = obj1.add(obj1.a,obj1.b)
# print("Area of the Rectangle:", result)






# class Area:
#     def add(self,a,b):
#         return 0.5*a*b
    
# class Triangle(Area):
#     def getdata(self):
#       self.a=int(input("enter the side a"))
#       self.b=int(input("enter the side b"))
     
# obj1 = Triangle()
# obj1.getdata()
# result = obj1.add(obj1.a,obj1.b)
# print("Area of the triangle:", result)

       
       
# class AreaCalculator:
#     def _init_(self):
#         self.length = 0
#         self.width = 0

#     def get_user_input(self):
#         self.length = int(input("Enter the length: "))
#         self.width = int(input("Enter the width : "))

#     def calculate_square_area(self):
#         return self.length * self.length

#     def calculate_rectangle_area(self):
#         return self.length * self.width

#     def display_results(self, shape):
#         if shape == "square":
#             area = self.calculate_square_area()
#         elif shape == "rectangle":
#             area = self.calculate_rectangle_area()
#         else:
#             print("Invalid shape specified")

#         print(f"Area of {shape} is: {area}")

# calculator = AreaCalculator()

# shape_choice = input("Enter the shape (square/rectangle): ").lower()
# calculator.get_user_input()

# if shape_choice == "square":
#     calculator.display_results("square")
# elif shape_choice == "rectangle":
#     calculator.display_results("rectangle")
# else:
#     print("Invalid shape specified. Please enter 'square' or 'rectangle'.")
    
    
    
    
    
    
    
    
    

# class LetsUpgrade:
#     def __init__(self):
#         self.subjects = {1: 'C', 2: 'JAVA', 3: 'C++', 4: 'Python'}
#         self.trainer = 'Ayush Aryan'
#         self.duration = {1: 1, 2: 1, 3: 0.5, 4: 0.5}

# class ITM:
#     def __init__(self):
#         self.subjects = {1: 'B TECH', 2: 'Hotel Management', 3: 'R AND D', 4: 'Fashion and Design'}
#         self.trainer = 'Sahil Sable'
#         self.duration = {1: 3, 2: 3, 3: 3, 4: 3}

# class Child(LetsUpgrade, ITM):
#     def __init__(self):
#         super().__init__()

#     def get_subject_details(self, choice):
#         if choice in self.subjects:
#             print(f"Subject: {self.subjects[choice]}")
#             print(f"Trainer: {self.trainer}")
#             print(f"Duration: {self.duration[choice]} months")
#         else:
#             print("Invalid choice")

# def main():
#     child_obj = Child()

#     print("\nChoose a subject:")
#     print("1. C\n2. JAVA\n3. C++\n4. Python\n"
#           "5. B TECH\n6. Hotel Management\n7. R AND D\n8. Fashion and Design\n"
#           "9. Exit")

#     choice = int(input("Enter your choice (1-9): "))

#     if choice == 9:
#         print("Exiting program.")
#     else:
#         child_obj.get_subject_details(choice)

# if __name__ == "__main__":
#     main()
     



#Multi-Level Inheritance
# class Grandfather:
#     def __init__(self, assets):
#         self.assets = assets

#     def display_info(self):
#         print(f"Grandfather's assets: ${self.assets}")


# class Father(Grandfather):
#     def __init__(self, assets, business):
#         Grandfather.__init__(self, assets)
#         self.business = business

#     def display_info(self):
#         Grandfather.display_info(self)
#         print(f"Father's business: {self.business}")


# class Child(Father):
#     def __init__(self, assets, business, education):
#         Father.__init__(self, assets, business)
#         self.education = education

#     def display_info(self):
#         Father.display_info(self)
#         print(f"Child's education: {self.education}")


# grandfather_assets = 1000
# father_assets = 5000
# business_info = "Family Business Inc."
# child_education = "College Graduate"

# # Creating instances
# grandfather = Grandfather(assets=grandfather_assets)
# father = Father(assets=father_assets, business=business_info)
# child = Child(assets=None, business=None, education=None)

# # Calculating and setting the child's assets
# child.assets = grandfather.assets + father.assets

# # Displaying information
# grandfather.display_info()
# print("\n")
# father.display_info()
# print("\n")
# child.display_info()




#Multi-Level Inheritance

# #CHAT GPT Code ⬇️
# class Grandfather:
#     def __init__(self, assets):
#         self.assets = assets

#     def display_grandfather_assets(self):
#         print("Grandfather's Assets: ₹", self.assets)

# class Father(Grandfather):
#     def __init__(self, assets, income):
#         super().__init__(assets)
#         self.income = income

#     def display_father_income(self):
#         print("Father's Income: ₹", self.income)

# class Son(Father):
#     def __init__(self, assets, income, pocket_money):
#         super().__init__(assets, income)
#         self.pocket_money = pocket_money

#     def display_son_pocket_money(self):
#         print("Son's Pocket Money: ₹", self.pocket_money)


# grandfather = Grandfather(1000000)
# father = Father(500000, 75000)
# son = Son(200000, 30000, 5000)

# grandfather.display_grandfather_assets()
# father.display_father_income()
# son.display_son_pocket_money()




#vrishank code ⬇️
# class Grandfather:
#     def __init__(self, assets):
#         self.assets = assets

# class Father(Grandfather):
#     def __init__(self, assets, business):
#         super().__init__(assets)
#         self.business = business

# class Child(Father):
#     def __init__(self, assets, business, education):
#         super().__init__(assets, business)
#         self.education = education

# grandfather_assets = 1000
# father_assets = 5000
# business_info = "Family Business"
# child_education = "Computer Science Engineer"
# #instance
# grandfather = Grandfather(assets=grandfather_assets)
# father = Father(assets=father_assets, business=business_info)
# child = Child(assets=None, business=None, education=None)

# child.assets = grandfather.assets + father.assets
# child.business = father.business
# child.education = child_education

# print(f"\nGrandfather's assets: ₹{grandfather.assets}")
# print(f"Father's assets: ₹{father.assets}")
# print(f"Child's assets: ₹{child.assets}")
# print(f"\nChild's business: {child.business}")
# print(f"\nChild's education: {child.education}\n")





# class GrandFather:
#     def __init__(self):
#         self.name = " GrandFather"
#         self._assets = 1500000

# class Father(GrandFather):
#     def __init__(self):
#         super().__init__()
#         self.name = self.name + " Father"
#         self._inharitedAssets = self._assets 
#         self._purchasedAssets = 200000
#         self._totalAssets = self._inharitedAssets + self._purchasedAssets

# class Child(Father):
#     def __init__(self, name, assets):
#         super().__init__()
#         self.name = self.name + " " + name
#         self.__inharitedAssets = self._totalAssets
#         self.__purchasedAssets = assets
#         self._totalAssets = self.__inharitedAssets + self.__purchasedAssets
    
#     def displayData(self):
#         print("Name: ", self.name)
#         print("Assets: ", self._totalAssets)

# obj = Child("Child",100000)
# obj.displayData()





##1. Design a library catalogue system using inheritance. take base class library item and derieved classes book, dvd and journal.
# each derived class should have unique attributes and methohds and system should support checking in nd checking out System.

# class LibraryItem:
#     def __init__(self, title, item_id):
#         self.title = title
#         self.item_id = item_id
#         self.checked_out = False

#     def display_info(self):
#         print(f"Title: {self.title}")
#         print(f"Item ID: {self.item_id}")
#         print(f"Status: {'Checked Out' if self.checked_out else 'Available'}")

#     def check_out(self):
#         if not self.checked_out:
#             print(f"{self.title} has been checked out.")
#             self.checked_out = True
#         else:
#             print(f"{self.title} is already checked out.")

#     def check_in(self):
#         if self.checked_out:
#             print(f"{self.title} has been checked in.")
#             self.checked_out = False
#         else:
#             print(f"{self.title} is already checked in.")


# class Book(LibraryItem):
#     def __init__(self, title, item_id, author):
#         super().__init__(title, item_id)
#         self.author = author

#     def display_info(self):
#         super().display_info()
#         print(f"Author: {self.author}")


# class DVD(LibraryItem):
#     def __init__(self, title, item_id, director):
#         super().__init__(title, item_id)
#         self.director = director

#     def display_info(self):
#         super().display_info()
#         print(f"Director: {self.director}")


# class Journal(LibraryItem):
#     def __init__(self, title, item_id, publisher):
#         super().__init__(title, item_id)
#         self.publisher = publisher

#     def display_info(self):
#         super().display_info()
#         print(f"Publisher: {self.publisher}")


# def main():
#     # Example usage
#     book1 = Book("The Python Programming Language", "B001", "Guido van Rossum")
#     dvd1 = DVD("Inception", "D001", "Christopher Nolan")
#     journal1 = Journal("Scientific American", "J001", "Springer")

#     library_items = [book1, dvd1, journal1]

#     while True:
#         print("\nLibrary Catalog System:")
#         print("1. Display Information")
#         print("2. Check Out Item")
#         print("3. Check In Item")
#         print("4. Exit")

#         choice = input("Enter your choice (1-4): ")

#         if choice == "1":
#             for item in library_items:
#                 item.display_info()
#         elif choice == "2":
#             item_id = input("Enter the item ID to check out: ")
#             for item in library_items:
#                 if item.item_id == item_id:
#                     item.check_out()
#         elif choice == "3":
#             item_id = input("Enter the item ID to check in: ")
#             for item in library_items:
#                 if item.item_id == item_id:
#                     item.check_in()
#         elif choice == "4":
#             print("Exiting the program. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 4.")


# if __name__ == "__main__":
#     main()





# class LibraryItem:
#     library_items = []

#     def __init__(self, item_type, item_name, item_id, item_count=0):
#         self.item_type = item_type
#         self.item_name = item_name
#         self.item_id = item_id
#         self.item_count = item_count

#         item_data = {
#             'item_type': self.item_type,
#             'item_name': self.item_name,
#             'item_id': self.item_id,
#             'item_count': self.item_count
#         }

#         if self.item_type == 'book':
#             self.author_name = input("Enter author's name for the book: ")
#             item_data['author_name'] = self.author_name
#         elif self.item_type == 'journal':
#             self.publisher_name = input("Enter publisher's name for the journal: ")
#             item_data['publisher_name'] = self.publisher_name
#         elif self.item_type == 'dvd':
#             self.director_name = input("Enter director's name for the DVD: ")
#             item_data['director_name'] = self.director_name
#         else:
#             raise ValueError("Invalid item_type. Please retry with 'book', 'journal', or 'dvd'.")

#         self.library_items.append(item_data)
        
#         if self


















#PRACTICLE SESSION
#1
# def max(a,b,c):
#     if a>b and a>c:
#         print(a, 'Is the largest number.')
#     elif b>a and b>c:
#         print(b, 'Is the largest number.')
#     elif c>a and c>b:
#         print(c, 'Is the largest number.')
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# c=int(input("Enter a number: "))
# max(a,b,c)
        


#2
# def sumList(size):
#     lts=[]
#     for i in range(size):
#         x=int(input("Enter the numbers: "))
#         lts.append(x)
#     print(lts)

#     summ=0
#     for i in lts:
#         summ+=i
#     return summ
# size=int(input("Enter number of elements: "))
# print(sumList(size))


#3
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input('enter number:'))
# print(fact(n))


#4
# def reverse_string(input_string):
    
#     reversed_string = input_string[::-1]
#     return reversed_string

# original_string = "Hello, World!"
# result = reverse_string(original_string)
# print(f"The reversed string is: {result}")


#5
# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers"
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result
# number_to_factorial = 5
# result = factorial(number_to_factorial)

# print(f"The factorial of {number_to_factorial} is: {result}")

#6
# def square_and_cube(number):
#     square = number ** 2
#     cube = number ** 3
#     return square, cube
# number_to_process = 3
# square_result, cube_result = square_and_cube(number_to_process)
# print(f"The square of {number_to_process} is: {square_result}")
# print(f"The cube of {number_to_process} is: {cube_result}")


#7
# def get_unique_elements(input_list):
#     unique_list = list(set(input_list))
#     return unique_list

# original_list = [1, 2, 2, 3, 4, 4, 5]
# distinct_elements = get_unique_elements(original_list)

# print(f"Original List: {original_list}")
# print(f"List with Distinct Elements: {distinct_elements}")



#8
# def counter(strin):
#     lowcount=0
#     upcount=0
#     for char in strin:
#         if char.islower():
#             lowcount+=1
#         else:
#             upcount+=1
#     return lowcount, upcount

# str1=input('Enter string:')
# print(counter(str1))


#9
# def is_perfect_number(number):
#     if number <= 0:
#         return False
    
#     divisors_sum = sum([i for i in range(1, number) if number % i == 0])
    
    
#     return divisors_sum == number


# number_to_check = 28
# result = is_perfect_number(number_to_check)

# if result:
#     print(f"{number_to_check} is a perfect number.")
# else:
#     print(f"{number_to_check} is not a perfect number.")



# #10
# def is_palindrome(input_str):
#     cleaned_str = ''.join(input_str.lower().split())
#     return cleaned_str == cleaned_str[::-1]

# input_string = "A man a plan a canal Panama"
# result = is_palindrome(input_string)

# if result:
#     print(f'"{input_string}" is a palindrome.')
# else:
#     print(f'"{input_string}" is not a palindrome.')
    


   










        
        
        
        
        
        