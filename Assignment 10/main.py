class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")
    
    def get_info(self):
        return f"{self.name} is a {self.breed}"


# Create dog instances
dog1 = Dog("Max", "German Shepherd")
dog2 = Dog("Bella", "Labrador")

# Call the bark method
print(f"Info: {dog1.get_info()}")
dog1.bark()

print(f"\nInfo: {dog2.get_info()}")
dog2.bark()

# Access instance variables directly
print(f"\nDirectly accessing instance variables:")
print(f"{dog1.name} is a {dog1.breed}")
print(f"{dog2.name} is a {dog2.breed}")
