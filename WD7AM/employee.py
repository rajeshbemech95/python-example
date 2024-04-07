from Person import Person

class Employee(Person):
    def isEmployee(self):
        return True
    
emp = Employee("World")
print(emp.getName())