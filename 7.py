class Employee:
    
    def get_details(self):
        self.name = input("Enter name: ")
        self.id = input("Enter employee id: ")
        self.gender = input("Enter gender: ")
        self.city = input("Enter city: ")
        self.salary = input("Enter salary: ")
    def display_details(self):
        print("*****DETAILS*****")
        print("Name of employee=",self.name)
        print("Id number=",self.id)
        print("Gender=",self.gender) 
        print("City=",self.city)
        print("Salary of employee=",self.salary)
e1 = Employee()
print("Employee Details:\n")
e1.get_details()
e1.display_details()

