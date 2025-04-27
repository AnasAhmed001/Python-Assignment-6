class Logger:
    def __init__(self, name):
        self.name = name
        print(f"Logger '{self.name}' created")
    
    def __del__(self):
        print(f"Logger '{self.name}' destroyed")


# Create logger objects
print("Creating first logger...")
logger1 = Logger("Main")

print("\nCreating second logger...")
logger2 = Logger("Debug")

print("\nDeleting first logger...")
del logger1

print("\nProgram ending...")
# When the program ends, remaining logger objects will be destroyed