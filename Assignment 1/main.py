class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")

# Create a Student object and display details
if __name__ == "__main__":
    student1 = Student("John Doe", 85)
    student1.display()
