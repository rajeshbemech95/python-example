class Employee:
    def __init__(self, name):
        self.name = name
        self.department = None

    def allocate_to_department(self, department):
        self.department = department

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

# Create departments
sales_department = Department("Sales")
it_department = Department("IT")
hr_department = Department("HR")

# Get employee name from user input
employee_name = input("Enter employee name: ")

# Create an Employee instance
employee = Employee(employee_name)

# Prompt user to choose a department
print("Choose a department:")
print("1. Sales")
print("2. IT")
print("3. HR")

department_choice = int(input("Enter the department number (1-3): "))

# Allocate the employee to the chosen department
if department_choice == 1:
    sales_department.add_employee(employee)
    employee.allocate_to_department(sales_department)
elif department_choice == 2:
    it_department.add_employee(employee)
    employee.allocate_to_department(it_department)
elif department_choice == 3:
    hr_department.add_employee(employee)
    employee.allocate_to_department(hr_department)
else:
    print("Invalid department choice.")

# Display allocation information
print(f"{employee.name} has been allocated to {employee.department.name} department.")
