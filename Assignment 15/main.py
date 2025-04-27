class A:
    def show(self):
        return "This is class A"


class B(A):
    def show(self):
        return "This is class B"


class C(A):
    def show(self):
        return "This is class C"


class D(B, C):
    # D inherits from both B and C, which creates a diamond inheritance pattern
    # Python's MRO (Method Resolution Order) determines which method is called
    pass


# Create an object of class D
d = D()

# Call the show method to see which version gets called
print(f"d.show() returns: {d.show()}")

# Display the Method Resolution Order (MRO) for class D
print("\nMethod Resolution Order (MRO) for class D:")
print(D.__mro__)

# Explanation of the MRO
print("\nExplanation of MRO:")
print("The method is resolved in the order listed above.")
print("Python uses C3 linearization algorithm to determine MRO.")
print("In this case, when d.show() is called, it follows the order:")
print("1. First looks in class D (but D doesn't override show())")
print("2. Then looks in class B (finds show() method there)")
print("3. If not found in B, would look in class C")
print("4. If not found in C, would look in class A")
print("5. Finally, would look in object (base class for all classes)")

# Example with a class that overrides the method
class E(B, C):
    def show(self):
        return "This is class E"

e = E()
print("\nWith class E that overrides show():")
print(f"e.show() returns: {e.show()}")

# Example calling parent's method using super()
class F(B, C):
    def show(self):
        return f"This is class F, and my parent says: {super().show()}"

f = F()
print("\nWith class F that calls parent's method using super():")
print(f"f.show() returns: {f.show()}")
print(f"In this case, super() refers to {B.__name__} according to MRO")
