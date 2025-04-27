class Employee:
    def __init__(self, employee_id, name, role):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.department = None  # Will be set when added to a department
    
    def get_info(self):
        dept_info = f", Department: {self.department.name}" if self.department else ""
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Role: {self.role}{dept_info}"
    
    def __str__(self):
        return self.name


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # Aggregation: Department has references to Employee objects
    
    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
            employee.department = self  # Update the employee's department reference
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            employee.department = None  # Clear the employee's department reference
    
    def list_employees(self):
        if not self.employees:
            return f"Department {self.name} has no employees."
        
        employee_list = ", ".join([str(emp) for emp in self.employees])
        return f"Department {self.name} has employees: {employee_list}"
    
    def __str__(self):
        return self.name


# Create Employee objects (independent of departments)
emp1 = Employee(101, "Ali Ahmed", "Developer")
emp2 = Employee(102, "Sara Khan", "Designer")
emp3 = Employee(103, "Usman Ali", "Manager")
emp4 = Employee(104, "Ayesha Malik", "Developer")

# Display employees before adding to departments
print("Employees before adding to departments:")
print(emp1.get_info())
print(emp2.get_info())
print(emp3.get_info())
print(emp4.get_info())

# Create Department objects
engineering = Department("Engineering")
design = Department("Design")

# Add employees to departments (aggregation)
engineering.add_employee(emp1)
engineering.add_employee(emp3)
design.add_employee(emp2)
design.add_employee(emp4)

# Display department information
print("\nDepartment information:")
print(engineering.list_employees())
print(design.list_employees())

# Display updated employee information with department
print("\nEmployees after adding to departments:")
print(emp1.get_info())
print(emp2.get_info())

# Transfer an employee between departments
print("\nTransferring Ayesha from Design to Engineering:")
design.remove_employee(emp4)
engineering.add_employee(emp4)

# Display updated department information
print(engineering.list_employees())
print(design.list_employees())

# Even if a department is deleted, employees still exist
print("\nDemonstrating that employees exist independently of departments:")
del design  # Remove the design department

# Employees that were in the design department still exist
print(emp2.get_info())  # Sara still exists but has no department
