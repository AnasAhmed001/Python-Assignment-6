class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        return f"Hello, my name is {self.name}"


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the Person class constructor
        self.subject = subject
    
    def introduce(self):
        base_intro = super().introduce()
        return f"{base_intro}. I teach {self.subject}"


# Create a Person object
person = Person("Ali")
print(person.introduce())

# Create a Teacher object
teacher = Teacher("Sara Khan", "Computer Science")
print(teacher.introduce())

# Demonstrate inheritance
print(f"\nIs teacher an instance of Teacher? {isinstance(teacher, Teacher)}")
print(f"Is teacher also an instance of Person? {isinstance(teacher, Person)}")
