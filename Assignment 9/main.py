import abc

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        """Calculate the area of the shape"""
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


# Try to instantiate the abstract class
try:
    shape = Shape()
except TypeError as e:
    print(f"Error trying to instantiate Shape: {e}")

# Create a Rectangle object
rectangle = Rectangle(5, 3)
print(f"Rectangle with width=5 and height=3 has area: {rectangle.area()}")

# Verify that Rectangle is a subclass of Shape
print(f"Is Rectangle a subclass of Shape? {issubclass(Rectangle, Shape)}")
print(f"Is rectangle an instance of Shape? {isinstance(rectangle, Shape)}")
