class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return self.factor * x

# Test the class
double = Multiplier(2)
triple = Multiplier(3)

# Test if object is callable
print(f"Is double callable? {callable(double)}")  # True

# Use objects as functions
print(f"Double 5: {double(5)}")     # 10
print(f"Triple 5: {triple(5)}")     # 15