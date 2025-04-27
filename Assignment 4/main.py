class Bank:
    bank_name = "Default Bank"
    
    def __init__(self, branch_name):
        self.branch_name = branch_name
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
    
    def display_info(self):
        return f"Bank: {self.bank_name}, Branch: {self.branch_name}"


# Create instances
branch1 = Bank("Downtown")
branch2 = Bank("Uptown")

# Display initial bank name for both instances
print(f"Initial bank name for branch1: {branch1.bank_name}")
print(f"Initial bank name for branch2: {branch2.bank_name}")

# Change bank name using class method
Bank.change_bank_name("City Bank")

# Display updated bank name for all instances
print(f"\nAfter changing bank name:")
print(f"Updated bank name for branch1: {branch1.bank_name}")
print(f"Updated bank name for branch2: {branch2.bank_name}")

# Change bank name using instance
branch1.change_bank_name("Metro Bank")

# Display updated bank name to show it affects all instances
print(f"\nAfter changing bank name using an instance:")
print(f"Updated bank name for branch1: {branch1.bank_name}")
print(f"Updated bank name for branch2: {branch2.bank_name}")
