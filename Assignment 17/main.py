def add_greeting(cls):
    """A class decorator that adds a greet method to a class"""
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet
    return cls


@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
