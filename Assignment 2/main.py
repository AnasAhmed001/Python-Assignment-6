class Counter:
    # Class variable to keep track of how many objects have been created
    count = 0
    
    def __init__(self):
        # Increment the count whenever a new object is created
        Counter.count += 1
    
    @classmethod
    def display_count(cls):
        """Class method to display the current count of objects created"""
        return f"Number of Counter objects created: {cls.count}"


# Example usage
if __name__ == "__main__":
    # Create some Counter objects
    c1 = Counter()
    c2 = Counter()
    c3 = Counter()
    
    # Display the count using the class method
    print(Counter.display_count())  # Should output: Number of Counter objects created: 3
    
    # Create one more object
    c4 = Counter()
    
    # Display the updated count
    print(Counter.display_count())  # Should output: Number of Counter objects created: 4
