class Car:
    def __init__(self, brand):
        # Public variable (in Python, all variables are public by default)
        self.brand = brand
    
    # Public method
    def start(self):
        return f"{self.brand} engine started!"


# Example usage
if __name__ == "__main__":
    # Create a Car object
    my_car = Car("Toyota")
    
    # Access the public variable from outside the class
    print(f"Car brand: {my_car.brand}")
    
    # Access and call the public method from outside the class
    print(my_car.start()) 