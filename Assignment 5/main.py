class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b


# Demonstrate usage of static method
# No need to create an instance to use static methods
print(f"MathUtils.add(5, 3) = {MathUtils.add(5, 3)}")

# Can also be called from an instance, but not recommended
math_utils = MathUtils()
print(f"math_utils.add(10, 20) = {math_utils.add(10, 20)}")