def log_function_call(func):
    """
    A decorator that logs when a function is called
    """
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is being called")
        return func(*args, **kwargs)
    return wrapper


@log_function_call
def say_hello(name="World"):
    """A simple function that says hello"""
    return f"Hello, {name}!"


# Test the decorated function
print(say_hello())
print(say_hello("Alice"))

