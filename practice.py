class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        
class Developer(Employee):
    def __int__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
        
    def display(self):
        super().display()