class Person:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False


class Employee(Person):
    def isEmployee(self):
        return True
    
emp = Person("Rajesh")
print(emp.getName(), emp.isEmployee())
e= Employee("Hello")
print(e.getName(),e.isEmployee())
