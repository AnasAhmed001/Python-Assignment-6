class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable (convention)
        self.__ssn = ssn        # Private variable (name mangling)
    
    def display_info(self):
        return f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}"


# Create an employee object
emp = Employee("Anas Ahmed", 50000, "123-45-6789")

# Try accessing the public variable
print("Accessing public variable:")
print(f"emp.name = {emp.name}")

# Try accessing the protected variable
print("\nAccessing protected variable:")
print(f"emp._salary = {emp._salary}")

# Try accessing the private variable
print("\nAccessing private variable:")
try:
    print(f"emp.__ssn = {emp.__ssn}")
except AttributeError as e:
    print(f"Error: {e}")

# Accessing private variable through name mangling
print("\nAccessing private variable through name mangling:")
print(f"emp._Employee__ssn = {emp._Employee__ssn}")

# Displaying all information using the class method
print("\nAccessing all variables through class method:")
print(emp.display_info())
